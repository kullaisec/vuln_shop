from flask import request
from utils.shell import run_payment

def checkout():
    coupon = request.args.get("coupon")
    run_payment(coupon)
    return "Payment processed"