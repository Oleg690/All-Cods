import React, { useState } from "react";
import "./App.css";
import TaskContainer from "./components/task-container/TaskContainer";
import TaskCreator from "./components/task-card-creator/TaskCreator";

const data = [
    {
        id: "Task-1",
        status: "To  Do",
        name: "My Birthday!",
        ddate: new Date(2024, 7, 4),
    },
    {
        id: "Task-2",
        status: "In Progress",
        name: "2",
        ddate: new Date(2024, 5, 23),
    },
    {
        id: "Task-3",
        status: "Completed",
        name: "3",
        ddate: new Date(2025, 5, 23),
    },
    {
        id: "Task-4",
        status: "Completed",
        name: "4",
        ddate: new Date(2025, 5, 23),
    },
    {
        id: "Task-5",
        status: "To Do",
        name: "5",
        ddate: new Date(2022, 5, 23),
    },
];

function App() {
    const [taskList, setTaskList] = useState(data);

    const onNewTask = (newTask) => {
        //console.log("All Data", taskList);
        //console.log("New Task", newTask);

        setTaskList((prevState) => [
            ...prevState,
            {
                ...newTask,
                id: newTask.taskName,
                name: newTask.taskDetails,
                ddate: new Date(newTask.dueDate),
            },
        ]);
    };

    return (
        <div className="app-container">
            <div className="scrollbox-inner">
                <h3>Task Manager</h3>
                <div className="Content">
                    <TaskContainer taskList={taskList} />
                    <TaskCreator addNewTask={onNewTask} />
                </div>
            </div>
        </div>
    );
}

export default App;
