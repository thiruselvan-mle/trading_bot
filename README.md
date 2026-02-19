# Binance Futures Trading Bot (USDT-M) - Internship Task

A simplified Python-based trading bot that interacts with the Binance Futures Testnet to place Market and Limit orders. This project features modular code architecture, structured logging, and robust error handling.

## 🚀 Features
- **Place Market Orders:** Instant execution on Binance Futures Testnet.
- **Place Limit Orders:** Execution at a specified price with GTC (Good Till Cancel) time in force.
- **Input Validation:** Thorough validation of symbols, sides, quantities, and prices using a dedicated validation layer.
- **Structured Logging:** All API requests, responses, and errors are logged to `trading.log` for debugging and auditing.
- **Environment Security:** Uses `.env` files to keep API credentials secure and out of version control.

## 📁 Project Structure
```text
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py         # Binance client initialization & time sync
│   ├── orders.py         # Logic for placing Market and Limit orders
│   ├── validators.py     # Input data validation logic
│   └── logging_config.py # Centralized logging configuration
├── cli.py                # Main entry point (CLI Layer)
├── trading.log           # Generated log file (API history)
├── .env                  # Environment variables (API Keys)
├── .gitignore            # Ignored files (venv, .env)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🛠️ Setup Instructions

### 1. Prerequisites
```bash
Python 3.x installed.
Binance Futures Testnet account with API credentials.
```

### 2. Installation
Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a .env file in the root directory and add your Binance Testnet API keys:

```bash
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

## 💻 How to Run Examples

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
Place a Limit Order
```
### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

## 📝 Assumptions & Notes

- Endpoint: The bot is configured to use the Binance Futures Testnet endpoint.

- Symbol: Currently optimized for ***BTCUSDT*** as per the validation rules, but extensible.

- Time Sync: Implemented a ***time_offset*** fix and ***recvWindow=60000*** to prevent "Timestamp ahead" errors common on Windows systems.

- Environment: Tested within a virtual environment (***venv***).

## 🛠️ Technologies Used

- Python 3.x

- python-binance: Official Binance API wrapper.

- python-dotenv: For managing environment variables.

- Argparse: For building the Command Line Interface.