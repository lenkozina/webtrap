import unittest
from http import HTTPStatus

from app import app, db


class LogCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        response = self.app.get("/api")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_post(self):
        response = self.app.post("/api")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_put(self):
        response = self.app.put("/api")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_patch(self):
        response = self.app.patch("/api")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_delete(self):
        response = self.app.delete("/api")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_get_invalid_param(self):
        response = self.app.delete("/api?invalid=1")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

    def test_path_not_found(self):
        response = self.app.delete("/path_not_exist")
        self.assertEqual(response.status_code, int(HTTPStatus.OK))

if __name__ == '__main__':
    unittest.main(verbosity=2)
