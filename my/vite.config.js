import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [vue(), tailwindcss()],
  base: '/my/', // เปลี่ยนเป็น '/' หากให้แสดงที่หน้าหลัก bunanusorn.github.io
})