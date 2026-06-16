from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

UW_KEY = "4bc930e0-299e-41dc-989b-f2890def11c1"
UW_BASE = "https://api.unusualwhales.com"
HEADERS = {
    "Authorization": f"Bearer {UW_KEY}",
    "UW-CLIENT-API-ID": "100001",
    "Accept": "application/json"
}

@app.route("/proxy")
def proxy():
    path = request.args.get("path", "")
    if not path:
        return jsonify({"error": "No path"}), 400
    resp = requests.get(UW_BASE + path, headers=HEADERS)
    response = jsonify(resp.json())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/")
def home():
    return "UW Proxy Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
