// postcss.config.js ✅
const tailwindcss = require('@tailwindcss/postcss'); // ⬅️ 新插件包
const autoprefixer = require('autoprefixer');

module.exports = {
  plugins: [
    tailwindcss(),  // ✅ 确保是函数调用
    autoprefixer()
  ]
}

