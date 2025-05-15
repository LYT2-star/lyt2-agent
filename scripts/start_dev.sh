#!/bin/bash
# scripts/start_dev.sh

echo "🐍 启动后端 FastAPI 开发环境..."
cd apps/api
uvicorn main:app --reload --host 0.0.0.0 --port 8000

