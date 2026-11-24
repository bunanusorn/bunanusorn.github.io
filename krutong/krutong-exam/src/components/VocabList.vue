<script setup>
import { ref, computed } from 'vue'
import { DATA } from '../vocabData.js'

const q = ref('')

const groups = computed(() => {
  const t = q.value.trim().toLowerCase()
  return DATA.map((g, i) => ({
    id: 'g' + i,
    title: g.title,
    topics: g.topics,
    words: g.words
      .map(([word, meaning, th, ex]) => ({ word, meaning, th, ex }))
      .filter(w => !t || `${w.word} ${w.meaning} ${w.th} ${w.ex}`.toLowerCase().includes(t))
  })).filter(g => g.words.length)
})
</script>

<template>
  <div class="vocab">
    <header class="vocab-head">
      <h1>📚 Vocabulary Booklet</h1>
      <p>คำศัพท์ตามหัวข้อ 1–81 พร้อมความหมายและประโยคตัวอย่าง</p>
    </header>

    <div class="tools">
      <input v-model="q" type="search" placeholder="🔍 ค้นหาคำศัพท์ ความหมาย หรือภาษาไทย..." />
      <div class="nav">
        <a v-for="g in groups" :key="g.id" :href="'#' + g.id">{{ g.title }}</a>
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
.vocab { --accent:#3b5bdb; --soft:#e8edff; --line:#e5e7eb; --muted:#6b7280; max-width:900px; margin:0 auto; padding:16px; line-height:1.6; color:#1f2430; text-align:left; }
.vocab-head { background:var(--accent); color:#fff; padding:24px 20px; text-align:center; border-radius:14px; }
.vocab-head h1 { margin:0 0 6px; font-size:1.6rem; }
.vocab-head p { margin:0; opacity:.9; }
.tools { position:sticky; top:0; z-index:10; background:#f6f7fb; padding:12px 0; }
.tools input { width:100%; padding:12px 16px; font-size:1rem; border:2px solid var(--line); border-radius:12px; outline:none; box-sizing:border-box; }
.tools input:focus { border-color:var(--accent); }
.nav { display:flex; flex-wrap:wrap; gap:8px; margin-top:10px; }
.nav a { text-decoration:none; background:var(--soft); color:var(--accent); padding:5px 12px; border-radius:999px; font-size:.85rem; font-weight:600; }
section { margin-top:28px; }
h2 { font-size:1.25rem; margin:0 0 4px; padding-left:10px; border-left:5px solid var(--accent); }
.topics { color:var(--muted); font-size:.85rem; margin:0 0 12px 15px; }
.card { background:#fff; border:1px solid var(--line); border-radius:14px; padding:14px 16px; margin-bottom:10px; }
.top { display:flex; flex-wrap:wrap; align-items:baseline; gap:8px 12px; }
.word { font-size:1.2rem; font-weight:700; color:var(--accent); }
.mean { font-weight:600; }
.th { color:#b45309; font-size:.92rem; }
.ex { margin-top:6px; padding:8px 12px; background:#f9fafb; border-left:3px solid #cbd5e1; border-radius:6px; font-style:italic; color:#374151; }
.empty { text-align:center; color:var(--muted); padding:30px; }
</style>
