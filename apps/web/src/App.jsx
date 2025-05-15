// apps/web/src/App.jsx
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import PluginPage from "./pages/PluginPage";
import LanguageToggle from "./components/LanguageToggle";

const App = () => {
  const [lang, setLang] = useState("zh");

  const token = localStorage.getItem("token");

  return (
    <Router>
      <div className="flex justify-between items-center bg-gray-100 px-6 py-2">
        <h1 className="font-bold text-lg">羚羊T2 Agent</h1>
        <LanguageToggle lang={lang} setLang={setLang} />
      </div>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route
          path="/dashboard"
          element={token ? <Dashboard /> : <Navigate to="/login" />}
        />
        <Route
          path="/plugins"
          element={token ? <PluginPage /> : <Navigate to="/login" />}
        />
      </Routes>
    </Router>
  );
};

export default App;

