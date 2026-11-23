// สร้างโฟลเดอร์ unitNN และ unitNN/quiz ให้ URL ไม่ต้องมี .html (GitHub Pages เสิร์ฟ index.html ในโฟลเดอร์)
import { mkdirSync, copyFileSync, writeFileSync } from 'fs'
const d = 'dist', idx = `${d}/index.html`
copyFileSync(idx, `${d}/404.html`)
writeFileSync(`${d}/.nojekyll`, '')
for (let i = 1; i <= 8; i++) {
  const u = 'unit' + String(i).padStart(2, '0')
  mkdirSync(`${d}/${u}/quiz`, { recursive: true })
  copyFileSync(idx, `${d}/${u}/index.html`)
  copyFileSync(idx, `${d}/${u}/quiz/index.html`)
}
console.log('postbuild ok')
