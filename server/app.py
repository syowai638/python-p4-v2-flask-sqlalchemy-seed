from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db  # Import the db defined in models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

# Initialize db with app
db.init_app(app)
migrate = Migrate(app, db)

from models import Pet
