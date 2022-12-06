from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/lenovo/Desktop/can/can/Python ile web geliştirme/Flask/todoapp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos = Todo.query.all()

        
    return render_template("index.html",todos = todos)

@app.route("/add",methods = ['POST'])
def addtodo():
    title = request.form.get("title")
    newtodo = Todo(title = title,complete = False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def todocomplete(id):
    todo = Todo.query.filter_by(id = id).first()
    """
    if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True
    """
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def todosil(id):
    
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    complete = db.Column(db.Boolean)
        
    
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)