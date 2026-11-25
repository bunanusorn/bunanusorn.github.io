<script setup>
import { ref, computed, reactive } from 'vue'
const props = defineProps({ item: Object, all: Array })
const emit = defineEmits(['back', 'open'])
const showTh = ref(true)
const picked = reactive({}), shown = reactive({})
const TH = /[\u0E00-\u0E7F]/
const paras = computed(() => {
  const out = []; let cur = null
  for (const l of (props.item.body || '').split('\n')) {
    const s = l.trim()
    if (!s) { cur = null; continue }
    const th = TH.test(s)
    if (cur && cur.th === th) cur.t += ' ' + s
    else { cur = { th, t: s }; out.push(cur) }
  }
  return out
})
const qs = computed(() => props.item.qs || [])
const score = computed(() => {
  const m = qs.value.map((q, i) => ({ q, i })).filter(x => x.q.kind === 'mcq')
  return { total: m.length, done: m.filter(x => picked[x.i]).length, right: m.filter(x => picked[x.i] === x.q.ans).length }
})
const clean = s => (s || '').replace(/\n+/g, ' ')
const dupsOf = computed(() => props.all.filter(r => r.dup === props.item.n))
</script>
<template>
  <button class="back" @click="emit('back')">← กลับ</button>
  <h1>#{{ item.n }} {{ item.title }}</h1>
  <p class="sub"><span class="badge" :class="item.type==='Reading'?'r':'l'">{{ item.type }}</span> ไฟล์วันที่ {{ item.date }}
    <span v-if="dupsOf.length" class="note"> · ซ้ำกับ {{ dupsOf.map(d => '#' + d.n).join(', ') }}</span></p>
  <p v-if="item.status==='pending' && !item.body" class="card">รายการนี้อยู่ในสารบัญของไฟล์ต้นฉบับ แต่ไม่มีเนื้อหา/คำถามในไฟล์ (สถานะ "รอแปล")</p>
  <template v-else>
    <label class="note"><input type="checkbox" v-model="showTh" /> แสดงคำแปลไทย</label>
    <div class="card" :class="{'hide-th': !showTh}">
      <template v-for="(p, i) in paras" :key="i">
        <p :class="p.th ? 'p-th' : 'p-en'">{{ p.t }}</p>
      </template>
    </div>
    <h2>แบบฝึกหัด
      <span class="badge" v-if="score.total">ตอบแล้ว {{ score.done }}/{{ score.total }} · ถูก {{ score.right }}</span></h2>
    <div v-if="!qs.length">
      <p class="note">ไม่สามารถแยกเป็นข้อสอบได้ — แสดงข้อความต้นฉบับ</p>
      <pre class="raw" v-if="item.qa_raw">{{ item.qa_raw }}</pre>
    </div>
    <div class="card q" v-for="(q, i) in qs" :key="i">
      <template v-if="q.kind==='mcq'">
        <b class="qh">{{ clean(q.q) }}</b>
        <button v-for="o in q.opts" :key="o[0]" class="opt"
          :class="{ good: picked[i] && o[0]===q.ans, wrong: picked[i]===o[0] && o[0]!==q.ans }"
          @click="!picked[i] && (picked[i] = o[0])">{{ o[0] }}. {{ o[1] }}</button>
        <template v-if="picked[i]">
          <p :class="picked[i]===q.ans ? 'badge ok' : 'badge bad'">{{ picked[i]===q.ans ? 'ถูกต้อง' : 'เฉลย: ' + q.ans }}</p>
          <pre class="raw" v-if="showTh && q.th">{{ q.th }}</pre>
        </template>
      </template>
      <template v-else-if="q.kind==='open'">
        <b class="qh">{{ clean(q.q) }}</b>
        <button @click="shown[i] = !shown[i]">{{ shown[i] ? 'ซ่อนเฉลย' : 'ดูเฉลย' }}</button>
        <template v-if="shown[i]"><p><b>เฉลย:</b> {{ q.ans_text }}</p><pre class="raw" v-if="showTh && q.th">{{ q.th }}</pre></template>
      </template>
      <template v-else>
        <p class="note">ข้อนี้สร้างเป็นแบบฝึกหัดไม่ได้ — แสดงข้อความต้นฉบับ</p>
        <pre class="raw">{{ q.raw }}</pre>
      </template>
    </div>
  </template>
</template>
