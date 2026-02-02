from flask import Flask
from auth.login import login_bp
from shop.products import products_bp
from shop.orders import orders_bp

app = Flask(__name__)
app.secret_key = "dev-secret-key"

app.register_blueprint(login_bp)
app.register_blueprint(products_bp)
app.register_blueprint(orders_bp)

if __name__ == "__main__":
    app.run(debug=True)