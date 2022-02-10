from flask_login import UserMixin
from enum import unique
from . import db

class Workspace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workSpaceName = db.Column(db.String(100), nullable=False)
    workSpaceDesc = db.Column(db.String(10000), nullable=False)
    workSpaceAdminID = db.Column(db.Integer, db.ForeignKey('user.id'))

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    uploadedBy = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workSpaces = db.relationship('Workspace')
    files = db.relationship('Upload')


