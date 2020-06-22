from flask import request

from app import db
from .models import Log
import logging


class SQLAlchemyHandler(logging.Handler):
    def emit(self, record):
        path = request.path
        method = request.method
        ip = request.remote_addr
        log = Log(logger=record.name,
                  level=record.levelname,
                  message=record.msg,
                  path=path,
                  method=method,
                  ip=ip,
        )
        db.session.add(log)
        db.session.commit()
