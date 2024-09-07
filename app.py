from flask import Flask



app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Blog home'


from mod_admin import admin

app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()