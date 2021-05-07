## Build a GraphQL API with Python, Flask and Ariadne

https://www.twilio.com/blog/graphql-api-python-flask-ariadne

```
pip install flask ariadne flask-sqlalchemy
```

```
mkdir api
touch api/__init__.py
touch api/{models,queries,mutations}.py

touch schema.graphql
touch main.py
```

### Create database

```
python

from main import db
db.create_all()
from datetime import datetime
from api.models import Todo
today = datetime.today().date()
todo = Todo(description="Run a marathon", due_date=today, completed=False)
db.session.add(todo)
db.session.commit()
```

### Run project

```
export FLASK_APP=main.py
flask run
```


http://localhost:5000/graphql

```
query fetchAllTodos {
  todos {
    success
    errors
    todos {
      description
      completed
      id
    }
  }
}
```

```
query fetchTodo {
  todo(todoId: "1") {
    success
    errors
    todo { id completed description dueDate }
  }
}
```

```
mutation newTodo {
  createTodo(description:"Go to the dentist", dueDate:"24-10-2020") {
    success
    errors
    todo {
      id
      completed
      description
    }
  }
}
```

```
mutation markDone {
  markDone(todoId: "1") {
    success
    errors
    todo { id completed description dueDate }
  }
}
```

```
mutation {
  deleteTodo(todoId: "1") {
    success
    errors
  }
}
```

```
mutation updateDueDate {
  updateDueDate(todoId: "2", newDate: "25-10-2020") {
    success
    errors
  }
}
```

