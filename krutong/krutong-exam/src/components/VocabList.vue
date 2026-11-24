<script setup>
import { ref, computed } from 'vue'
import { DATA } from '../vocabData.js'

const q = ref('')

const groups = computed(() => {
  const t = q.value.trim().toLowerCase()
  return DATA.map((g, i) => ({
    id: 'vg' + i,
    title: g.title,
    topics: g.topics,
    words: g.words
      .map(([word, meaning, th, ex]) => ({ word, meaning, th, ex }))
      .filter((w) => !t || `${w.word} ${w.meaning} ${w.th} ${w.ex}`.toLowerCase().includes(t)),
  })).filter((g) => g.words.length)
})

// ใช้ scrollIntoView แทนลิงก์ #anchor เพื่อไม่ให้ชนกับ router แบบ hash ของแอป
function jump(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
</script>

<template>
  <div>
    <h1>📚 คำศัพท์พร้อมประโยคตัวอย่าง</h1>
    <p class="meta">คำศัพท์ตามหัวข้อ 1–81 พร้อมความหมายและประโยคตัวอย่าง</p>

    <div class="tools">
      <input v-model="q" type="search" placeholder="🔍 ค้นหาคำศัพท์ ความหมาย หรือภาษาไทย..." />
      <div class="nav row">
        <button v-for="g in groups" :key="g.id" @click="jump(g.id)">{{ g.title }}</button>
      </div>
    </div>

    <section v-for="g in groups" :id="g.id" :key="g.id">
      <h2>{{ g.title }}</h2>
      <p class="topics">{{ g.topics }}</p>
      <div v-for="w in g.words" :key="w.word" class="card">
        <div class="top">
          <span class="word">{{ w.word }}</span>
          <span class="mean">= {{ w.meaning }}</span>
          <span v-if="w.th" class="th">({{ w.th }})</span>
        </div>
        <div class="ex">“{{ w.ex }}”</div>
      </div>
    </section>

    <p v-if="!groups.length" class="empty">ไม่พบคำที่ค้นหา</p>
  </div>
</template>

<style scoped>
h1 { font-family: Georgia, serif; font-size: 1.45rem; margin: 0.1em 0; }
.tools { position: sticky; top: 0; z-index: 5; background: var(--bg); padding: 10px 0; }
.tools input {
  width: 100%; padding: 12px 16px; font: inherit; border: 2px solid var(--line); border-radius: 12px;
  outline: none; background: var(--card); color: var(--ink);
}
.tools input:focus { border-color: var(--acc); }
.nav { margin-top: 10px; }
.nav button { padding: 4px 12px; font-size: 0.85rem; color: var(--acc); font-weight: 600; border-radius: 999px; }
section { margin-top: 24px; scroll-margin-top: 130px; }
section h2 { font-family: Georgia, serif; font-size: 1.2rem; margin: 0 0 4px; padding-left: 10px; border-left: 5px solid var(--acc); }
.topics { color: var(--mute); font-size: 0.85rem; margin: 0 0 12px 15px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 14px; padding: 12px 16px; margin-bottom: 10px; }
.top { display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 12px; }
.word { font-size: 1.15rem; font-weight: 700; color: var(--acc); }
.mean { font-weight: 600; }
.th { color: var(--th); font-size: 0.92rem; }
.ex { margin-top: 6px; padding: 8px 12px; background: var(--bg); border-left: 3px solid var(--line); border-radius: 6px; font-style: italic; }
.empty { text-align: center; color: var(--mute); padding: 30px; }
</style>
