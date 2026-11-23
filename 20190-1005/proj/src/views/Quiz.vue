<script setup>
import { ref, watchEffect, computed } from 'vue'
import { useRoute } from 'vue-router'
import { units, course } from '../data/units.js'
const mods = import.meta.glob('../content/unit*.js')
const r = useRoute(), c = ref(null), name = ref(''), ans = ref([]), done = ref(false), msg = ref('')
const u = computed(() => units.find(x => x.id === r.params.unit))
const logo = import.meta.env.BASE_URL + 'logo.png'
watchEffect(async () => {
  const f = mods[`../content/${r.params.unit}.js`]
  c.value = f ? (await f()).default : false
})
const norm = s => String(s ?? '').toLowerCase().replace(/[\s.\-]/g, '')
const ok = i => { const q = c.value.quiz.qs[i]; return q.o ? ans.value[i] === q.a : q.a.includes(norm(ans.value[i])) }
const n = computed(() => c.value.quiz.qs.length)
const score = computed(() => done.value ? c.value.quiz.qs.filter((_, i) => ok(i)).length : 0)
const pass = computed(() => done.value && score.value / n.value >= c.value.quiz.pass)
const today = () => new Date().toLocaleDateString('th-TH', { dateStyle: 'long' })
function submit() {
  if (!name.value) return (msg.value = 'กรุณากรอกชื่อ-นามสกุลก่อนส่งคำตอบ')
  if (ans.value.filter(a => a !== undefined && a !== '').length < n.value) return (msg.value = 'กรุณาตอบให้ครบทุกข้อ')
  msg.value = ''; done.value = true
}
const print = () => window.print()
const reset = () => { ans.value = []; done.value = false; scrollTo(0, 0) }
</script>
<template>
  <p v-if="c === false">ยังไม่มีแบบทดสอบสำหรับหน่วยนี้</p>
  <template v-else-if="c">
    <div class="noprint">
      <p><RouterLink :to="'/' + u.id">← กลับไปบทเรียน</RouterLink></p>
      <h1>แบบทดสอบ หน่วยที่ {{ u.n }}: {{ u.t }}</h1>
      <p class="warn">{{ n }} ข้อ (เลือกตอบและเติมคำ) ผ่านเมื่อถูกอย่างน้อย {{ Math.round(c.quiz.pass * 100) }}% จึงจะได้รับเกียรติบัตร คำตอบเติมคำพิมพ์เป็นภาษาอังกฤษตัวเล็กหรือใหญ่ก็ได้</p>
      <label>ชื่อ-นามสกุล <input v-model.trim="name" placeholder="เช่น นายสมชาย ใจดี" /></label>
      <ol class="qs">
        <li v-for="(q, i) in c.quiz.qs" :key="i">
          <p>{{ q.t }}</p>
          <template v-if="q.o">
            <label v-for="(o, j) in q.o" :key="j" class="opt"><input type="radio" :name="'q' + i" :value="j" v-model="ans[i]" :disabled="done" /> {{ o }}</label>
          </template>
          <input v-else v-model="ans[i]" :disabled="done" placeholder="พิมพ์คำตอบ" />
          <p v-if="done" :class="ok(i) ? 'ok' : 'no'">{{ ok(i) ? '✓ ถูกต้อง' : '✗ ไม่ถูกต้อง' }} — {{ q.e }}</p>
        </li>
      </ol>
      <button @click="submit" :disabled="done">ส่งคำตอบ</button>
      <button v-if="done" class="alt" @click="reset">ทำใหม่</button>
      <button v-if="pass" class="alt" @click="print()">พิมพ์เกียรติบัตร</button>
      <p v-if="msg" class="no">{{ msg }}</p>
      <p v-if="done" class="score">ได้ {{ score }} / {{ n }} ข้อ {{ pass ? '· ผ่าน ได้รับเกียรติบัตร' : '· ยังไม่ผ่าน ลองทบทวนบทเรียนแล้วทำใหม่' }}</p>
    </div>
    <section v-if="pass" id="cert">
      <img :src="logo" alt="" />
      <p>{{ course.college }}</p>
      <h2>เกียรติบัตร</h2>
      <p>ขอมอบเกียรติบัตรฉบับนี้ให้ไว้เพื่อแสดงว่า</p>
      <div class="nm">{{ name }}</div>
      <p>ผ่านแบบทดสอบ หน่วยที่ {{ u.n }} {{ u.t }}<br />วิชา {{ course.code }} {{ course.name }}<br />คะแนน {{ score }} / {{ n }} ข้อ</p>
      <p>ให้ไว้ ณ วันที่ {{ today() }}</p>
      <p class="sg">({{ course.teacher }})<br />ครูผู้สอน</p>
    </section>
  </template>
</template>
