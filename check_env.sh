#!/bin/bash
# LYT2 环境检查脚本 for Ubuntu 20.04
# 使用前：chmod +x check_env.sh

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

check() {
  if command -v $1 &> /dev/null; then
    echo -e "${GREEN}[✓] $2 已安装${NC}"
  else
    echo -e "${RED}[✗] $2 未安装，请执行：sudo apt install $3${NC}"
  fi
}

echo "\n🔍 正在检测羚羊T2部署基础环境..."

# 检查 Python
check python3 "Python 3" "python3"

# 检查 pip
check pip3 "pip3 (Python 包管理器)" "python3-pip"

# 检查 Node.js
check node "Node.js" "nodejs"

# 检查 npm
check npm "npm (Node 包管理器)" "npm"

# 检查 Docker
check docker "Docker" "docker.io"

# 检查 Docker Compose
check docker-compose "Docker Compose" "docker-compose"

# 检查 Redis
check redis-server "Redis 服务" "redis-server"

