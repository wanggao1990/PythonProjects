from datetime import datetime
from flask import render_template, session, redirect, url_for

from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from . import main
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('.index'))

    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())



@main.route('/user/')
def user_none():
    return user("")


@main.route('/user/<name>/')
def user(name):
    ls = {1, 2, 3, 4, 5, 6}
    return render_template('user.html', name=name, comments=ls)

############################################################################


@main.route('/base/')
def base():
    return render_template('heirBase.html')


############################################################################
@main.route('/boot/')
def boot_none():
    # return render_template('base-bootstrap.html', name = 'stranger')
    return boot('stranger')


@main.route('/boot/<name>/')
def boot(name):
    # if name == None:  #ÎÞÐ§¡£¡£¡£
    #     return render_template('base-bootstrap.html', name = 'stranger')
    # else:
    return render_template('base-bootstrap.html', name=name, current_time=datetime.utcnow())
