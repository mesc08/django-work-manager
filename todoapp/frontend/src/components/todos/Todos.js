import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTodos, deleteTodos } from "../../actions/todos";

class Todos extends Component {
  static propTypes = {
    todos: PropTypes.array.isRequired,
    getTodos: PropTypes.func.isRequired,
    deleteTodos: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getTodos();
  }

  render() {
    // console.log(this.props.todos);

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
            <th />
          </thead>
          <tbody>
            {this.props.todos.map((todo) => (
              <tr key={todo.id}>
                <td>{todo.id}</td>
                <td>{todo.title}</td>
                <td>{todo.description}</td>
                <td>{todo.created}</td>
                <td>{todo.datecompleted}</td>
                <td>{todo.priority ? "Yes" : "No"}</td>
                <td>{todo.user}</td>
                <td>
                  <button
                    onClick={this.props.deleteTodos.bind(this, todo.id)}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
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

export default connect(mapStateToProps, { getTodos, deleteTodos })(Todos);
