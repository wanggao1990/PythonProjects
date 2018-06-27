# from app import app
#
# if __name__ == '__main__':
#     app.run()

###############################################################
from flask import request
from flask import Flask, url_for, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login',methods=['GET','POST'])
def login():
    # if request.method == 'POST':
    #     return do_the_login()
    # else:
    #     return show_the_login_form()
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
    return json.jsonify({'a':1,"n":2,"c":3, "arr":[1,2,3]})

def do_the_login():
   return "do login"

def show_the_login_form():
    return "show login form"

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


app.run()

###############################################################
# from app import app
#
# from app.dept import dept
# from app.user import user
#
#
# app.register_blueprint(user, url_prefix='/user')
# app.register_blueprint(dept, url_prefix='/dept')
#
#
# if __name__ == '__main__':
#     app.run()