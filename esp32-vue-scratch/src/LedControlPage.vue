<script setup>
import { ref, onBeforeUnmount } from 'vue'

const esp32Ip = ref('192.168.1.105') // แก้ไขเป็น IP ของ ESP32
const isConnected = ref(false)
const ledState = ref(false)
const errorMessage = ref('')
let socket = null

function connect() {
  errorMessage.value = ''
  if (socket) socket.close()
  socket = new WebSocket(`ws://${esp32Ip.value}:81`)
  socket.onopen = () => {
    isConnected.value = true
  }
  socket.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data)
      if (data.type === 'led_status') ledState.value = Boolean(data.led)
    } catch (err) {
      console.error('JSON Error:', err)
    }
  }
  socket.onerror = () => {
    errorMessage.value = 'เชื่อมต่อไม่สำเร็จ ตรวจสอบ IP และ Wi-Fi วงเดียวกัน'
  }
  socket.onclose = () => {
    isConnected.value = false
  }
}

function disconnect() {
  if (socket) {
    socket.close()
    socket = null
  }
  isConnected.value = false
}

function sendCommand(payload) {
  if (!socket || socket.readyState !== WebSocket.OPEN) return
  socket.send(JSON.stringify(payload))
}

onBeforeUnmount(() => disconnect())
</script>

<template>
  <section class="page">
    <h1>ควบคุม LED ขา D4 (GPIO 4)</h1>

    <div class="card">
      <label>IP Address ของ ESP32:</label>
      <div class="row">
        <input v-model.trim="esp32Ip" type="text" placeholder="192.168.1.105" />
        <button v-if="!isConnected" @click="connect">เชื่อมต่อ</button>
        <button v-else class="danger" @click="disconnect">ตัดการเชื่อมต่อ</button>
      </div>
      <p>
        สถานะ:
        <strong :style="{ color: isConnected ? '#16a34a' : '#dc2626' }">
          {{ isConnected ? 'เชื่อมต่อแล้ว' : 'ยังไม่เชื่อมต่อ' }}
        </strong>
      </p>
      <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>

    <div class="card">
      <h2>สถานะ LED: {{ ledState ? 'เปิด (ON)' : 'ปิด (OFF)' }}</h2>
      <div class="row">
        <button
          class="on"
          :disabled="!isConnected"
          @click="sendCommand({ command: 'set_led', state: true })"
        >
          เปิด LED
        </button>
        <button
          class="off"
          :disabled="!isConnected"
          @click="sendCommand({ command: 'set_led', state: false })"
        >
          ปิด LED
        </button>
        <button
          class="toggle"
          :disabled="!isConnected"
          @click="sendCommand({ command: 'toggle_led' })"
        >
          สลับสถานะ
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.card {
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 1.25rem;
  margin-bottom: 1rem;
  background: #fff;
}
.row {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}
input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid #9ca3af;
  border-radius: 6px;
}
button {
  padding: 0.55rem 0.9rem;
  border: none;
  border-radius: 6px;
  color: #fff;
  background: #2563eb;
  cursor: pointer;
}
button.on {
  background: #16a34a;
}
button.off,
button.danger {
  background: #dc2626;
}
button.toggle {
  background: #d97706;
}
button:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}
.error {
  color: #dc2626;
  font-size: 0.9rem;
}
</style>