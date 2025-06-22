from flask import Flask, render_template, jsonify
import speedtest
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speedtest")
def run_speedtest():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results = st.results.dict()

    return jsonify({
        "download": round(results["download"] / 1_000_000, 2),
        "upload": round(results["upload"] / 1_000_000, 2),
        "ping": round(results["ping"], 2)
    })

@app.route("/cpu")
def cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    return jsonify({"cpu": cpu})

if __name__ == "__main__":
    # Important fix: listen on all interfaces for Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
