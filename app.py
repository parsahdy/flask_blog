from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run()