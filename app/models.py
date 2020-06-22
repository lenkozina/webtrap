from datetime import datetime

from app import db


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logger = db.Column(db.String)
    level = db.Column(db.String)
    message = db.Column(db.String)
    path = db.Column(db.String)
    method = db.Column(db.String)
    ip = db.Column(db.String)
    creation_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    __table_args__ = ({'sqlite_autoincrement': True},)
