from flask import (
    Flask,
    render_template,
    request
)

from src.models.action import Action
from src.controllers.actions import Actions
from src.handlers.win import Windows
# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"


@app.route('/')
def home():
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    desktop = Windows()
    actions = Actions(app, desktop)
    app.run(debug=True)
