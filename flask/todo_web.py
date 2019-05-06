from datetime import datetime

from flask import Flask, abort, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='./template', static_folder='./static')

# config sqlite config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    created_time = db.Column(db.DateTime)
    finished_time = db.Column(db.DateTime)

    def __init__(self, title):
        self.title = title
        self.created_time = datetime.now()

    def __repr__(self):
        return f'<TODO id is {self.id} title is {self.title}>'


@app.before_first_request
def before_first_do():
    """
    create database or do init
    """
    try:
        db.create_all()
    except Exception as e:
        print(e)
    else:
        pass


@app.route('/')
def index():
    todos = Todo.query.order_by(db.desc(Todo.status)).all()
    time = datetime.now()
    return render_template('todo/index.html', time=time, todos=todos)


@app.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'GET':
        return render_template('todo/add_todo.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        todo = Todo(title=title)
        # 2018-10-28 11:00:00
        todo.created_time = datetime.strptime(
            request.form.get('created_time', None), '%Y-%m-%d %H:%M:%S')
        todo.finished_time = datetime.strptime(
            request.form.get('finished_time', None), '%Y-%m-%d %H:%M:%S')
        todo.status = False
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        # bad request
        abort(400)


@app.route('/toggle')
def toggle():
    id = request.args.get('id')
    todo = Todo.query.get_or_404(id)
    todo.status = (not todo.status)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_todo')
def delete_todo():
    """
    删除 todo中的一项
    """
    id = request.args.get('id')
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update_todo', methods=['GET', 'POST'])
def update_todo():
    if request.method == 'GET':
        id = request.args.get('id', None)
        if id:
            todo = Todo.query.get_or_404(id)
            return render_template('todo/update_todo.html', todo=todo)
    elif request.method == 'POST':
        id = request.form.get('id')
        title = request.form.get('title')
        todo = Todo.query.get_or_404(id)
        todo.title = title
        todo.created_time = datetime.strptime(
            request.form.get('created_time', None), '%Y-%m-%d %H:%M:%S')
        todo.finished_time = datetime.strptime(
            request.form.get('finished_time', None), '%Y-%m-%d %H:%M:%S')
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        abort(400)


@app.route('/search_todo', methods=['GET', 'POST'])
def search_todo():
    if request.method == 'GET':
        return render_template('todo/search_todo.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        print(title)
        todos = Todo.query.filter(Todo.title.like('%' + title + '%')).all()
        time = datetime.now()
        return render_template('todo/index.html', todos=todos, time=time)

    return "hello world"


@app.route('/test')
def test():
    return render_template('todo/test.html')


if __name__ == "__main__":
    app.run(debug=True)
