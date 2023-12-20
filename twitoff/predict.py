'''U3 S11 M3'''
import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .nottwitter import vectorize_tweet


def predict_user(user0_name, user1_name, hypo_tweet_text):
    '''docstring'''
    user0 = User.query.filter(User.username == user0_name).one()
    user1 = User.query.filter(User.username == user1_name).one()

    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    vects = np.vstack([user0_vects, user1_vects])

    zeros = np.zeros(len(user0.tweets))
    ones = np.ones(len(user1.tweets))

    labels = np.concatenate([zeros, ones])

    log_reg = LogisticRegression()

    log_reg.fit(vects, labels)

    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text)

    prediction = log_reg.predict(hypo_tweet_vect.reshape(1, -1))
    return prediction[0]
