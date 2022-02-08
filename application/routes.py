from application import app, db
from application.models import Todos
from flask import render_template

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('home.html', all_todos=all_todos)
    