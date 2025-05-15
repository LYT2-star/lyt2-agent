// apps/web/src/components/LanguageToggle.jsx
import React from "react";

const LanguageToggle = ({ lang, setLang }) => {
  return (
    <div>
      <button
        className={`px-2 ${lang === "zh" ? "font-bold" : ""}`}
        onClick={() => setLang("zh")}
      >
        中文
      </button>
      |
      <button
        className={`px-2 ${lang === "en" ? "font-bold" : ""}`}
        onClick={() => setLang("en")}
      >
        EN
      </button>
    </div>
  );
};

export default LanguageToggle;

