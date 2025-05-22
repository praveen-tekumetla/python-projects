from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path


# instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#create login manager
login_manager = LoginManager()
login_manager.init_app(app)

def create_database(app):
    if not path.exists('dinner_party/instance' + "my_database.db"):
        with app.app_context():
            db.create_all()
        print('Created Database!')
        
import routes, models
create_database(app=app)

# if __name__ == "__main__":
#     app.run(debug=True)