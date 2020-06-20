from flask import Flask
import os
import time

app = Flask(__name__)


@app.route("/")
def hello():
    curr_time = time.time()
    return f"Hello World! at {curr_time}"


@app.route("/time")
def get_current_time():
    return {"time": time.time()}


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
