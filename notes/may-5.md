# Flask Checklist for Functioning Flask Application

1. Create assignment folder
2. Navigate into the assignment folder
3. Create our virtual environment, INSTALL FLASK EVERY TIME BEFORE OPENING VIRTUAL ENVIRONMENT

   `pipenv install flask`

   `pipenv install PyMySQL`

   `pipenv install flask-bcrypt`

   **Warning**: look for pipfile.lock and pipfile

   !! If these aren't there, you have an issue that needs to be resolved

   - usually if you installed it at a higher folder, the pip files are there. just delete those and reinstall in the folder you want it in.

   - the virtual env. files are at: /Users/veronicahing/.local/share

   - remove the virtual things and reinstall

4. Go into virtual environment

   `pipenv shell`

5. Folder structure
   - pipfile and pipfile.lock
   - you need to create server.py
     - it HAS to be server.py
   - you need to also have mysqlconnection.py
     -mysqlconnection.py lives in it's own folder

## server.py file:

```py
    from flask import Flask  # Import Flask to allow us to create our app
    app = Flask(__name__)    # Create a new instance of the Flask class called "app"

    @app.route('/')          # The "@" decorator associates this route with the function immediately following
    def hello_world():
        return 'Hello World!'  # Return the string 'Hello World!' as a response

    if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
        app.run(debug=True)    # Run the app in debug mode.
```

## mysqlconnection.py file:

```
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root',
                                    password = 'root',
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close()
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

```

#Folder Structure
ex:
TODOS_PROJECT >sql >todos_app - **init**.py

> controllers (routes in server)

    -users.py
    -todos.py

> models (this is folder full of what each table is in the server)

    -user.py
    -todo.py
    -other class files associated with each table in server

- when using bcrypt, this also needs to be on top of some associated models:

```
from flask_bcrypt import Bcrypt bcrypt = Bcrypt(app)
# we are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument
```

> static

    - css files
    - images
    > templates
        - index.html
        - show_users.html
        - show_todos.html

> -server.py
