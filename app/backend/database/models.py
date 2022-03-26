from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TextData(db.Model):
    """
    Text data table
    """
    __tablename__ = 'text_data'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
