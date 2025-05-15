#!/bin/bash
# scripts/deploy_docker.sh

echo "🐳 正在构建 Docker 镜像..."
docker-compose build

echo "🚀 启动容器服务..."
docker-compose up -d

echo "✅ 部署完成："
echo "- 后端接口：http://localhost:8000/api"
echo "- 前端页面：http://localhost:5173"

