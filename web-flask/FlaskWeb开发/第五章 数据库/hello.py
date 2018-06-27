# coding=utf-8

import os
from flask_sqlalchemy import SQLAlchemy

from flask import Flask,     render_template,    session, redirect, url_for,  flash
from flask_bootstrap import Bootstrap  # 3-4
from flask_moment import Moment   # 3-11
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'



basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    # users = db.relationship('User', backref='role')
    users = db.relationship('User', backref='role', lazy='dynamic')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


###############################################################################################################
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/')
def user_none():
    return user("")


@app.route('/user/<name>/')
def user(name):
    ls = {1, 2, 3, 4, 5, 6}
    return render_template('user.html', name=name, comments=ls)


@app.route('/base/')
def base():
    return render_template('heirBase.html')


@app.route('/boot/')
def boot_none():
    # return render_template('base-bootstrap.html', name = 'stranger')
    return boot('stranger')


@app.route('/boot/<name>/')
def boot(name):
    # if name == None:  #无效。。。
    #     return render_template('base-bootstrap.html', name = 'stranger')
    # else:
    return render_template('base-bootstrap.html', name=name, current_time=datetime.utcnow())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 404

app.run()


exit(-1)
#####################################

db.create_all()


db.drop_all()
db.create_all()

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)

print(admin_role.id)
print(mod_role.id)
print(user_role.id)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

#db.session.add_all([admin_role, mod_role, user_role,
#      user_john, user_susan, user_david])

db.session.commit()

print(admin_role.id)
print(mod_role.id)
print(user_role.id)

admin_role.name = 'Administrator'
db.session.add(admin_role)
db.session.commit()

db.session.delete(mod_role)
db.session.commit()

print(Role.query.all())
print(User.query.all())

print(str(User.query.filter_by(role=user_role)))

user_role = Role.query.filter_by(name='User').first()

users = user_role.users
print(users)
print(users[0].role)


# class Role(db.Model):
#   # ...
#   users = db.relationship('User', backref='role', lazy='dynamic')
#   # ...

print(user_role.users.order_by(User.username).all())
print(user_role.users.count())


