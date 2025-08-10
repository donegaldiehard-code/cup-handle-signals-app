import yfinance as yf
from sp500 import get_sp500_tickers

def is_cup_and_handle(prices):
    # Simple detection for educational use
    window = 40
    if len(prices) < window:
        return False
    norm = (prices - prices.min()) / (prices.max() - prices.min())
    cup = norm[:int(window*0.7)]
    handle = norm[int(window*0.7):]
    if cup.min() < 0.4 and handle.min() > 0.6 and norm[-1] > 0.8:
        return True
    return False

def find_cup_handle_signals():
    tickers = get_sp500_tickers()
    signals = []
    for symbol in tickers[:20]:  # Limit for demo
        try:
            df = yf.download(symbol, period='6mo', interval='1d')
            if len(df) < 40:
                continue
            prices = df['Close'][-40:]
            if is_cup_and_handle(prices):
                signals.append({"symbol": symbol, "last_price": round(prices[-1], 2)})
        except Exception:
            continue
    return signals
