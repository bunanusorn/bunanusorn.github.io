<script setup>
import { course } from './data/units.js'
const logo = import.meta.env.BASE_URL + 'logo.png'
</script>
<template>
  <header class="noprint">
    <img :src="logo" alt="ตราวิทยาลัย" />
    <div><p>{{ course.college }}</p>
      <RouterLink to="/" class="ttl">{{ course.code }} {{ course.name }}</RouterLink>
      <small>ครูผู้สอน: {{ course.teacher }}</small></div>
  </header>
  <main><RouterView /></main>
  <footer class="noprint">จัดทำโดย {{ course.teacher }} · {{ course.college }}</footer>
</template>
