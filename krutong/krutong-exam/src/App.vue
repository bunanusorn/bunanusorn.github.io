<script setup>
import { ref, computed, watch } from 'vue'
import sets from './data/sets.json'
import SetPicker from './components/SetPicker.vue'
import QuestionCard from './components/QuestionCard.vue'
import ContentBlock from './components/ContentBlock.vue'

const filter = ref('ทั้งหมด')
const current = ref(sets[0].id)
const showTh = ref(true)
const memorize = ref(true)
const view = ref('all') // 'all' | 'q'
const picks = ref({})

const qCount = (s) => s.items.filter((x) => x.k === 'q').length
const totalQ = sets.reduce((a, s) => a + qCount(s), 0)
const set = computed(() => sets.find((s) => s.id === current.value))
const list = computed(() => sets.filter((s) => filter.value === 'ทั้งหมด' || s.type === filter.value))
const answered = computed(() => Object.keys(picks.value).length)
const score = computed(
  () => set.value.items.filter((it, i) => it.k === 'q' && picks.value[i] && picks.value[i] === it.a).length
)

watch(filter, () => {
  if (!list.value.find((s) => s.id === current.value) && list.value.length) current.value = list.value[0].id
})
watch(current, () => {
  picks.value = {}
  window.scrollTo(0, 0)
})

function pick(i, letter) {
  if (!picks.value[i]) picks.value = { ...picks.value, [i]: letter }
}
function toggleMemorize() {
  memorize.value = !memorize.value
  picks.value = {}
}
function toggleTheme() {
  const r = document.documentElement
  const dark = matchMedia('(prefers-color-scheme: dark)').matches
  const now = r.dataset.theme || (dark ? 'dark' : 'light')
  r.dataset.theme = now === 'dark' ? 'light' : 'dark'
}
</script>

<template>
  <div class="wrap">
    <div class="row" style="justify-content: space-between">
      <h1>คลังข้อสอบ Reading &amp; Listening</h1>
      <button @click="toggleTheme">◐ ธีม</button>
    </div>
    <p class="meta">{{ sets.length }} ชุด · {{ totalQ }} ข้อ · บทความ โจทย์ เฉลย และคำแปลไทย</p>

    <SetPicker v-model:filter="filter" v-model:current="current" :list="list" :count="qCount" />

    <template v-if="set">
      <div class="toolbar row">
        <div class="row">
          <button :class="{ on: showTh }" @click="showTh = !showTh">คำแปลไทย {{ showTh ? 'เปิด' : 'ปิด' }}</button>
          <button :class="{ on: memorize }" @click="toggleMemorize">โหมดท่องจำ {{ memorize ? 'เปิด' : 'ปิด' }}</button>
          <button :class="{ on: view === 'all' }" @click="view = 'all'">ทั้งชุด</button>
          <button :class="{ on: view === 'q' }" @click="view = 'q'">เฉพาะโจทย์</button>
        </div>
        <span class="meta" v-if="!memorize">
          ตอบถูก {{ score }} / {{ answered }} (ทั้งหมด {{ qCount(set) }})
          <button @click="picks = {}">รีเซ็ต</button>
        </span>
        <span class="meta" v-else>{{ qCount(set) }} ข้อ</span>
      </div>

      <h2>{{ set.title }}</h2>
      <div class="meta">หน้า {{ set.page }} ของไฟล์ต้นฉบับ</div>

      <template v-for="(it, ix) in set.items" :key="set.id + '-' + ix">
        <QuestionCard
          v-if="it.k === 'q'"
          :q="it"
          :memorize="memorize"
          :show-th="showTh"
          :picked="picks[ix]"
          @pick="(l) => pick(ix, l)"
        />
        <ContentBlock v-else-if="view === 'all'" :item="it" :show-th="showTh" />
      </template>
    </template>
  </div>
</template>

<style scoped>
h1 { font-family: Georgia, serif; font-size: 1.55rem; margin: 0.1em 0; }
h2 { font-family: Georgia, serif; margin: 0 0 4px; }
.toolbar {
  position: sticky; top: 0; z-index: 5; justify-content: space-between;
  background: var(--bg); padding: 8px 0; border-bottom: 1px solid var(--line); margin-bottom: 12px;
}
</style>
