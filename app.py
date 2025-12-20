import time
import socket
from flask import Flask

app = Flask(__name__)

# ❌ BAD: Hardcoded secret
DB_PASSWORD = "super-secret-password"

@app.route("/")
def home():
    return f"""
    <h1>Bad Flask App</h1>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Database password: {DB_PASSWORD}</p>
    """

@app.route("/slow")
def slow():
    time.sleep(10)
    return "This request was very slow"

@app.route("/crash")
def crash():
    return 1 / 0

if __name__ == "__main__":
    print("Starting BAD Flask app...")
    app.run(host="0.0.0.0", port=5000)
