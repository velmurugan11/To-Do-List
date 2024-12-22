from config import get_database

db = get_database()
tasks_collection = db["tasks"]

# This function fetches all tasks from the tasks_collection in the MongoDB database.
def get_all_tasks():
    return list(tasks_collection.find({},{"_id":0}))

# This function adds a new task to the tasks_collection with a name and sets its completion status to False (indicating that the task is not completed).
def add_task(task_name):
    task = {"task":task_name,"completed":False}
    tasks_collection.insert_one(task)
    return task

# This function updates the completion status of a task in the database.
def update_task(task_name,completed):
    result = tasks_collection.update_one({"task":task_name},{"$set":{"completed":completed}})
    return result.modified_count

# This function deletes a task from the database based on its name.
def delete_task(task_name):
    result = tasks_collection.delete_one({"task":task_name})
    return result.deleted_count