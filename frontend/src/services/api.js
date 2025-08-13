import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api",  // adjust if your Django API is different
});

export default API;
