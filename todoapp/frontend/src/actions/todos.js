import axios from "axios";
import { createMessage, returnErrors } from "./messages";

import { GET_TODOS, DELETE_TODO, ADD_TODO, GET_ERRORS } from "./types";

//GET TODOS
export const getTodos = () => (dispatch) => {
  axios
    .get("/api/todolists/")
    .then((res) => {
      dispatch({
        type: GET_TODOS,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

//DELETE TODOS
export const deleteTodos = (id) => (dispatch) => {
  axios
    .delete(`/api/todolists/${id}`)
    .then((res) => {
      dispatch(createMessage({ deleteTodo: "To-Do Deleted" }));
      dispatch({
        type: DELETE_TODO,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

//ADD TODO
export const addTodo = (todo) => (dispatch) => {
  axios
    .post("/api/todolists/", todo)
    .then((res) => {
      dispatch(createMessage({ addTodo: "To-Do added" }));
      dispatch({
        type: ADD_TODO,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
