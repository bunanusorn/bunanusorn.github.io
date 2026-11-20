<script setup>
import { ref } from 'vue'
import LedControlPage from './LedControlPage.vue'
import AboutPage from './AboutPage.vue'

// 'control' = หน้าควบคุม LED, 'about' = หน้าแนะนำตัว & Infographic
const currentPage = ref('about') // ตั้งค่าเริ่มต้นให้เปิดมาเจอหน้าแนะนำตัว & Infographic ก่อน
</script>

<template>
  <main class="container">
    <nav class="nav-bar">
      <button
        :class="['nav-btn', { active: currentPage === 'about' }]"
        @click="currentPage = 'about'"
      >
        แนะนำตัว & Infographic
      </button>
      <button
        :class="['nav-btn', { active: currentPage === 'control' }]"
        @click="currentPage = 'control'"
      >
        ควบคุม LED (D4)
      </button>
    </nav>

    <AboutPage v-if="currentPage === 'about'" />
    <LedControlPage v-else />
  </main>
</template>

<style scoped>
.container {
  max-width: 560px;
  margin: 2rem auto;
  padding: 0 1rem;
  font-family: system-ui, sans-serif;
}
.nav-bar {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.nav-btn {
  flex: 1;
  padding: 0.65rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #f3f4f6;
  color: #374151;
  font-weight: 600;
  cursor: pointer;
}
.nav-btn.active {
  background: #7f1d1d;
  color: #fef08a;
  border-color: #7f1d1d;
}
</style>