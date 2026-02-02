from flask import Blueprint, request
from database import get_db

products_bp = Blueprint("products", __name__)

@products_bp.route("/search")
def search():
    q = request.args.get("q")
    db = get_db()

    sql = "SELECT name, description FROM products WHERE name LIKE '%" + q + "%'"
    rows = db.execute(sql).fetchall()

    html = ""
    for name, desc in rows:
        html += f"<h2>{name}</h2><p>{desc}</p>"

    return html