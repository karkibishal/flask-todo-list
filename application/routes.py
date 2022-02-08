from application import app, db
from application.models import Todos
from flask import render_template

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('home.html', all_todos=all_todos)

@app.route('/add')
def add():
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    if latest_todo:
        new_todo = Todos(task="New Todo"+str(latest_todo.id + 1))
    else:
        new_todo = Todos(task="New Todo1")
    db.session.add(new_todo)
    db.session.commit()
    return "Added a new Todo"