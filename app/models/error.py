from flask import jsonify
from flask_api import status

class InvalidUsage(Exception):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
    
    def __str__(self):
        return self.message