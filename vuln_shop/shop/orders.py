from flask import Blueprint, request
from auth.session import get_current_user
from utils.serializer import load_order

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/order")
def view_order():
    order_id = request.args.get("id")
    user_id = get_current_user()

    data = load_order(order_id)
    if data["user_id"] != user_id:
        return "Forbidden", 403

    return f"Order total: {data['total']}"