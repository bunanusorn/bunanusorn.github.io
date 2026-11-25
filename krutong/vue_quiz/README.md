# สื่อการสอน CEFR (Vue 3 + Vite)

```
npm install
npm run dev
```

- ข้อมูลทั้งหมดอยู่ใน `src/data/library.json` (สร้างจากไฟล์ Reading_Listening_สรุปแปลไทย.pdf ด้วย `scripts/parse.py`)
- `src/data/checklist.json` = รายการ 81 Reading + 12 Listening จากไฟล์รีวิว 31 ต.ค. 2569 เทียบกับคลัง (`scripts/match.py`, แก้การจับคู่ที่ `scripts/manual.json`)
- ห้ามแต่งข้อสอบเอง: ข้อที่แยกเป็นตัวเลือก/เฉลยได้จะเป็นแบบฝึกหัด ข้อที่แยกไม่ได้แสดงข้อความดิบจากไฟล์
