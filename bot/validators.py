def validate_inpt(symbol, side, quantity, price):
        if symbol.lower() != "btcusdt":
            msg =  "Only symbol BTCUSDT is Available"
            action = False
            return msg, action

        if side.lower() not in ("buy", "sell"):
            msg =  "Only BUY or SELL action is Allowed"
            action = False
            return msg, action

        if quantity <= 0:
            msg =  "quantity must be greater than 0"
            action = False
            return msg, action
        
        if price is not None:      
            if price <= 0:
                msg = "Price must be greater than 0"
                action = False
                return msg, action

        return "Valid input", True