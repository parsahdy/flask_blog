from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://parsa_blog:parsa@localhost:3000/flask_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mod_admin import admin
from mod_users import users

app.register_blueprint(admin)
app.register_blueprint(users)


if __name__ == '__main__':
    from views import home
    app.route('/')(home)
    app.run()