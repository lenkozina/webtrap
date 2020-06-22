import logging

from flask import request, jsonify
from flask_restful import Resource

from app import app, api
from .handlers import SQLAlchemyHandler
from .models import Log

db_handler = SQLAlchemyHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(db_handler)

@app.errorhandler(404)
def not_found_error(error):
    logger.error('path not found')
    return jsonify(message='path not found'), 200

@app.errorhandler(405)
def not_allowed_error(error):
    logger.error('method not allowed')
    return jsonify(message='method not allowed'), 200

def process1():
    """ Функция, реализующая работу процесса 1"""
    logger.info('do process1')

def process2(notawaiting):
    """ Функция, реализующая работу процесса 2"""
    logger.info('do process2')
    if notawaiting and notawaiting == '1':
        logger.info('got notawaiting param=1')

def process3():
    """ Функция, реализующая работу процесса 3""" 
    logger.info('do process3')

class LogApi(Resource):
    def get(self):
        logger.info('get main api page')
        invalid = request.args.get('invalid', '')
        notawaiting = request.args.get('notawaiting', '')
        if invalid and invalid == '1':
            logger.error('got invalid param=1')
        else:
            process1()
            process2(notawaiting)
            process3()
        return {'message': 'get main api page'}, 200

    def post(self):
        logger.error('method not allowed')
        return {'message': 'method not allowed'}, 200

    def delete(self):
        logger.error('method not allowed')
        return {'message': 'method not allowed'}, 200

    def put(self):
        logger.error('method not allowed')
        return {'message': 'method not allowed'}, 200

    def patch(self,):
        logger.error('method not allowed')
        return {'message': 'method not allowed'}, 200


class LogList(Resource):

    def get(self):
        """
            Логи обращений к localhost:port
            Здесь можно отфильтровать записи по сообщению, методу, URL-у и уровню логгирования
            ---
            tags:
              - Логи обращений к API
            parameters:
              - name: level
                in: query
                type: string
                enum: ['INFO', 'ERROR', 'WARNING']
                description: Уровень логирования
              - name: message
                in: query
                type: string
                description: текст сообщения при логировании
              - name: path
                type: string
                description: путь, к которому происходило обращение
              - name: method
                type: string
                in: query
                enum: ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']
                description: метод
            responses:
              200:
                description: Результат фильтрации
                schema:
                  id: log
                  properties:
                    level:
                      type: string
                      description: уровень логирования
                      default: INFO
                    method:
                      type: string
                      description: метод
                      default: GET
                    path:
                      type: string
                      description: путь
                      default: /api
                    message:
                      type: string
                      description: текст сообщения
                      default: path not found
            """
        logger.info('get main api page')
        logs = Log.query
        level = request.args.get('level', '')
        if level:
            logs = logs.filter_by(level=level)
        method = request.args.get('method', '')
        if method:
            logs = logs.filter_by(method=method)
        path = request.args.get('path', '')
        if path:
            logs = logs.filter_by(path=path)
        message = request.args.get('message', '')
        if message:
            logs = logs.filter_by(message=message)
        logs = logs.order_by(Log.creation_date.desc())
        log_list = list()
        for log in logs:
            l = dict(
                id=log.id,
                logger=log.logger,
                level=log.level,
                message=log.message,
                path=log.path,
                method=log.method,
                ip=log.ip,
                creation_date=log.creation_date.isoformat()
            )
            log_list.append(l)
        return log_list, 200

api.add_resource(LogList, '/api/logs/')
api.add_resource(LogApi, '/api/')
