# คลังข้อสอบ Reading & Listening (Vue 3 + Vite)

โปรเจกต์ฝึกข้อสอบจากไฟล์ `All_Reading_Listening_Newest_to_Oldest.pdf`
(76 ชุด · บทความ · โจทย์ · เฉลย · คำแปลไทย)

## วิธีใช้
```bash
npm install
npm run dev      # เปิดโหมดพัฒนา
npm run build    # สร้างไฟล์ใน dist/
```

## โครงสร้าง
```
src/
  App.vue                    หน้าหลัก + state (ตัวกรอง, โหมดท่องจำ, คะแนน)
  components/
    SetPicker.vue            เลือกประเภท/ชุดข้อสอบ
    QuestionCard.vue         การ์ดโจทย์ปรนัย + เฉลย + คำแปล
    ContentBlock.vue         บทความ/หัวข้อ/คำแปล/ข้อความเฉลย
  data/sets.json             ข้อมูลทั้งหมด (ดึงจาก PDF)
```

## รูปแบบข้อมูล (`sets.json`)
```json
{ "id": 0, "title": "...", "page": 1, "type": "Reading",
  "items": [
    { "k": "h", "t": "หัวข้อ" },
    { "k": "p", "l": "en" | "th", "t": "ข้อความ" },
    { "k": "q", "n": 1, "q": "โจทย์", "o": {"A": "...", "B": "...", "C": "...", "D": "..."},
      "a": "B", "tq": "โจทย์ไทย", "to": {"A": "...", ...} }
  ] }
```

## หมายเหตุ
- ข้อที่ไม่มีเฉลยในต้นฉบับ (`a` เป็น null) จะแสดงว่าไม่มีเฉลย
- ข้อ drag-and-drop / matching และข้อที่จับรูปแบบไม่ได้ แสดงเป็นข้อความธรรมดา (`k: "p"`)
- ภาษาไทยที่ดึงจาก PDF อาจมีวรรณยุกต์เพี้ยนบางจุด แก้ได้ที่ `src/data/sets.json`
