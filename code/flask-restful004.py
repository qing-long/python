from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    """
    {
        "user" : {
            "name": "buglan,
            "sex": "man"
        }
    }
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user', type=dict)
        self.parser1 = reqparse.RequestParser()
        self.parser1.add_argument('name', type=str, location=('user'))
        super(Hello, self).__init__()
    def post(self):
        args = self.parser.parse_args()
        args1 = self.parser1.parse_args(req=args)
        print(args['user'])
        print(args1['name'])
        pass

api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run()