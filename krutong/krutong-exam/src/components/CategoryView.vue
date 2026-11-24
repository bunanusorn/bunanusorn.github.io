<script setup>
import { cleanTitle } from '../categories.js'

defineProps({ category: Object, list: Array, count: Function })
defineEmits(['open-set'])
</script>

<template>
  <div>
    <h1>{{ category.icon }} {{ category.name }}</h1>
    <p class="meta">{{ list.length }} ชุด</p>

    <button v-for="(s, i) in list" :key="s.id" class="item" @click="$emit('open-set', s.id)">
      <span class="no">{{ i + 1 }}</span>
      <span class="body">
        <span class="title">{{ cleanTitle(s.title) }}</span>
        <span class="meta">{{ count(s) }} ข้อ · หน้า {{ s.page }} ของไฟล์ต้นฉบับ</span>
      </span>
      <span class="badge" :class="{ lis: s.type === 'Listening' }">{{ s.type }}</span>
    </button>
  </div>
</template>

<style scoped>
h1 { font-family: Georgia, serif; font-size: 1.45rem; margin: 0.1em 0; }
.item {
  display: flex; align-items: center; gap: 12px; width: 100%; text-align: left;
  padding: 12px 14px; margin-bottom: 8px; border-radius: 12px;
  background: var(--card); border: 1px solid var(--line);
}
.item:hover { border-color: var(--acc); }
.no {
  flex: none; width: 30px; height: 30px; border-radius: 50%; display: grid; place-items: center;
  background: var(--thbg); color: var(--th); font-weight: 700; font-size: 0.85rem;
}
.body { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.title { font-weight: 600; overflow-wrap: anywhere; }
.badge {
  flex: none; font-size: 0.72rem; padding: 2px 8px; border-radius: 999px;
  background: var(--okbg); color: var(--ok); font-weight: 700;
}
.badge.lis { background: var(--thbg); color: var(--th); }
</style>
