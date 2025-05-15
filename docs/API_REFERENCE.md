用户登录

POST /api/user/login
Body: { username, password }
Response: { access_token, token_type }

提交简历任务
POST /api/task/resume
Form: file(PDF), job_type
Header: Authorization: Bearer <token>
Response: { parsed, score, report_url }

提交股票任务

POST /api/task/stock
Form: symbol
Header: Authorization
Response: { charts, summary, report_url }

插件上传
POST /api/plugin/upload
Form: file(zip)
Header: Authorization
Response: { message }

插件列表
GET /api/plugin/list
Response: [ { name, description, enabled } ]

插件启用/禁用
POST /api/plugin/enable/{name}   或  /disable/{name}

