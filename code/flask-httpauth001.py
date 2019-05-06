from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
auth = HTTPBasicAuth()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(25))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('password is not a readable attributes')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return "<user {}>".format(self.username)
    
    def __repr__(self):
        return "<user {}>".format(self.username)


class Login(Resource):
    decorators = [auth.login_required]
    def get(self):
        return "hello {}".format(auth.username)

user_fields = {
    "username": fields.String,
    "password_hash": fields.String
}


class Register(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, location='json')
        self.parser.add_argument('password', type=str, location='json')
        super(Register, self).__init__()
    @marshal_with(user_fields)
    def post(self):
        args = self.parser.parse_args()
        try:
            user = User()
            user.username = args['username']
            user.password = args['password']
            db.session.add(user)
            db.session.commit()
            return user
        except:
            return {"message": "error"}, 409


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True     


api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

if __name__ == "__main__":
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)