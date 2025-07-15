from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/delay")
def delay():
    if time.time() - start_time < 30:
        return "Not Ready", 500
    return "Ready", 200

app.run(host='0.0.0.0', port=8080)
