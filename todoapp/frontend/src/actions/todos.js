import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";
import { GET_TODOS, DELETE_TODO, ADD_TODO } from "./types";

// GET TODOS
export const getTodos = () => (dispatch, getState) => {
  axios
    .get("/api/todolists", tokenConfig(getState))
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

// DELETE TODO
export const deleteTodos = (id) => (dispatch, getState) => {
  axios
    .delete(`/api/todolists/${id}`, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ deleteTodo: "Todo Deleted" }));
      dispatch({
        type: DELETE_TODO,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

// ADD TODO
export const addTodo = (lead) => (dispatch, getState) => {
  const user = getState().auth.user.id;
  lead = {
    ...lead,
    user: user,
  };
  axios
    .post(`/api/todolists/`, lead, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ addTodo: "Todo Added" }));
      dispatch({
        type: ADD_TODO,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
