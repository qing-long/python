# flask

## flask 简单实施
- [Hello world](./helloworld.py) flask hello world 代码

- [basic struct](./basic_struct/) flask web 应用基本结构

- [flask route](./flask_route.py) flask 路由

- [flask template](./flask_template.py) flask 模板的使用


- flask url 的唯一行
    ```python
    @app.route('/people')  # /people/ 则会是404 not found
    @app.route('/people/') # /people 会跳转到 /people/ 301 重定向
    ```

- [flask todo web with jinja2 template](./todo_web.py)
    - flask todo application
    - falsk tempalte
    - flask static file
    - bootstrap datetimepicker
    - flask sqlalchemy
    - flask route
    - celery
    - async send email

- [flask todo web test](./test_todo_web.py)
    - flask test todo application

- [flask password mail](./password_mail.py)
    - wtf-form

## flask 命令行

- flask run 运行flask 用
- flask shell 进入flask应用交互式环境
- flask routes 查看当前路由映射的地址

- [flask cli command](./cli_hello/wsgi.py) 自定义flask命令行命令
    - 绝对不要直接对用户输入的内容使用safe过滤器，否则容易被植入恶意代码，导致XSS攻击