from flask import ( Flask, request, current_app, make_response, redirect,
                    abort, render_template)

app = Flask(__name__)

@app.route('/')
def index():

    """重定向 """
    # return redirect('http://www.baidu.com')

    """ 设置cookie """
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response

    return "<h1>Hello world</h1>"


@app.route('/user/<int:id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name


class User:
    pass

users =[]
for i in range(4):
    user = User()
    user.id = i
    user.name = "name%d" % i
    users.append(user)

def load_user(i):
    if i not in range(4):
        return ""
    return users[i]


@app.route('/users/<name>')
def hello(name):
    if name == None:
        return '<h1>Hello World!</h1>'
    else:
        return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(host="192.168.250.100", port=80)
