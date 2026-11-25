<script setup>
import { computed } from 'vue'
const props = defineProps({ list: Array, lib: Array })
defineEmits(['open'])
const L = n => props.lib.find(r => r.n === n)
const st = c => {
  if (!c.ids.length) return c.approx.length ? 'approx' : 'missing'
  return c.ids.every(i => L(i)?.status === 'pending') ? 'pending' : 'found'
}
const sections = computed(() => ['Reading', 'Listening'].map(s => ({ s, rows: props.list.filter(c => c.sec === s) })))
const count = (rows, k) => rows.filter(c => st(c) === k).length
const T = { found: ['พบในไฟล์', 'ok'], pending: ['มีในสารบัญ แต่ไม่มีเนื้อหา', 'warn'], approx: ['ไม่พบชื่อตรง (มีเรื่องใกล้เคียง)', 'warn'], missing: ['ไม่พบในไฟล์', 'bad'] }
</script>
<template>
  <p class="note">เทียบรายการในไฟล์ "รีวิวแนวข้อสอบ CEFR รอบ 31 ต.ค. 2569" (Reading 81 เรื่อง / Listening 12 เรื่อง) กับไฟล์ Reading_Listening_สรุปแปลไทย</p>
  <section v-for="g in sections" :key="g.s">
    <h2>{{ g.s }} ({{ g.rows.length }})</h2>
    <div class="sum">
      <span class="badge ok">พบ {{ count(g.rows,'found') }}</span>
      <span class="badge warn">ไม่มีเนื้อหา {{ count(g.rows,'pending') }}</span>
      <span class="badge warn">ใกล้เคียง {{ count(g.rows,'approx') }}</span>
      <span class="badge bad">ไม่พบ {{ count(g.rows,'missing') }}</span>
    </div>
    <div style="overflow-x:auto"><table>
      <tr><th>#</th><th>หัวข้อในรีวิว</th><th>สถานะ</th><th>เปิดดู</th></tr>
      <tr v-for="c in g.rows" :key="c.no">
        <td>{{ c.no }}</td>
        <td>{{ c.title }}<div class="note" v-if="c.batch">{{ c.batch }}</div></td>
        <td><span class="badge" :class="T[st(c)][1]">{{ T[st(c)][0] }}</span></td>
        <td><a class="lnk" v-for="i in (c.ids.length ? c.ids : c.approx)" :key="i" @click="$emit('open', i)">#{{ i }}</a></td>
      </tr>
    </table></div>
  </section>
</template>
