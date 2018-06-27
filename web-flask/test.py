from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'root page'

@app.route('/user/<user>')  
def hello_world(user):  
    return 'Hello %s' % user  

@app.route('/login')
def login():
    return 'hello'

if __name__ == '__main__':
    app.run()
