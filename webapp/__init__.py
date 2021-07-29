from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import logging

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "I Love Cookies And Cookies Love Me"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    logging.basicConfig(filename="supercoollog.log", level=logging.INFO)
    logging.info("Creating and initializing app")

    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)


    from .viewcontroller import viewsBP

    app.register_blueprint(viewsBP, url_prefix="/")

    from .model import Employee, Department

    create_db(app)
    return app


def create_db(app):
    if not path.exists("webapp/" + DB_NAME):
        from .model import Employee, Department
        logging.info("DB doesnt exists, creating DB")
        db.create_all(app=app)

        logging.info("Created DB")
