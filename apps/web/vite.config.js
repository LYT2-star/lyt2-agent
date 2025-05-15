import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: resolve(__dirname, 'index.html')  // ✅ 指定构建入口
    },
    outDir: 'dist'
  },
  server: {
    port: 5173
  }
})

