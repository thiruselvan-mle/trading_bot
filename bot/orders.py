import logging
from bot.client import get_client

logger = logging.getLogger(__name__)

def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
        
        logger.info(f"Market order Success: {order}")
        print("Market Order Placed Successfully")
        print(order)
    
    except Exception as e:
        logger.error(f"Market Order Failed: {str(e)}")
        print("Market Order Failed:", str(e))

def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=str(price)
        )

        logger.info(f"Limit Order Success: {order}")
        print("Limit Order Placed Successfully")
        print(order)

    except Exception as e:
        logger.error(f"Limit Order Failed: {str(e)}")
        print("Limit Order Failed:", str(e))

