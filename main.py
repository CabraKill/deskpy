from flask import (
    Flask,
    render_template,
    request,
    jsonify
)
from app.models.action import Action
from app.controllers.actionsController import ActionsController
from app.handlers.windows import Windows
from app.models.error import InvalidUsage
import socket

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    desktop = Windows()
    actions = ActionsController(app, desktop)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host=local_ip,debug=True)
