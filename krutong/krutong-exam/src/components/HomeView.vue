<script setup>
import { computed } from 'vue'
import { CATEGORIES, categoryOf } from '../categories.js'
import { DATA } from '../vocabData.js'

const props = defineProps({ sets: Array, qCount: Function })
defineEmits(['open-cat', 'open-vocab'])

const cats = computed(() =>
  CATEGORIES.map((c) => {
    const list = props.sets.filter((s) => categoryOf(s) === c.id)
    return { ...c, n: list.length, q: list.reduce((a, s) => a + props.qCount(s), 0) }
  }).filter((c) => c.n > 0)
)
const totalQ = computed(() => props.sets.reduce((a, s) => a + props.qCount(s), 0))
const vocabCount = DATA.reduce((a, g) => a + g.words.length, 0)
</script>

<template>
  <div>
    <h1>คลังข้อสอบ Reading &amp; Listening</h1>
    <p class="meta">{{ sets.length }} ชุด · {{ totalQ }} ข้อ · บทความ โจทย์ เฉลย และคำแปลไทย</p>

    <h2 class="sec">เลือกหมวดหมู่</h2>
    <div class="grid">
      <button v-for="c in cats" :key="c.id" class="cat" @click="$emit('open-cat', c.id)">
        <span class="ico">{{ c.icon }}</span>
        <span class="name">{{ c.name }}</span>
        <span class="meta">{{ c.n }} ชุด · {{ c.q }} ข้อ</span>
      </button>
    </div>

    <h2 class="sec">เครื่องมือช่วยเรียน</h2>
    <div class="grid">
      <button class="cat vocab" @click="$emit('open-vocab')">
        <span class="ico">📚</span>
        <span class="name">คำศัพท์พร้อมประโยคตัวอย่าง</span>
        <span class="meta">{{ vocabCount }} คำ · ค้นหาได้</span>
      </button>
    </div>
  </div>
</template>

<style scoped>
h1 { font-family: Georgia, serif; font-size: 1.55rem; margin: 0.1em 0; }
.sec { font-size: 1rem; margin: 22px 0 10px; color: var(--mute); font-weight: 600; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 12px; }
.cat {
  display: flex; flex-direction: column; align-items: flex-start; gap: 4px;
  text-align: left; padding: 16px; border-radius: 14px;
  background: var(--card); border: 1px solid var(--line);
  transition: transform 0.12s, border-color 0.12s;
}
.cat:hover { transform: translateY(-2px); border-color: var(--acc); }
.ico { font-size: 1.8rem; line-height: 1; }
.name { font-weight: 700; font-size: 1.02rem; }
.vocab { border-style: dashed; }
</style>
