import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTodos } from "../../actions/todos";

class Todos extends Component {
  static PropTypes = {
    todos: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getTodos();
  }

  render() {
    return (
      <Fragment>
        <h2>To-Do's</h2>
        <table className="table table-striped">
          <thead>
            <th>Id</th>
            <th>Title</th>
            <th>Description</th>
            <th>Created</th>
            <th>Date Completed</th>
            <th>Priority</th>
            <th>User ID</th>
          </thead>
          <tbody>
            {this.props.todos.map((todo) => (
              <tr key={todo.id}>
                <td>{todo.id}</td>
                <td>{todo.title}</td>
                <td>{todo.description}</td>
                <td>{todo.created}</td>
                <td>{todo.datecompleted}</td>
                <td>{todo.priority}</td>
                <td>{todo.user}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  todos: state.todos.todos,
});

export default connect(mapStateToProps, { getTodos })(Todos);
