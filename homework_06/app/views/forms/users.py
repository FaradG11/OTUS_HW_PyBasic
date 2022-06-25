from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    username = StringField(
        label="Username",
        name="user_name",
        validators=[
            DataRequired(),
            Length(min=3, max=100),
        ]
    )
    name = StringField(
        label="long name of the user",
        name="name"
    )
    email = StringField(
        label="e-mail",
        name="e-mail"
    )


