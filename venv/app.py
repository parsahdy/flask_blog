from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import Development

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return 'Blog home'


from mod_admin import admin

app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()