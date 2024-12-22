from flask import Flask, jsonify, request, render_template
from models import get_all_tasks,add_task,update_task,delete_task

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tasks",methods=["GET"])
def view_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks)

@app.route("/api/tasks",methods=["POST"])
def create_task():
    data = request.json
    if "task" not in data:
        return jsonify({"error":"Task name is required"}),400 
    task = add_task(data["task"])
    return jsonify(task),201

@app.route("/api/tasks/<string:task_name>", methods=["PUT"])
def mark_task_completed(task_name):
    data = request.json
    if "completed" not in data:
        return jsonify({"error":"complete status is required"}),400
    updated_count = update_task(task_name,data["completed"])
    if updated_count:
        return jsonify({"message":"Task updated successfully"})
    return jsonify({"Error":"Task not found"}),404

@app.route("/api/tasks/<string:task_name>", methods=["DELETE"])
def delete_task_route(task_name):
    deleted_count = delete_task(task_name)
    if deleted_count:
        return jsonify({"message":"task deleted successfully"})
    return jsonify({"Error":"Task not found"}),404

if __name__=="__main__":
    app.run(debug=True)