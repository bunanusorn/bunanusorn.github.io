<script setup>
import { units, course } from '../data/units.js'
const ready = Object.keys(import.meta.glob('../content/unit*.js')).map(p => p.match(/unit\d+/)[0])
</script>
<template>
  <h1>หน่วยการเรียนรู้</h1>
  <p>รหัสวิชา {{ course.code }} · {{ course.name }} · ทฤษฎี 1 ปฏิบัติ 4 · {{ course.credit }} หน่วยกิต</p>
  <div class="grid">
    <RouterLink v-for="u in units" :key="u.id" :to="'/' + u.id" class="card">
      <b>หน่วยที่ {{ u.n }}</b><span>{{ u.t }}</span>
      <small>ทฤษฎี {{ u.th }} · ปฏิบัติ {{ u.pr }} ชม. · {{ ready.includes(u.id) ? 'พร้อมเรียน + แบบทดสอบ' : 'กำลังจัดทำ' }}</small>
    </RouterLink>
  </div>
</template>
