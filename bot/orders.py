from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):

    client = get_client()

    try:

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        else:

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        print("Full API response:", order)

        logger.info(order)

        return order

    except Exception as e:

        logger.error(str(e))
        print("API Error:", e)

        raise