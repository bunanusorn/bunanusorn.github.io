import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/bunanusorn.github.com/', // เช่น '/my-vue-app/'
  plugins: [vue()],
})