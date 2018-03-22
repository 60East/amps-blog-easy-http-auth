"""
Basic Authentication code is based on the code snippet by
Armin Ronacher: http://flask.pocoo.org/snippets/8/
"""

from flask import Flask, request, Response
from functools import wraps


# create the flask app example
app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username/password is valid."""
    return username == 'falken' and password == 'joshua'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="AMPS Authentication"'}
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route('/<username>')
@requires_auth
def permission_document(username):
    return """
        {
          "logon": true,
          "replication-logon": true,
          "topic": [{
              "topic": ".*",
              "read": true,
              "write": true
            }],
          "admin": [{
              "topic": "/amps/administrator",
              "read": true,
              "write": false
            }, {
              "topic": ".*",
              "read": true,
              "write": false
            }]
        }
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

