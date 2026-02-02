import pickle

def load_order(order_id):
    with open(f"orders/{order_id}.pkl", "rb") as f:
        return pickle.load(f)