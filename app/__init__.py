from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'
UPLOAD_FOLDER = './app/static/uploads'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # added just to suppress a warning
app.config.from_object(__name__)
db = SQLAlchemy(app)


from app import views
