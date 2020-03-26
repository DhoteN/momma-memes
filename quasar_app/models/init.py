from alchemy import alchemy
from app import db, quota_namespace
import datetime
import json
import decimal

__author__ = 'nikita'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT, DECIMAL
from alchemy import *

import flask


# db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(500), nullable=False)
    firstName = db.Column(db.String(150), nullable=False)
    lastName = db.Column(db.String(150), nullable=True)
    participantId = db.Column(db.String(150), nullable=False, unique=True, index=True)
    roleId = db.Column(db.Integer,db.ForeignKey('role.id'), nullable=False)
    # role=db.relationship('Role',backref=db.backref('users',lazy='dynamic'))
    teamId = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(1000), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    privilege = db.Column(db.String(50), nullable=False,default='user')
    expiryToken = db.Column(db.String(50), nullable=True)
    expiryDate = db.Column(db.DateTime, nullable=True)
    is_first_login = db.Column(db.Boolean, nullable=True)
    access_list = db.Column(db.VARCHAR(500), nullable=True)
    country_list = db.Column(db.TEXT(), nullable=True)
    locked = db.Column(db.Boolean, default=False)
    login_attempt = db.Column(db.Integer, default=0)
    last_passwords = db.Column(db.TEXT())
    last_login = db.Column(db.DateTime)
    sso_username = db.Column(db.String(250))
    data_masking = db.Column(db.Boolean, default=False)
