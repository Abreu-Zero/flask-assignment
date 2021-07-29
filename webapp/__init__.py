from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "I Love Cookies And Cookies Love Me"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .viewcontroller import viewsBP

    app.register_blueprint(viewsBP, url_prefix="/")

    from .model import Employee, Department

    create_db(app)
    return app


def create_db(app):
    if not path.exists("webapp/" + DB_NAME):
        from .model import Employee, Department
        print("DB doesnt exists, creating DB")
        db.create_all(app=app)

        print("Created DB")
