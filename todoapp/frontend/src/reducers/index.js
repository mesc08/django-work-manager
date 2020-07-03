import { combineReducers } from "redux";
import todos from "./todos";
import errors from "./errors";

export default combineReducers({
  todos,
  errors,
});
