from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required


class TodoForm(From):
    title = StringField('What is it ablout?', validators=[Required()])
    body = TextAraField('Description')
    done = BooleanField('Done')
    submit = SubmitField('Add')