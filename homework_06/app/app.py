from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from views.users import users_app
from models.database import db

app = Flask(__name__)
config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

app.register_blueprint(users_app, url_prefix="/users")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/about/")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(port=5000)
