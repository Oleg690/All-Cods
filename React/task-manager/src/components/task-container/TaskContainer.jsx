import React from "react";
import "./TaskContainer.css";
import TaskCard from "../tack-card/TaskCard";

function TaskContainer(props) {
  return (
    <div className="task-container">
      {props.taskList.map((item, index) => (
        <TaskCard
          key={index}
          id={item.id}
          status={item.status}
          name={item.name}
          ddate={item.ddate}
        />
      ))}
    </div>
  );
}

export default TaskContainer;
