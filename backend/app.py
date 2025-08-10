from flask import Flask, jsonify
from detector import find_cup_handle_signals

app = Flask(__name__)

@app.route("/signals")
def get_signals():
    signals = find_cup_handle_signals()
    return jsonify({"signals": signals})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)