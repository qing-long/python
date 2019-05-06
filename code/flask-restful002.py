from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('user', type=dict, help="user must dict type")
parser.add_argument('message', type=str, help='send_message must be str')
parser.add_argument('allow_people', type=str, help='allow_people must be str')
parser.add_argument('meeting_room', type=str, help='meeting_room must be str')



class Test1(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        response = {
            "user": args['user'],
            "message": args['message'],
            "allow_people": args['allow_people'],
            "meeting_room": args['meeting_room']        
        }
        return response, 200

api.add_resource(Test1, '/test1')


if __name__ == "__main__":
    app.run(debug=True)
