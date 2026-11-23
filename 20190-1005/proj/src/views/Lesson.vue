<script setup>
import { ref, watchEffect, computed } from 'vue'
import { useRoute } from 'vue-router'
import { units } from '../data/units.js'
const mods = import.meta.glob('../content/unit*.js')
const r = useRoute(), c = ref(null)
const u = computed(() => units.find(x => x.id === r.params.unit))
watchEffect(async () => {
  c.value = null
  const f = mods[`../content/${r.params.unit}.js`]
  c.value = f ? (await f()).default : false
})
</script>
<template>
  <p><RouterLink to="/">← หน่วยการเรียนรู้ทั้งหมด</RouterLink></p>
  <h1>หน่วยที่ {{ u.n }} {{ u.t }}</h1>
  <p v-if="c === false" class="warn">เนื้อหาหน่วยนี้กำลังจัดทำ</p>
  <template v-else-if="c">
    <section v-for="s in c.sections" :key="s.h">
      <h2>{{ s.h }}</h2>
      <p v-for="t in s.p || []" :key="t">{{ t }}</p>
      <ul v-if="s.li"><li v-for="t in s.li" :key="t">{{ t }}</li></ul>
    </section>
    <RouterLink :to="'/' + u.id + '/quiz'" class="btn">ทำแบบทดสอบเพื่อรับเกียรติบัตร</RouterLink>
  </template>
</template>
