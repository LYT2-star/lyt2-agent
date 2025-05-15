# apps/web/Dockerfile

# 构建阶段
FROM node:18-alpine as build

WORKDIR /app
COPY . .
RUN npm install && npm run build

# 部署阶段
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

