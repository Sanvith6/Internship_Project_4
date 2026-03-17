from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello, World!", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    # Development server only – use a production WSGI server in production.
    app.run(host="0.0.0.0", port=5000, debug=False)
