import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const analyzeWeather = async (payload) => {
  const res = await API.post("/weather/analysis", payload);
  return res.data;
};