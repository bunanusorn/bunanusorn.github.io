# 21990-1005 พื้นฐานเทคโนโลยีดิจิทัลในงานอาชีพ (Vue 3 + Vite)

URL ตัวอย่าง: https://bunanusorn.github.io/20190-1005/unit07 และ .../unit07/quiz (ไม่มี .html)

## ใช้งาน
    npm install
    npm run dev      # พัฒนา
    npm run build    # สร้างโฟลเดอร์ dist พร้อม unitNN/ และ unitNN/quiz/

คัดลอก **เนื้อหาภายใน dist/** ไปวางในโฟลเดอร์ `20190-1005/` ของ repo `bunanusorn.github.io` แล้ว push

## เพิ่มเนื้อหาหน่วยอื่น
คัดลอก `src/content/unit07.js` เป็น `unit01.js` ... `unit08.js` แล้วแก้เนื้อหา (sections) และข้อสอบ (quiz)
ระบบจะแสดงหน่วยนั้นว่า “พร้อมเรียน” อัตโนมัติ ถ้าเปลี่ยนชื่อโฟลเดอร์บน github.io ให้แก้ `base` ใน vite.config.js
