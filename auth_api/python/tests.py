import unittest
import hashlib
import jwt
from methods import Token, Restricted
key = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
role = {"admin": "admin", "noadmin": "editor", "bob": "viewer"}

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

        #admin credentials
    def test_generate_token1(self):
        # self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))
        self.assertEqual((jwt.encode({"role": role['admin']}, key, algorithm="HS256")), self.convert.generate_token('admin', 'secret'))

        #noadmin credentials
    def test_generate_token2(self):
        # self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))
        self.assertEqual((jwt.encode({"role": role['noadmin']}, key, algorithm="HS256")), self.convert.generate_token('noadmin', 'noPow3r'))

        #bob credentials
    def test_generate_token3(self):
        # self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))
        self.assertEqual((jwt.encode({"role": role['bob']}, key, algorithm="HS256")), self.convert.generate_token('bob', 'thisIsNotAPasswordBob'))

        #wrong credentials
    def test_generate_token4(self):
        # self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))
        self.assertEqual((jwt.encode({403: 'Forbidden'}, key, algorithm="HS256")), self.convert.generate_token('bob', 'test'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))
        #self.assertEqual('test', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))

if __name__ == '__main__':
    unittest.main()
