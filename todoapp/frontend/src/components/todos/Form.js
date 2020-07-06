import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addTodo } from "../../actions/todos";

class Form extends Component {
  state = {
    title: "",
    description: "",
    priority: "0",
  };

  static propTypes = {
    addTodo: PropTypes.func.isRequired,
  };

  onChange = (e) =>
    this.setState({
      [e.target.name]: e.target.value,
    });

  onSubmit = (e) => {
    e.preventDefault();

    const todo = {
      title: this.state.title,
      description: this.state.description,
      priority: parseInt(this.state.priority),
      user: 16,
    };

    // console.log(todo);
    this.props.addTodo(todo);
    this.setState({
      title: "",
      description: "",
      priority: "0",
    });
  };

  render() {
    const { title, description, priority } = this.state;

    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add To-do</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Title</label>
            <input
              className="form-control"
              type="text"
              name="title"
              onChange={this.onChange}
              value={title}
            />
          </div>
          <div className="form-group">
            <label>Description</label>
            <input
              className="form-control"
              type="text"
              name="description"
              onChange={this.onChange}
              value={description}
            />
          </div>
          <div className="form-check">
            <input
              className="form-check-input"
              type="checkbox"
              name="priority"
              onChange={this.onChange}
              value={priority === "0" ? "1" : "0"}
              id="defaultCheck1"
            />
            <label>Priority</label>
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addTodo })(Form);
