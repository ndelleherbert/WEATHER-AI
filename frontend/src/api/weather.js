/*import axios from "axios";

// 🌍 Auto switch between local and production
const BASE_URL =
  import.meta.env.MODE === "development"

    ? "http://localhost:8000"
    : import.meta.env.VITE_API_URL;

const API = axios.create({
  baseURL: BASE_URL,
});

export const analyzeWeather = async (payload) => {
  const res = await API.post("/weather/analysis", payload);
  return res.data;
};
*/


import axios from "axios";

const isDev = import.meta.env.DEV;

// ❌ block localhost 
const BASE_URL = isDev
  ? "http://localhost:8000"
  : import.meta.env.VITE_API_URL;

if (!isDev && (!BASE_URL || BASE_URL.includes("localhost"))) {
  throw new Error("❌ Production cannot use localhost API URL");
}

const API = axios.create({
  baseURL: BASE_URL,
});

export const analyzeWeather = async (payload) => {
  const res = await API.post("/weather/analysis", payload);
  return res.data;
};