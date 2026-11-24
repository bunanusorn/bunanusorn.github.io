<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue'
import sets from './data/sets.json'
import QuestionCard from './components/QuestionCard.vue'
import ContentBlock from './components/ContentBlock.vue'
import VocabList from './components/VocabList.vue'
import HomeView from './components/HomeView.vue'
import CategoryView from './components/CategoryView.vue'
import { categoryOf, getCategory, cleanTitle } from './categories.js'

// ---------- router แบบ hash (รองรับปุ่ม Back ของเบราว์เซอร์) ----------
// #/            หน้าหลัก (หมวดหมู่)
// #/cat/<id>    รายการชุดในหมวด
// #/set/<id>    หน้าทำข้อสอบ
// #/vocab       หน้าคำศัพท์
function parseHash() {
  const [name = '', arg = ''] = location.hash.replace(/^#\/?/, '').split('/')
  if (name === 'cat' && getCategory(arg)) return { name: 'cat', id: arg }
  if (name === 'set' && sets.some((s) => s.id === Number(arg))) return { name: 'set', id: Number(arg) }
  if (name === 'vocab') return { name: 'vocab' }
  return { name: 'home' }
}
const route = ref(parseHash())
const onHash = () => {
  route.value = parseHash()
  window.scrollTo(0, 0)
}
onMounted(() => window.addEventListener('hashchange', onHash))
onUnmounted(() => window.removeEventListener('hashchange', onHash))
const go = (path = '') => {
  location.hash = '/' + path
}

// ---------- ข้อมูล ----------
const showTh = ref(true)
const memorize = ref(true)
const view = ref('all') // 'all' | 'q'
const picks = ref({})

const qCount = (s) => s.items.filter((x) => x.k === 'q').length
const set = computed(() => (route.value.name === 'set' ? sets.find((s) => s.id === route.value.id) : null))
const category = computed(() => {
  if (route.value.name === 'cat') return getCategory(route.value.id)
  if (set.value) return getCategory(categoryOf(set.value))
  return null
})
const catSets = computed(() => (category.value ? sets.filter((s) => categoryOf(s) === category.value.id) : []))
const idx = computed(() => (set.value ? catSets.value.findIndex((s) => s.id === set.value.id) : -1))
const prevSet = computed(() => (idx.value > 0 ? catSets.value[idx.value - 1] : null))
const nextSet = computed(() => (idx.value >= 0 ? catSets.value[idx.value + 1] || null : null))

const answered = computed(() => Object.keys(picks.value).length)
const score = computed(() =>
  set.value ? set.value.items.filter((it, i) => it.k === 'q' && picks.value[i] && picks.value[i] === it.a).length : 0
)

watch(set, () => {
  picks.value = {}
})

const backLabel = computed(() => {
  if (route.value.name === 'set') return category.value.name
  return 'หน้าหลัก'
})
function goBack() {
  if (route.value.name === 'set') go('cat/' + category.value.id)
  else go()
}

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
    <div class="row topbar">
      <button v-if="route.name !== 'home'" @click="goBack">← {{ backLabel }}</button>
      <span class="grow"></span>
      <button v-if="route.name !== 'vocab'" @click="go('vocab')">📚 คำศัพท์</button>
      <button @click="toggleTheme">◐ ธีม</button>
    </div>

    <HomeView
      v-if="route.name === 'home'"
      :sets="sets"
      :q-count="qCount"
      @open-cat="(id) => go('cat/' + id)"
      @open-vocab="go('vocab')"
    />

    <CategoryView
      v-else-if="route.name === 'cat'"
      :category="category"
      :list="catSets"
      :count="qCount"
      @open-set="(id) => go('set/' + id)"
    />

    <VocabList v-else-if="route.name === 'vocab'" />

    <template v-else-if="set">
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

      <h2>{{ cleanTitle(set.title) }}</h2>
      <div class="meta">{{ category.icon }} {{ category.name }} · หน้า {{ set.page }} ของไฟล์ต้นฉบับ</div>

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

      <div class="row pager">
        <button :disabled="!prevSet" @click="go('set/' + prevSet.id)">← ชุดก่อนหน้า</button>
        <span class="grow"></span>
        <button :disabled="!nextSet" @click="go('set/' + nextSet.id)">ชุดถัดไป →</button>
      </div>
    </template>
  </div>
</template>

<style scoped>
h2 { font-family: Georgia, serif; margin: 0 0 4px; }
.topbar { margin-bottom: 14px; }
.grow { flex: 1; }
.toolbar {
  position: sticky; top: 0; z-index: 5; justify-content: space-between;
  background: var(--bg); padding: 8px 0; border-bottom: 1px solid var(--line); margin-bottom: 12px;
}
.pager { margin-top: 24px; }
button:disabled { opacity: 0.4; cursor: default; }
</style>
