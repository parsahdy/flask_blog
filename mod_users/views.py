from flask import request, render_template, flash
from app import db
from . import users
from .models import User
from .forms import RegisterForm

@users.route('/register/', methodes=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template('users/register.html', form=form)
        if form.password.data != form.confirm_password.data:
            error_msg = 'Password and Confirm_password does not match'
            form.password.errors.append(error_msg)
            form.confirm_password.errors.append(error_msg)
        new_user = User()
        new_user.username = form.username.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You created your account successfully', 'success')
    return render_template('users/register.html', form=form)