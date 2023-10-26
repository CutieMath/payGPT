from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys

app = Flask(__name__)
CORS(app)


@app.route("/run-script", methods=["POST"])
def run_script():
    data = request.json
    query = data["query"]

    try:
        # Run script and get the output
        result = subprocess.run(
            [
                sys.executable,
                "main.py",
                query,
            ],  # command to run the python langchain script
            capture_output=True,
            text=True,
        )
        return jsonify({"result": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e), "stderr": e.stderr}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    print("APP running on port 5000")
