<template>
  <section class="page">
    <div class="card author-box">
      <div class="author-badge">ผู้พัฒนาชิ้นงาน</div>
      <h2 class="author-name">นายอนุสรณ์ บุญเจริญปัญญา</h2>
      <p class="project-title">ชิ้นงาน: ESP32 x Vue.js (ควบคุม LED ขา D4 / GPIO 4)</p>
    </div>

    <div class="card infographic-box">
      <h3>แผนผังการต่อวงจร (Wiring Diagram Infographic)</h3>
      <img
        src="/wiring-infographic.jpg"
        alt="ESP32 x Vue.js Wiring Diagram Infographic"
        class="infographic-img"
      />
    </div>
  </section>
</template>

<style scoped>
.page {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.card {
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 1.25rem;
  background: #fff;
}
.author-box {
  background: linear-gradient(135deg, #7f1d1d, #991b1b);
  color: #fff;
  border-color: #eab308;
}
.author-badge {
  display: inline-block;
  background: #eab308;
  color: #111827;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  margin-bottom: 0.5rem;
}
.author-name {
  margin: 0;
  font-size: 1.25rem;
}
.project-title {
  margin: 0.35rem 0 0;
  font-size: 0.95rem;
  color: #fef08a;
}
.infographic-box h3 {
  margin: 0 0 0.75rem;
  font-size: 1.05rem;
}
.infographic-img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 8px;
}
</style>