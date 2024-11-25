from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello, World! Current time: {datetime.now()}"

if __name__ == "__main__":
    app.run(debug=True)
