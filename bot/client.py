from binance.client import Client
import os
import time

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    
    client = Client(api_key, api_secret, testnet=True)
    client.FUTURES_TESTNET_URL = 'https://testnet.binancefuture.com/fapi'

    server_time = client.get_server_time()
    system_time = int(time.time() * 1000)
    client.timestamp_offset = server_time['serverTime'] - system_time
    
    return client