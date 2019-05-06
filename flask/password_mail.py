import base64
import os

from flask import Flask, render_template, request, current_app
from wtforms import TextAreaField, StringField, Form
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['code'] = 'jmdqkdndaeqtcagh'
app.config['SECRET_KEY'] = 'YOU-NEVER-GUESS-THE-SECRET-KEY'


class MyForm(Form):
    message = TextAreaField('message', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm(request.form)
    if request.method == 'GET':
        return render_template('index.html', form=form)
    elif request.method == 'POST' and form.validate():
        message = form.message.data
        email = form.email.data
        encrypt_message = base64.b64encode(message.encode())
        send_email(email, encrypt_message.decode())
        return 'something is ok'
    return 'something is error'


def send_email(to, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    _user = "1831353087@qq.com"
    # 需要的密码是相关设置中开启IMAP/SMTP 的授权码 _pwd是授权码
    _pwd = os.environ.get('code', None) or current_app.config.get('code', None)
    _to = to

    # 使用MIMEText构造符合smtp协议的header及body
    msg = MIMEText(message)
    msg["Subject"] = Header("password_mail", charset='utf-8')
    msg["From"] = _user
    msg["To"] = _to

    s = smtplib.SMTP_SSL(
        "smtp.qq.com", timeout=5, port=465)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)  # 登陆服务器
    try:
        s.sendmail(_user, _to, msg.as_string())  # 发送邮件
    finally:
        s.close()
