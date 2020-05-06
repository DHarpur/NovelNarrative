import sys
from flask import Flask
from flask_cors import CORS
from views.userView import userRoutes
from views.bookView import bookRoutes
from views.movieView import movieRoutes

print(sys.path)
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

app.register_blueprint(userRoutes)
app.register_blueprint(bookRoutes)
app.register_blueprint(movieRoutes)


@app.route("/")
def index():
    return "Hello"


if __name__ == '__main__':
    app.secret_key = b'G\x0e\x07\x94\xf3ASGP\xe9\x98\x82\x07[\\\xeeq\xda =\xbf3$*'
    app.run()
