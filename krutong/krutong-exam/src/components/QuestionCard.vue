<script setup>
const props = defineProps({ q: Object, memorize: Boolean, showTh: Boolean, picked: String })
const emit = defineEmits(['pick'])

function cls(letter) {
  if (props.memorize) return letter === props.q.a ? 'ok' : ''
  if (!props.picked) return ''
  if (letter === props.q.a) return 'ok'
  return letter === props.picked ? 'no' : ''
}
</script>

<template>
  <div class="q">
    <div class="meta">ข้อ {{ q.n || '' }}</div>
    <div class="qt">{{ q.q }}</div>
    <div v-if="showTh && q.tq" class="th">{{ q.tq }}</div>

    <button
      v-for="(text, letter) in q.o"
      :key="letter"
      class="opt"
      :class="cls(letter)"
      :disabled="memorize"
      @click="emit('pick', letter)"
    >
      <b>{{ letter }}</b>
      <span>
        {{ text }}
        <span v-if="showTh && q.to" class="th-opt">{{ q.to[letter] }}</span>
      </span>
    </button>

    <div class="st" v-if="memorize">
      <span v-if="q.a" class="good">✓ เฉลย {{ q.a }}. {{ q.o[q.a] }}</span>
      <span v-else class="meta">ไม่มีเฉลยของข้อนี้ในไฟล์ต้นฉบับ</span>
    </div>
    <div class="st" v-else-if="picked">
      <span v-if="!q.a" class="meta">ไม่พบเฉลยของข้อนี้ในไฟล์ต้นฉบับ</span>
      <span v-else :style="{ color: picked === q.a ? 'var(--ok)' : 'var(--no)' }">
        {{ picked === q.a ? '✓ ถูกต้อง' : '✗ เฉลยคือ ' + q.a + '. ' + q.o[q.a] }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.q { border: 1px solid var(--line); border-radius: 12px; padding: 14px; margin: 14px 0; background: var(--card); }
.qt { font-weight: 600; margin: 4px 0 10px; }
.th { margin: 0 0 10px; padding: 6px 10px; background: var(--thbg); color: var(--th); border-radius: 8px; }
.th-opt { display: block; color: var(--th); font-size: 0.9rem; }
.opt { display: flex; gap: 10px; width: 100%; text-align: left; margin-bottom: 7px; padding: 10px 12px; align-items: flex-start; }
.opt b { min-width: 1.3em; color: var(--acc); }
.opt:disabled { opacity: 1; color: var(--ink); cursor: default; }
.opt.ok { background: var(--okbg); border-color: var(--ok); }
.opt.no { background: var(--nobg); border-color: var(--no); }
.st { font-size: 0.9rem; margin-top: 6px; }
.good { color: var(--ok); font-weight: 700; }
</style>
