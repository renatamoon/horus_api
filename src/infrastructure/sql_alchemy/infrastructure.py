# THIRD PART IMPORTS
import os.path

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# PROJECT IMPORTS
from main import app


class SqlAlchemyInfrastructure:

    @classmethod
    def database_configuration(cls) -> tuple:
        basedir = os.path.abspath(os.path.dirname(__file__))

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
        app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
        db = SQLAlchemy(app)
        ma = Marshmallow(app)
        return db, ma

# if __name__ == '__main__':
#     db, ma = SqlAlchemyInfrastructure.database_configuration()
#     response = db.create_all()
#     print(response)
