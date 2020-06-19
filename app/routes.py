import logging

from flask import request, render_template, redirect, url_for

from app import app
from .forms import LogSearchForm, LEVELS, METHODS
from .handlers import SQLAlchemyHandler
from .models import Log

db_handler = SQLAlchemyHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(db_handler)


@app.errorhandler(404)
def not_found_error(error):
    logger.error('path not found')
    return redirect(url_for('get'), code=200)

@app.errorhandler(405)
def not_found_error(error):
    logger.error('method not allowed')
    return redirect(url_for('get'), code=200)

def process1():
    """ Функция, реализующая работу процесса 1"""
    logger.info('do process1')


def process2(request):
    """ Функция, реализующая работу процесса 2"""
    logger.info('do process2')
    notawaiting = request.args.get('notawaiting')
    if notawaiting and notawaiting == '1':
        logger.info('got notawaiting param=1')


def process3():
    """ Функция, реализующая работу процесса 3"""
    logger.info('do process3')


@app.route("/api", methods=['GET', 'POST'])
def get():
    """ Функция для обработки маршрутов к /api. """
    form = LogSearchForm()
    if request.method == 'POST':
        logger.error('method not allowed')
        items = Log.query
        if form.creation_date_start.data:
            items = items.filter(Log.creation_date > form.creation_date_start.data)
        if form.creation_date_end.data:
            items = items.filter(Log.creation_date < form.creation_date_end.data)
        if form.message.data:
            items = items.filter_by(message=form.message.data)
        if form.level.data and form.level.data != '0':
            items = items.filter_by(level=LEVELS[int(form.level.data)])
        if form.method.data and form.method.data != '0':
            items = items.filter_by(method=METHODS[int(form.method.data)])
        if form.path.data:
            items = items.filter_by(path=form.path.data)
        return render_template('form.html',
                               form=form,
                               items=items,
                               count=items.count()), 200
    logger.info('get main api page')
    invalid = request.args.get('invalid')
    if invalid and invalid == '1':
        logger.error('got invalid param=1')
        print('got invalid param=1')
    else:
        process1()
        process2(request)
        process3()
    return render_template('form.html', form=form, items=Log.query.all()), 200
