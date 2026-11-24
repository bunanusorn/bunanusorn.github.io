<script setup>
import { computed } from 'vue'
const props = defineProps({ item: Object, showTh: Boolean })
const isAnswer = computed(() =>
  /^(✅|❌|Answer|Correct Answer|เฉลย|ตอบ|คําตอบ|คำตอบ|เหตุผล|Explanation)/i.test(props.item.t)
)
</script>

<template>
  <h3 v-if="item.k === 'h'" :class="{ ans: isAnswer }">{{ item.t }}</h3>
  <p v-else-if="item.l === 'en'" class="en" :class="{ ans: isAnswer }">{{ item.t }}</p>
  <p v-else-if="showTh" class="th" :class="{ ans: isAnswer }">{{ item.t }}</p>
</template>

<style scoped>
h3 { font-family: Georgia, serif; margin: 18px 0 6px; font-size: 1.05rem; color: var(--acc); }
p { margin: 0 0 10px; white-space: pre-wrap; }
.th { padding: 8px 12px; background: var(--thbg); color: var(--th); border-radius: 10px; font-size: 0.95rem; }
.ans { border-left: 4px solid var(--ok); background: var(--okbg); padding: 6px 10px; border-radius: 6px; }
</style>
