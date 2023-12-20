'''U3 S11 M1'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    '''docstring'''
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    username = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)


class Tweet(DB.Model):
    '''docstring'''
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger,
                        DB.ForeignKey('user.id'),
                        nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
