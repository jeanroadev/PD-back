import unittest
from app import create_app, db

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_get_services(self):
        response = self.client.get('/services')
        self.assertEqual(response.status_code, 200)
