from flask import session, render_template, request, abort, flash
from . import admin
from mod_users.forms import LoginForm
from mod_users.models import User
from .utils import admin_only_view


@admin.route('/')
@admin_only_view
def index():
    return 'Hello from admin'

@admin.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            abort(400)
        user = User.query.filter(user.email == form.email.data).first()
        if not user:
            flash("Incorrect Credentials.", category='error')
            return render_template('admin/login.html', form=form)
        if not user.check_password(form.password.data):
            flash("Incorrect Credentials.", category='error')
            return render_template('admin/login.html', form=form)
        if not user.is_admin():
            flash("Incorrect Credentials.", category='error')
            return render_template('admin/login.html', form=form)
        session['email'] = user.email
        session['user_id'] = user.id
        session['role'] = user.role
        return "Logged in Successfully."
    if session.get('role') == 1:
        return "You are already logged in."
    return render_template('admin/login.html', form=form) 