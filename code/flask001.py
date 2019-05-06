from flask import Flask, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!!!"

@app.route('/user/<username>')
def user(username):
    return "hello {} default is {}".format(username, type(username))

@app.route('/user_id/<int:id>')
def user_id(id):
    return 'id is {}'.format(type(id))

@app.route('/float/<float:float_id>')
def float_id(float_id):
    return 'float_id is {}'.format(type(float_id))

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return ''

@app.route('/register')
def register():
    return ''






if __name__ == "__main__":
    app.run(debug=True)