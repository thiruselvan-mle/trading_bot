import logging

logger = logging.getLogger(__name__)

def place_market_order(symbol, side, quantity):
    logger.info(f"Market order requested: {symbol} {side} {quantity}")
    print(f"""Symbol :{symbol} \nSide :{side} \nQuantity :{quantity}""")

def place_limit_order(symbol, side, quantity, price):
    logger.info(f"LIMIT order requested: {symbol} {side} {quantity} {price}")
    print(f"""Symbol :{symbol} \nSide :{side} \nQuantity :{quantity} \nPrice : {price}""")

