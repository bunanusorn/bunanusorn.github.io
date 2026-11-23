import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// base = ชื่อโฟลเดอร์บน github.io (ถ้าเปลี่ยนชื่อโฟลเดอร์ ให้แก้ที่นี่ที่เดียว)
export default defineConfig({ base: '/20190-1005/', plugins: [vue()] })
