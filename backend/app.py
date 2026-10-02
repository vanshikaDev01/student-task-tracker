```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/add", methods=["POST"])
def add_task():

    data = request.get_json()

    task = data["task"]

    print("Task received:", task)

    return jsonify({
        "message": "Task received: " + task
    })

app.run(debug=True)
```
