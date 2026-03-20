from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Task Manager App Running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify({"message": "Task added"}), 201

@app.route('/tasks', methods=['DELETE'])
def delete_task():
    tasks.clear()
    return jsonify({"message": "All tasks deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8200)
