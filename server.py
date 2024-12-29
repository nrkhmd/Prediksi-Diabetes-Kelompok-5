from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "API is running!"

@app.route('/run-script', methods=['POST'])
def run_script():
    try:
        # Replace 'db2.py' with the actual script name
        result = subprocess.run(['python', 'db.py'], capture_output=True, text=True)
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
