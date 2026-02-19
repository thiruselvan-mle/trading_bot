import argparse
import logging

from bot.orders import place_market_order
from bot.orders import place_limit_order
from bot.validators import validate_inpt
from bot.logging_config import setup_login

logger = logging.getLogger(__name__)

def main():
    setup_login()
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()
    symbol = args.symbol
    side = args.side
    order_type = args.type
    quantity = args.quantity
    price = args.price

    msg, action = validate_inpt(symbol, side, quantity, price)

    if  not action:
        print(msg)

    else:
        if order_type.lower() == 'market':
            place_market_order(symbol, side, quantity)
                        
        elif order_type.lower()  == 'limit':
            if price is None:
                logger.error("Price Required For LIMIT Order")
                print("Price Required For LIMIT Order")
                return
            
            place_limit_order(symbol, side, quantity, price)

        else:
            logger.error("Invalid order type!")
            print("Invalid order type")

if __name__ == "__main__":
    main()