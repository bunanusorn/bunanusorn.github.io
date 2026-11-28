<script setup>
import { ref, computed } from 'vue'
import lib from './data/library.json'
import checklist from './data/checklist.json'
import Item from './Item.vue'
import Checklist from './Checklist.vue'
import Gate from './Gate.vue'
let saved = false
try { saved = localStorage.getItem('cefr_unlocked') === '1' } catch (e) {}
const unlocked = ref(saved)
const logout = () => { try { localStorage.removeItem('cefr_unlocked') } catch (e) {} unlocked.value = false }

const MONTHS = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
const tab = ref('lib'), q = ref(''), cur = ref(null), type = ref('All')

const playable = lib.filter(r => r.status !== 'dup')
const groups = computed(() => {
  const k = q.value.trim().toLowerCase()
  const by = {}
  for (const r of playable) {
    if (type.value !== 'All' && r.type !== type.value) continue
    if (k && !(`${r.n} ${r.title}`.toLowerCase().includes(k))) continue
    const key = (r.date || '').slice(0, 7) || 'ไม่ระบุ'
    ;(by[key] ||= []).push(r)
  }
  return Object.keys(by).sort().reverse().map(key => {
    const [y, m] = key.split('-')
    return { key, label: m ? `${MONTHS[+m - 1]} ${y}` : key, items: by[key] }
  })
})
const dups = lib.filter(r => r.status === 'dup')
const open = n => { cur.value = lib.find(r => r.n === n); window.scrollTo(0, 0) }
const label = t => t.replace(/^(?:\d+(?:[._]\d+)?_?\s*)?(?:TOEFL\s*|IELTS\s*|Review\s*)?(?:Reading|Listening)\s*[-_ ]*/i, '').replace(/_/g, ' ').trim() || t
</script>

<template>
  <Gate v-if="!unlocked" @ok="unlocked = true" />
  <div class="wrap" v-else>
    <Item v-if="cur" :item="cur" :all="lib" @back="cur = null" @open="open" />
    <template v-else>
      <h1>สื่อการสอน CEFR – Reading & Listening</h1>
      <p class="sub">เนื้อหา คำถาม และเฉลยทั้งหมดมาจากไฟล์ต้นฉบับเท่านั้น · จัดตามเดือนของไฟล์ ใหม่ → เก่า · ข้อที่สร้างเป็นแบบฝึกหัดไม่ได้จะแสดงข้อความดิบ</p>
      <div class="tabs">
        <button @click="logout" style="margin-left:auto;order:3">ออกจากระบบ</button>
        <button :class="{on: tab==='lib'}" @click="tab='lib'">คลังข้อสอบ ({{ playable.length }})</button>
        <button :class="{on: tab==='chk'}" @click="tab='chk'">ตรวจเทียบรีวิว 31 ต.ค. 2569</button>
      </div>
      <template v-if="tab==='lib'">
        <input type="search" v-model="q" placeholder="ค้นหาชื่อเรื่อง หรือเลขที่…" />
        <div class="tabs">
          <button v-for="t in ['All','Reading','Listening']" :key="t" :class="{on: type===t}" @click="type=t">{{ t === 'All' ? 'ทั้งหมด' : t }}</button>
        </div>
        <section v-for="g in groups" :key="g.key">
          <h2>{{ g.label }} <span class="badge">{{ g.items.length }} เรื่อง</span></h2>
          <div class="list">
            <button class="row" v-for="r in g.items" :key="r.n" @click="open(r.n)">
              <span class="num">#{{ r.n }}</span>
              <span class="t">{{ label(r.title) }}</span>
              <span class="badge" :class="r.type==='Reading'?'r':'l'">{{ r.type }}</span>
              <span class="badge ok" v-if="r.added">เพิ่มใหม่</span>
              <span class="badge warn" v-if="r.status==='pending'">ไม่มีเนื้อหาในไฟล์</span>
            </button>
          </div>
        </section>
        <section v-if="dups.length">
          <h2>รายการซ้ำ (ไฟล์ต้นฉบับไม่แปลซ้ำ)</h2>
          <p class="note">
            <span v-for="d in dups" :key="d.n">#{{ d.n }} → <a class="lnk" @click="open(d.dup)">#{{ d.dup }}</a></span>
          </p>
        </section>
      </template>
      <Checklist v-else :list="checklist" :lib="lib" @open="open" />
    </template>
  </div>
</template>
