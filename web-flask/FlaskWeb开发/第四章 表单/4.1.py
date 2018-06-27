from flask import Flask,     render_template,    session, redirect, url_for,  flash

from flask_bootstrap import Bootstrap  # 3-4

from flask_moment import Moment   # 3-11

from datetime import datetime

# 表单提交
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)

moment = Moment(app)

# 程序实例传入构造方法进行初始化，使用一个包含所有 Bootstrap 文件的基模板
bootstrap = Bootstrap(app)

############################################################################
# 设置密钥的 4-1
app.config['SECRET_KEY'] = 'hard to guess string'


# NameForm 表单中有一个名为 name 的文本字段和一个名为 submit 的提交按钮
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

#   WTForms 支持的 HTML 标准字段、验证函数
# StringField           文本字段
# TextAreaField         多行文本字段
# PasswordField         密码文本字段
# HiddenField           隐藏文本字段
# DateField             文本字段，值为 datetime.date 格式
# DateTimeField         文本字段，值为 datetime.datetime 格式
# IntegerField          文本字段，值为整数
# DecimalField          文本字段，值为 decimal.Decimal
# FloatField            文本字段，值为浮点数
# BooleanField          复选框，值为 True 和 False
# RadioField            一组单选框
# SelectField           下拉列表
# SelectMultipleField   下拉列表，可选择多个值
# FileField             文件上传字段
# SubmitField           表单提交按钮
# FormField             把表单作为字段嵌入另一个表单
# FieldList             一组指定类型的字段

# Email         验证电子邮件地址
# EqualTo       比较两个字段的值；常用于要求输入两次密码进行确认的情况
# IPAddress     验证 IPv4 网络地址
# Length        验证输入字符串的长度
# NumberRange   验证输入的值在数字范围内
# Optional      无输入值时跳过其他验证函数
# Required      确保字段中有数据
# Regexp        使用正则表达式验证输入值
# URL           验证 URL
# AnyOf         确保输入值在可选值列表中
# NoneOf        确保输入值不在可选值列表中
############################################################################


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    # name = None
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    # return render_template('index.html', name=name, form=form)  # 应用目录下的templates目录下

    if form.validate_on_submit():
        '''根据提交结果重新渲染表单 '''
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        ''' 避免刷新重新post上一次数据，应该是get '''
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)

############################################################################


@app.route('/user/')
def user_none():
    return user("")


@app.route('/user/<name>/')
def user(name):
    ls = {1, 2, 3, 4, 5, 6}
    return render_template('user.html', name=name, comments=ls)

############################################################################


@app.route('/base/')
def base():
    return render_template('heirBase.html')


############################################################################
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

############################################################################


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def page_not_found(e):
    return render_template('505.html'), 404
############################################################################

app.run()
