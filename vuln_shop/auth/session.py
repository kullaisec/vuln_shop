from flask import session

def get_current_user():
    return session.get("user_id")