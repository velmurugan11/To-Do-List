const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

function fetchTasks() {
    fetch("/api/tasks") // fetch the tasks from the server
        .then(response => response.json()) // Parse the response as JSON
        .then(data => { // Use the parsed data (list of tasks)
            taskList.innerHTML = ""; //Clear the current task list
            data.forEach(task => { // Loop through the array of tasks
                const taskItem = document.createElement("li"); // Create a new <li> element for each task
                taskItem.classList.add("task-item"); // Add a class to the <li> for styling
                // taskItem.innerHTML = Set the inner HTML of the <li> to represent the task 
                // Display the task name and a checkmark if completed
                taskItem.innerHTML = `
                    <span>${task.task} ${task.completed ? "\u2714" : ""}</span> 
                    <div>
                        <button class="complete-btn" onclick="markCompleted('${task.task}')">Complete</button>
                        <button class="delete-btn" onclick="deleteTask('${task.task}')">Delete</button>
                    </div>
                `;
                taskList.appendChild(taskItem); // Append the new task item to the task list
            });
        });
}

function addTask() {
    const task = taskInput.value.trim();
    if (!task) return alert("Please enter a task!");
    fetch("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task })
    }).then(() => {
        taskInput.value = "";
        fetchTasks();
    });
}

function markCompleted(taskName) {
    fetch(`/api/tasks/${taskName}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed: true })
    }).then(fetchTasks);
}

function deleteTask(taskName) {
    fetch(`/api/tasks/${taskName}`, {
        method: "DELETE"
    }).then(fetchTasks);
}

addTaskBtn.addEventListener("click", addTask);

// Keyboard shortcut key ENTER
taskInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        addTask();
    }
});

window.onload = fetchTasks;
