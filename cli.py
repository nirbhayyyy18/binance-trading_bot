import click
from bot.orders import place_order
from bot.validators import *

@click.command()

@click.option("--symbol", required=True)
@click.option("--side", required=True)
@click.option("--order_type", required=True)
@click.option("--quantity", required=True)
@click.option("--price", required=False)
@click.option("--order_type", required=True, help="MARKET / LIMIT / STOP_LIMIT")

def main(symbol, side, order_type, quantity, price):

    try:

        validate_side(side)
        validate_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        print("\nOrder Request Summary")
        print("---------------------")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)
        print("Price:", price)

        order = place_order(symbol, side, order_type, quantity, price)

        print("\nOrder Response")
        print("---------------------")

        print("Order ID:", order.get("orderId", "N/A"))
        print("Status:", order.get("status", "N/A"))
        print("Executed Qty:", order.get("executedQty", "0"))
        print("Avg Price:", order.get("avgPrice", "0"))
        print(order)

        print("\nOrder placed successfully")

    except Exception as e:

        print("\nOrder Failed")
        print(str(e))


if __name__ == "__main__":
    main()