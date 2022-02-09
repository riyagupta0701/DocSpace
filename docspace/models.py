from flask_login import UserMixin
from enum import unique
from . import db

class Workspace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workSpaceName = db.Column(db.String(100), unique=True)
    workSpaceDesc = db.Column(db.String(2000))
    workSpaceAdminID = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workSpaces = db.relationship('Workspace')


