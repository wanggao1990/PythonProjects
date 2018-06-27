from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  #应用目录下的templates目录下

@app.route('/user/<name>')
def user(name):
    ls ={1,2,3,4,5,6}
    return render_template('user.html', name=name, comments = ls)


@app.route('/base')
def base():
    return render_template('heirBase.html')  

app.run()
