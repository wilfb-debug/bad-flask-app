import os
from flask import Flask

app = Flask(__name__)

# Read from environment variables (Cloud Run supplies these)
DB_HOST = os.environ.get("DB_HOST", "not-set")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "not-set")

@app.get("/")
def home():
    # ✅ DB_HOST can be shown for demo if you want (not sensitive)
    # ❌ DB_PASSWORD must NEVER be returned
    return f"""
    <h1>Secure Flask App</h1>
    <p>DB Host: {DB_HOST}</p>
    <p>DB Password: [REDACTED]</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
