from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# @app.route('/<name>')
# def index(name):            # 动态路由, 这2个可以分开写

@app.route('/')
def index():
    print(request.accept_charsets)
    print(request.accept_encodings)
    print(request.accept_languages)
    print(request.accept_mimetypes)
    print(request.access_route)
    print(request.trusted_hosts)
    print(request.authorization)


    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/users/<name>')
def hello(name):
    #
    # print(request.base_url)
    # print(request.url)
    # print(request.url_root)
    # print(request.url_rule)
    # print(request.query_string)
    # print(request.url_charset)

    if name == None:
        return '<h1>Hello World!</h1>'
    else:
        return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(host="192.168.3.100", port=80)
