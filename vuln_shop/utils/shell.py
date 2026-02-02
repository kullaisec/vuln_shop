import os

def run_payment(coupon_code):
    cmd = f"echo Applying coupon {coupon_code}"
    os.system(cmd)