from flask import Flask, render_template

from flask_bootstrap import Bootstrap  # 3-4

from flask_moment import Moment   # 3-11

from datetime import datetime  

app = Flask(__name__)

moment = Moment(app)


# 程序实例传入构造方法进行初始化，使用一个包含所有 Bootstrap 文件的基模板
bootstrap = Bootstrap(app)

############################################################################
@app.route('/')
def index():
    return render_template('index.html')  #应用目录下的templates目录下
                           

############################################################################
@app.route('/user/')
def user_none():
    return user("stranger")

@app.route('/user/<name>/')
def user(name):
    ls ={1,2,3,4,5,6}
    return render_template('user.html', name=name, comments = ls)

############################################################################
@app.route('/base/')
def base():
    return render_template('heirBase.html')
                          

############################################################################
@app.route('/boot/')
def boot_none():
    #return render_template('base-bootstrap.html', name = 'stranger')
    return boot('stranger')
    
@app.route('/boot/<name>/')
def boot(name):   
    #if name == None:  #无效。。。
    #    return render_template('base-bootstrap.html', name = 'stranger')
    #else:
    return render_template('base-bootstrap.html',name=name,
                            current_time=datetime.utcnow())

############################################################################
@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404


############################################################################
app.run()
