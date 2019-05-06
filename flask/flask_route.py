from flask import Flask
from flask import Blueprint


def create_app():
    app = Flask(__name__)

    # 装饰器模式注册的路由
    @app.route('/')
    def index():
        return 'hello world'

    def home():
        return 'home'

    # 另一种方式注册路由
    # 3个参数 rule endpoint view_func
    app.add_url_rule('/home', 'home', view_func=home)  # 支持多种方式注册路由

    @app.route('/a')
    @app.route('/b')
    @app.route('/c')
    def a():
        return 'a'

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
