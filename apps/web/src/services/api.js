// apps/web/src/services/api.js
const BASE_URL = import.meta.env.VITE_API_BASE || "http://115.190.35.2:8000/api";

export const login = async (username, password) => {
  const res = await fetch(`${BASE_URL}/user/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  return res.json();
};

export const submitResumeTask = async (file, job_type = "运营") => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("job_type", job_type);
  const res = await fetch(`${BASE_URL}/task/resume`, {
    method: "POST",
    headers: { Authorization: "Bearer " + localStorage.getItem("token") },
    body: formData,
  });
  return res.json();
};

