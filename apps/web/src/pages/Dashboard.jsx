// apps/web/src/pages/Dashboard.jsx
import React, { useState } from "react";
import { submitResumeTask } from "../services/api";

const Dashboard = () => {
  const [file, setFile] = useState(null);
  const [jobType, setJobType] = useState("运营");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const res = await submitResumeTask(file, jobType);
    setResult(res);
  };

  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold mb-4">上传简历任务</h2>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <select
        className="mb-4 border px-2 py-1"
        value={jobType}
        onChange={(e) => setJobType(e.target.value)}
      >
        <option>运营</option>
        <option>产品</option>
        <option>研发</option>
        <option>市场</option>
      </select>
      <button className="bg-green-600 text-white px-4 py-2 rounded" onClick={handleSubmit}>
        提交任务
      </button>

      {result && (
        <div className="mt-6 bg-gray-100 p-4 rounded shadow">
          <h4 className="font-bold">评分结果：</h4>
          <pre className="text-sm">{JSON.stringify(result, null, 2)}</pre>
          {result.report_url && (
            <a href={result.report_url} className="text-blue-600 underline" target="_blank">
              下载报告
            </a>
          )}
        </div>
      )}
    </div>
  );
};

export default Dashboard;

