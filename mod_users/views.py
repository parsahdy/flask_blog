from flask import request, render_template, flash
from sqlalchemy.exc import IntegrityError

from app import db

from . import users
from .models import User
from .forms import RegisterForm
from .utils import add_to_redis, send_signup_message, get_form_redis, delete_from_redis


@users.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)
        if form.password.data != form.confirm_password.data:
            error_msg = 'Password and Confirm_password does not match'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
            return render_template('users/register.html', form=form)
        old_user = User.query.filter(User.email.ilike(form.email.data).first())
        if old_user:
            flash("Email has been taken", "error")
            return render_template('users/register.html', form=form)
        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            token = add_to_redis(new_user, 'register')
            send_signup_message(new_user, token)
            flash('You created your account successfully', 'success')
        except IntegrityError:
            db.session.rollback()
            flash("Email has been taken", "error")
    return render_template('users/register.html', form=form)


@users.route('/confirm/')
def confirm_registeration():
    email = request.args.get('email')
    token = request.args.get('token')

    user = User.query.filter(user.email.ilike(email)).first()
    if not user:
        return 'user not found'
    if user.active:
        return 'user already activated'
    token_from_redis = get_form_redis(user, 'register')
    if not token_from_redis:
        return "wrong/Expired Token!"
    
    if token != token_from_redis.decode('UTF-8'):
        return "wrong/Expired Token!"
    
    user.active = True
    db.session.commit()
    delete_from_redis(user, 'register')

    return '1'