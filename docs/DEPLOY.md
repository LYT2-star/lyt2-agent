DEPLOY.md —— 部署指南
本地开发部署（推荐调试阶段）
# 进入后端目录并安装依赖
cd apps/api
pip install -r ../../requirements.txt
uvicorn main:app --reload --port 8000

# 另起终端窗口，启动前端
cd ../web
npm install
npm run dev
访问：

后端：http://localhost:8000/api

前端：http://localhost:5173

Docker 一键部署（推荐生产环境）

cp .env.example .env
chmod +x scripts/deploy_docker.sh
./scripts/deploy_docker.sh

容器启动后访问：

http://localhost:5173
