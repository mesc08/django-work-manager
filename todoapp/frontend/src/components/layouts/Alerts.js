import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
  };

  componentDidUpdate(prevProps) {
    const { error, alert } = this.props;
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
  }

  // componentDidUpdate(prevProps) {
  //   const { error, alert } = this.props;

  //   if (error !== prevProps.error) {
  //     if (error.msg.title) {
  //       alert.error(`Title: ${error.msg.title.join()}`);
  //     }
  //     if (error.msg.description) {
  //       alert.error(`Description: ${error.msg.description.join()}`);
  //     }
  //   }
  // }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = (state) => ({
  error: state.errors,
});

export default connect(mapStateToProps)(withAlert()(Alerts));
