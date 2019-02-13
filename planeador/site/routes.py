from flask import Blueprint, render_template, url_for, flash, redirect
from planeador.site.forms import RegistrationForm, LoginForm
mod =  Blueprint('site', __name__)

@mod.route('/')
def home():
    return render_template("home.html")

@mod.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Cuenta creada para {form.username.data}', 'success')
        return redirect(url_for('site.home'))
    return render_template('register.html', title='Register', form=form)

@mod.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)