<script setup lang="ts">
const profile = {
  name: 'นายอนุสรณ์ บุญเจริญปัญญา',
  occupation: 'ครูคอมพิวเตอร์',
}
</script>

<template>
  <section class="intro-card">
    <h2>แนะนำตัว (Introduction)</h2>
    <div class="info-row">
      <span class="label">ชื่อ-นามสกุล:</span>
      <span class="value">{{ profile.name }}</span>
    </div>
    <div class="info-row">
      <span class="label">อาชีพ:</span>
      <span class="value">{{ profile.occupation }}</span>
    </div>
  </section>
</template>

<style scoped>
.intro-card {
  padding: 1.5rem;
  border: 1px solid var(--color-border, #ccc);
  border-radius: 8px;
}
h2 {
  margin-bottom: 1rem;
  color: #42b883;
}
.info-row {
  display: flex;
  gap: 8px;
  margin-bottom: 0.5rem;
  font-size: 1.05rem;
}
.label {
  font-weight: bold;
}
</style>