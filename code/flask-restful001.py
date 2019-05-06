from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return "most small api"

api.add_resource(Hello, '/', '/hello', '/helloword')


if __name__ == '__main__':
    app.run()