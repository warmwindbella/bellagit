from datetime import datetime
from . import db
from app.exception import ValdationError


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column('id', db.Integer, primary_ley=True)
    title = db.Column(db.String(50))
    body = db.Cplumn(db.String)
    done = db.Column(db.Boolean)
    publication_date = db.Column(db.Datetime)
    
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.done = False
        self.publication_date = datetime.utcnow()
    
    @staticmethod
    def from_json(json_post):
        title = json_post.get('title')
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('post does not have a body')
        return Todo(title, body)
    
    
    def to_json(self):
        todo_json = {
                'id' : self.id
                'title' : self.title
                'body' : self.body
                'donr' : self.done
        }
        return todo_json


    def __repr__(self):
        return "<Todo '%s'>" % self.title