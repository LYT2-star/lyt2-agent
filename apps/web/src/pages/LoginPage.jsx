// apps/web/src/pages/LoginPage.jsx
import React, { useState } from "react";
import { login } from "../services/api";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    const res = await login(username, password);
    console.log("登录响应：", res);  // ✅ 加上这一句  
    if (res?.access_token) {
      localStorage.setItem("token", res.access_token);
      navigate("/dashboard");
    } else {
      alert("登录失败，请检查用户名或密码");
    }
  };

  return (
    <div className="w-full h-screen flex items-center justify-center bg-gray-100">
      <div className="p-6 bg-white shadow-md rounded w-96">
        <h2 className="text-xl font-bold text-center mb-4">登录 LYT2 Agent</h2>
        <input
          className="w-full mb-3 border px-3 py-2"
          placeholder="用户名"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className="w-full mb-3 border px-3 py-2"
          type="password"
          placeholder="密码"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="w-full bg-blue-600 text-white py-2 rounded" onClick={handleLogin}>
          登录
        </button>
      </div>
    </div>
  );
};

export default LoginPage;

