<p align="center">
  <img src="./static/assets/log.png" width="160" />
</p>   


## 🛡️ License & Usage Notice

本项目采用自定义开放协议（基于 MIT），**仅允许非商业用途**。

如您希望将本项目用于商业产品或商业部署，请先取得项目作者书面授权。

 This project is licensed under a custom MIT-based open license, for **non-commercial use only**.
 Please contact the author if you intend to use this project for commercial purposes.



研发团队:
主研发：北京市密网信息科技有限公司（项目规划 + 交付控制）

技术支持：北京市密网信息科技有限公司（全栈代码开发 + 模块封装）


特此声明：

本项目遵循 自定义 MIT 协议 + 禁止商业化条款。

您可以自由学习、研究、使用、修改和传播本项目，但禁止以任何形式将其用于商业目的，包括但不限于：

将本项目代码直接用于收费产品或服务；

将项目整体或修改版本进行销售、二次授权；

使用该项目部署 SaaS 服务后对外收费；

如需商业使用，请联系作者北京市密网信息科技有限公司（可在 Issues 留言或发送邮件mtl15739501059@163.com）；

备注：
本项目及附属材料所涉及的所有 "羚羊" 二字命名均来自北京市密网信息科技有限公司的凌羪商标的谐音，知悉；

# 🦌 LYT2 Agent 开源版（羚羊T2）

LYT2 是一个国产开源 AI Agent 系统，支持插件链、多任务协同执行，适用于可落地业务流程。


## ✨ 功能特性
- ✅ 多智能体调度架构
- ✅ 插件链执行（支持热插拔）
- ✅ 应用落地完整实现
- ✅ 前后端分离（React + FastAPI）
- ✅ 一键部署（Docker Compose）
- ✅ 支持国产大模型或 GPT 接入


## ✨  项目特色

- 🧠  多Agent智能体系统（任务调度 + 插件执行）
- 📎  插件市场支持（热插拔，上传即用）
- 📂  内置任务链：股票分析、报表分析
- 🌐  Web UI 界面（React + TailwindCSS）
- 🗣️  支持中英文界面切换（i18n）
- 🚀  一键 Docker Compose 部署
- 🧱🧱 模块化代码结构，便于二次开发 



    
---

## 🧱 项目结构

LYT2/
├── apps/ # 前后端服务
│ ├── api/ # FastAPI 后端服务
│ └── web/ # React 前端页面
├── packages/ # 核心功能模块
│ ├── core/ # 任务调度器 / 执行器 / 规划器
│ ├── agents/ #  股票、报表 Agent
│ ├── tools/ # 插件系统（内置插件）
│ └── lang/ # 多语言支持
├── scripts/ # 启动 / 部署脚本
├── static/ # 静态资源（图表 / 报告 / LOGO）
├── docs/ # 使用说明 / API文档 / 插件指南
├── .env.example # 环境变量模板
├── docker-compose.yml # Docker 部署配置
└── README.md # 本文件



---

## ⚙️ 快速启动

1. 安装依赖

> Python 版本推荐 ≥ 3.9  
> Node.js 版本推荐 ≥ 18.0

```bash
# 后端依赖
cd apps/api
pip install -r ../../requirements.txt

# 前端依赖
cd ../web
npm install


2. 本地开发启动

# 启动后端
cd apps/api
uvicorn main:app --reload --port 8000

# 启动前端
cd ../web
npm run dev
   
   
3. Docker 部署

执行check_env.sh 脚本检查基础环境，确保基础环境都已安装；

cp .env.example .env
./scripts/deploy_docker.sh


访问地址：

前端：http://localhost:5173

后端：http://localhost:8000/api

账户说明
默认用户无需注册，直接从后端接口创建测试Token

登录成功后即可访问分析股票、管理插件功能

示例任务链
📈 股票分析链
输入股票代码 ➜ 获取行情 ➜ 图表生成 ➜ LLM总结 ➜ 生成HTML报告

🧩 插件扩展
你可以上传 .zip 包形式的插件，其中应包含：
plugin.zip
├── tool.py               # 插件执行代码（继承 ToolBase）
└── metadata.json         # 插件元信息（name、description 等）
详见：docs/PLUGIN_GUIDE.md


默认登录：

用户名：admin
 
密码：123456 



📖 文档合集
文档文件	说明
README.md	项目总览说明
DEPLOY.md	部署指南
PLUGIN_GUIDE.md	插件开发说明
API_REFERENCE.md	后端API接口说明（路径/参数/示例）

研发团队:
主研发：北京市密网信息科技有限公司（项目规划 + 交付控制）

技术支持：北京市密网信息科技有限公司（全栈代码开发 + 模块封装）


特此声明：

本项目遵循 自定义 MIT 协议 + 禁止商业化条款。

您可以自由学习、研究、使用、修改和传播本项目，但禁止以任何形式将其用于商业目的，包括但不限于：

将本项目代码直接用于收费产品或服务；

将项目整体或修改版本进行销售、二次授权；

使用该项目部署 SaaS 服务后对外收费；

如需商业使用，请联系作者北京市密网信息科技有限公司（可在 Issues 留言或发送邮件mtl15739501059@163.com）。





