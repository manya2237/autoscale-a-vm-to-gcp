from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask CPU Monitoring App Running!"

@app.route('/high-load')
def high_load():
    subprocess.Popen(["stress", "--cpu", "4", "--timeout", "30"])
    return "High CPU load started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)