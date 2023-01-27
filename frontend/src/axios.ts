import axios from "axios";

// Authenticated Axios Configurations
const authAxios = axios.create({
  baseURL: process.env.publicPath,
  timeout: 5000,
});

export default authAxios;
