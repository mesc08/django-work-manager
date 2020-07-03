import React, { Component, Fragment } from "react";
import Header from "./layouts/Header";
import Dashboard from "./todos/Dashboard";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";
import Alerts from "./layouts/Alerts";

import { Provider } from "react-redux";
import store from "../store";

const alertOptions = {
  timeout: 3000,
  position: "top center",
};

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <AlertProvider template={AlertTemplate} {...alertOptions}>
          <Fragment>
            <Header />
            <Alerts />
            <div className="container">
              <Dashboard />
            </div>
          </Fragment>
        </AlertProvider>
      </Provider>
    );
  }
}

export default App;
// ReactDOM.render(<App />, document.getElementById("app"));
