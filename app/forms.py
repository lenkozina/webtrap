from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField

METHODS=('', 'GET', 'POST', 'PUT', 'PATCH', 'DELETE')
LEVELS=('', 'INFO', 'ERROR')

class LogSearchForm(FlaskForm):
    creation_date_start = DateField('creation_date_start')
    creation_date_end = DateField('creation_date_end')
    method = SelectField(
        'method',
        choices=[tag for tag in enumerate(METHODS)],
        default='',
    )
    path = StringField('path')
    level = SelectField(
        'level',
        choices=[tag for tag in enumerate(LEVELS)],
        default='',
    )
    message = StringField('message')
