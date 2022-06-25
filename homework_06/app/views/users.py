import logging

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, InternalServerError

from views.forms import UserForm
from models import User
from models.database import db

log = logging.getLogger(__name__)

users_app = Blueprint("users_app", __name__)


@users_app.get("/", endpoint="list")
def get_users_list():

    users = User.query.all()
    return render_template(
        "users/list.html",
        users=users,
    )

@users_app.get("/test/")
def test_page():
    return render_template(
        "users/test.html"
    )


@users_app.route("/<int:user_id>/", methods=["GET", "DELETE"], endpoint="details")
def get_user_by_id(user_id: int):
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User #{user_id} not found!")

    if request.method == "GET":
        return render_template(
            "users/details.html",
            user=user,
        )

    user_name = user.name
    db.session.delete(user)
    db.session.commit()
    flash(f"Deleted user {user_name!r}", "warning")
    url = url_for("users_app.list")
    return {"ok": True, "url": url}


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400

    user_name = form.username.data
    name = form.name.data
    email = form.email.data

    user = User(username=user_name, name=name, email=email)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save user {user_name!r}, probably username is not unique!"
        form.form_errors.append(error_text)
        return render_template("users/add.html", form=form), 400

    except DatabaseError:
        log.exception("could not save user %r", user_name)
        raise InternalServerError(f"could not save user {user_name!r}")

    flash(f"Created new user: {user.name}", "success")
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
