import argparse

from app import app, db
from app.models import Log

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Log': Log}

parser = argparse.ArgumentParser(description='Скрипт для запуска API')
parser.add_argument("-port", help="порт, который будет слушать API", required=True)
args = parser.parse_args()

if __name__ == '__main__':
    app.run(port=args.port, debug=True)
