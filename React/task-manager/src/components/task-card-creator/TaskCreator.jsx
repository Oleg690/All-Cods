import React, { useState } from "react";
import "./TaskCreator.css";

function TaskCreator(props) {
  /* const [taskName, setTaskName] = useState("");
    const [taskDate, setTaskDate] = useState();
    const [taskDetails, setTaskDetails] = useState(""); */

  const [formData, setFormData] = useState({
    status: "To Do",
    taskName: "",
    dueDate: "",
    taskDetails: "",
  });

  /*  const handleNameChange = (event) => {
        setFormData((prevState) => ({
            ...prevState,
            taskName: event.target.value,
        }));
    };

    const handleDateChange = (event) => {
        setFormData((prevState) => ({
            ...prevState,
            dueDate: event.target.value,
        }));
        //setTaskDate(event.target.value);
    };

    const handleDetailsChange = (event) => {
        setFormData((prevState) => ({
            ...prevState,
            taskDetails: event.target.value,
        }));
        //setTaskDetails(event.target.value);
    }; */

  const handleSubmit = (event) => {
    event.preventDefault();

    props.addNewTask(formData);

    //console.log("Data: ", formData);
    resetForm();
  };

  function resetForm() {
    setFormData({
      taskName: "",
      dueDate: "",
      taskDetails: "",
    });
  }

  const handleInputChange = (event) => {
    setFormData((prevState) => ({
      ...prevState,
      [event.target.name]: event.target.value,
    }));
  };

  return (
    <div className="wrapper">
      <div className="card-xl">
        <h3>Create Task</h3>
        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <label>Task Name</label>
            <input
              value={formData.taskName}
              name="taskName"
              onChange={handleInputChange}
              type="text"
            />
          </div>

          <div className="form-row">
            <label>Due Date</label>
            <input
              value={formData.dueDate}
              name="dueDate"
              onChange={handleInputChange}
              type="date"
            />
          </div>

          <div className="form-row">
            <label>Task Details</label>
            <textarea
              value={formData.taskDetails}
              name="taskDetails"
              onChange={handleInputChange}
              cols="30"
              rows="10"
            ></textarea>
          </div>
          <div className="btnDiv">
            <button type="submit" className="btn">
              Create Task
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default TaskCreator;
