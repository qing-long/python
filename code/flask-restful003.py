from flask import Flask
from flask_restful import fields, marshal_with, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

resource_fields = {
    'username': fields.String,
    "password": fields.String
}

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(50))

    def __str__(self):
        return "<User {}>".format(self.username)

class Test2(Resource):
    @marshal_with(resource_fields)
    def post(self):
        users = User.query.filter_by(username='admin').all()
        print(users)
        return users

api.add_resource(Test2, '/test2')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
