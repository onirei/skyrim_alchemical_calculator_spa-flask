from flask import Flask
from config import Config


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config.from_object(Config)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/skyrim'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from sac_app import routes, models