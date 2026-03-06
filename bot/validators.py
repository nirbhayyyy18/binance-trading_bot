def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_type(order_type):
    if order_type not in ["MARKET", "LIMIT","STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET , LIMIT, or STOP_MARKET")


def validate_quantity(qty):
    if float(qty) <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    if order_type in ["LIMIT", "STOP_LIMIT"] and price is None:
        raise ValueError("Price required for LIMIT or STOP_LIMIT order")
    