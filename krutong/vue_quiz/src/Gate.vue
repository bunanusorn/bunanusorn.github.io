<script setup>
import { ref } from 'vue'
const emit = defineEmits(['ok'])
const CODE = '11111111'
const code = ref(''), err = ref(false)
const submit = () => {
  if (code.value.trim() === CODE) {
    try { localStorage.setItem('cefr_unlocked', '1') } catch (e) {}
    emit('ok')
  } else { err.value = true; code.value = '' }
}
</script>
<template>
  <div class="gate">
    <div class="card gate-box">
      <h1>สื่อการสอน CEFR</h1>
      <p class="sub">กรุณาใส่รหัสเพื่อเข้าใช้งาน</p>
      <input type="password" inputmode="numeric" v-model="code" placeholder="รหัส" autofocus
             @keyup.enter="submit" @input="err = false" />
      <p v-if="err" class="badge bad">รหัสไม่ถูกต้อง</p>
      <button class="on" style="margin-top:12px;width:100%" @click="submit">เข้าสู่ระบบ</button>
    </div>
  </div>
</template>
<style scoped>
.gate{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px}
.gate-box{width:100%;max-width:340px;text-align:center}
input{width:100%;font:inherit;font-size:1.2rem;text-align:center;letter-spacing:.3em;padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink)}
</style>
