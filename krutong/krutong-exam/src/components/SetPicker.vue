<script setup>
defineProps({ list: Array, count: Function })
const filter = defineModel('filter')
const current = defineModel('current')
</script>

<template>
  <div class="card">
    <div class="row">
      <button v-for="t in ['ทั้งหมด', 'Reading', 'Listening']" :key="t" :class="{ on: filter === t }" @click="filter = t">
        {{ t }}
      </button>
    </div>
    <select v-model.number="current" style="margin-top: 10px">
      <option v-for="s in list" :key="s.id" :value="s.id">
        {{ s.title.slice(0, 70) }} · {{ count(s) }} ข้อ · หน้า {{ s.page }}
      </option>
    </select>
  </div>
</template>
