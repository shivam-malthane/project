from flask import Flask, render_template, send_file, jsonify
import datetime, json

app = Flask(__name__)

@app.route("/")
def reports():
    return render_template("index.html")

@app.route("/download-report")
def download_report():
    # Dummy placeholder for CSV/PDF download
    return send_file("data/sample_report.pdf", as_attachment=True)

@app.route("/get-audit-logs")
def get_audit_logs():
    with open("data/audit_logs.json") as f:
        logs = json.load(f)
    return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)
