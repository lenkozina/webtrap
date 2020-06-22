import unittest
from http import HTTPStatus

from app import app, db
from app.models import Log


class LogCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        response = self.app.get("/api/")
        MESSAGES = [
            'get main api page',
            'do process1',
            'do process2',
            'do process3'
        ]
        # проверярем, что сделались все нужные записи в таблицу
        for message in MESSAGES:
            log = Log.query.filter_by(
                message=message,
                level='INFO',
                path='/api/',
                method='GET',
            )
            self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_post(self):
        response = self.app.post("/api/")
        log = Log.query.filter_by(
            message='method not allowed',
            level='ERROR',
            path='/api/',
            method='POST',
        )
        self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_put(self):
        response = self.app.put("/api/")
        log = Log.query.filter_by(
            message='method not allowed',
            level='ERROR',
            path='/api/',
            method='PUT',
        )
        self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_patch(self):
        response = self.app.patch("/api/")
        log = Log.query.filter_by(
            message='method not allowed',
            level='ERROR',
            path='/api/',
            method='PATCH',
        )
        self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_delete(self):
        response = self.app.delete("/api/")
        log = Log.query.filter_by(
            message='method not allowed',
            level='ERROR',
            path='/api/',
            method='DELETE',
        )
        self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_get_invalid_param(self):
        response = self.app.get("/api/?invalid=1")
        log = Log.query.filter_by(
            message='got invalid param=1',
            level='ERROR',
            path='/api/',
            method='GET',
        )
        self.assertEqual(log.count(), 1)
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_path_not_found(self):
        response = self.app.delete("/path_not_exist")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

if __name__ == '__main__':
    unittest.main(verbosity=2)
