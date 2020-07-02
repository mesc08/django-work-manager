import axios from "axios";

import { GET_TODOS } from "./types";

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
    .catch((err) => console.log(err));
};
