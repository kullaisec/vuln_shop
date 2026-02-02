from flask import Blueprint, request, session
from database import get_db
from utils.logger import audit_log

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    db = get_db()
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    user = db.execute(query).fetchone()

    audit_log(username)

    if user:
        session["user_id"] = user[0]
        return "Logged in"
    return "Invalid", 401