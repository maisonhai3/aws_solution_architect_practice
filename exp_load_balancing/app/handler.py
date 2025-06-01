from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello from the backend!"

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

@app.route("/sticky", methods=["GET"])
def sticky():
    session_id = request.cookies.get("AWSALB")
    return jsonify({"sticky_session": bool(session_id), "session_id": session_id})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
