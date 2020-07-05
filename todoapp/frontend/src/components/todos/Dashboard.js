import React, { Fragment } from "react";
import Form from "./Form";
import Todos from "./Todos";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Todos />
    </Fragment>
  );
}
