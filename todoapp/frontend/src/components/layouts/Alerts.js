import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
  };

  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      // alert.error("There is an error");
      // console.log(error.msg.msg.description, error.msg.msg.title);
      if (error.msg.msg.title) {
        alert.error(`Title: ${error.msg.msg.title.join()}`);
      }
      if (error.msg.msg.description) {
        alert.error(`Description: ${error.msg.msg.description.join()}`);
      }
    }

    if (message !== prevProps.message) {
      if (message.deleteTodo) alert.success(message.deleteTodo);
      if (message.addTodo) alert.success(message.addTodo);
      // if (message.passwordNotMatch) alert.error(message.passwordNotMatch);
    }
  }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = (state) => ({
  error: state.errors,
  message: state.messages,
});

export default connect(mapStateToProps)(withAlert()(Alerts));
