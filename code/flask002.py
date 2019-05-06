from flask import Flask, url_for, request, render_template, session, g, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOU NEVER GUESS THE KEY'

@app.route('/login')
def login():
    return "login page"

@app.route('/register')
def register():
    return 'register page'

@app.route('/user/<username>')
def user(username):
    return username

with app.test_request_context():
    url_for('login')
    url_for('register')
    url_for('login', next='/')
    url_for('user', username='buglan')

@app.route('/methods', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def methods():
    if request.method == 'GET':
        return "GET method"
    
    if request.method == 'HEAD':
        # head no response
        return "HEAD method"

    if request.method == 'POST':
        return "POST method"

    if request.method == 'PUT':
        return "PUT method"

    if request.method == 'DELETE':
        return "DELETE method"

    if request.method == 'OPTIONS':
        return "OPTIONS method"

@app.route('/render_templates')
def render():
    session['username'] = 'buglan'
    g.name = 'buglan'
    flash('this is flash message')
    return render_template('flask_index.html')

if __name__ == '__main__':
    app.run(debug=True)