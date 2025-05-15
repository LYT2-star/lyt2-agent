// apps/web/src/pages/PluginPage.jsx
import React, { useEffect, useState } from "react";

const BASE_URL = import.meta.env.VITE_API_BASE || "http://localhost:8000/api";

const PluginPage = () => {
  const [pluginFile, setPluginFile] = useState(null);
  const [pluginList, setPluginList] = useState([]);

  const fetchPlugins = async () => {
    const res = await fetch(`${BASE_URL}/plugin/list`);
    const data = await res.json();
    setPluginList(data);
  };

  const uploadPlugin = async () => {
    const formData = new FormData();
    formData.append("file", pluginFile);
    const res = await fetch(`${BASE_URL}/plugin/upload`, {
      method: "POST",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
      body: formData,
    });
    const result = await res.json();
    alert(result.message || "插件上传成功");
    fetchPlugins();
  };

  const togglePlugin = async (name, action) => {
    await fetch(`${BASE_URL}/plugin/${action}/${name}`, {
      method: "POST",
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    fetchPlugins();
  };

  useEffect(() => {
    fetchPlugins();
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-xl font-bold mb-4">插件管理</h2>
      <input
        type="file"
        onChange={(e) => setPluginFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded ml-2"
        onClick={uploadPlugin}
      >
        上传插件（.zip）
      </button>

      <h3 className="text-lg font-semibold mt-6 mb-2">插件列表</h3>
      <ul className="bg-white p-4 rounded shadow">
        {pluginList.map((plugin, idx) => (
          <li
            key={idx}
            className="flex justify-between items-center border-b py-2"
          >
            <div>
              <strong>{plugin.name}</strong>: {plugin.description}
            </div>
            <div>
              {plugin.enabled ? (
                <button
                  className="text-red-600 hover:underline"
                  onClick={() => togglePlugin(plugin.name, "disable")}
                >
                  禁用
                </button>
              ) : (
                <button
                  className="text-green-600 hover:underline"
                  onClick={() => togglePlugin(plugin.name, "enable")}
                >
                  启用
                </button>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PluginPage;

