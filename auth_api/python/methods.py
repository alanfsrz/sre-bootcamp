import jwt
from flask import jsonify
import hashlib
key = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"
salt = {"admin": "F^S%QljSfV", "noadmin": "KjvFUC#K*i", "bob": "F^S%QljSfV"}
dict = {"admin": "15e24a16abfc4eef5faeb806e903f78b188c30e4984a03be4c243312f198d1229ae8759e98993464cf713e3683e891fb3f04fbda9cc40f20a07a58ff4bb00788", "noadmin": "89155af89e8a34dcbde088c72c3f001ac53486fcdb3946b1ed3fde8744ac397d99bf6f44e005af6f6944a1f7ed6bd0e2dd09b8ea3bcfd3e8862878d1709712e5", "bob": "2c9dab627bd73b6c4be5612ff77f18fa69fa7c2a71ecedb45dcec45311bea736e320462c6e8bfb2421ed112cfe54fac3eb9ff464f3904fe7cc915396b3df36f0"}
role = {"admin": "admin", "noadmin": "editor", "bob": "viewer"}
dbtoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI"
class Token:
    def generate_token(self, username, password):
        if (username in dict):
            h=hashlib.sha512((password + salt[username]).encode('utf-8'))
            if (h.hexdigest() == (dict[username])):
                return jwt.encode({"role": role[username]}, key, algorithm="HS256")
                #Store the token on the db
        return jwt.encode({403: 'Forbidden'}, key, algorithm="HS256")


class Restricted:
    def access_data(self, authorization):
        #db query to validate if a token exist and is the same as the one received in generate_token(username, password)
        if (dbtoken == authorization):
            return "You are under protected data"
        return "Token is invalid, please try to re-login"
