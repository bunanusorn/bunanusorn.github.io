// จัดหมวดหมู่ชุดข้อสอบ (ใช้ id ของชุดใน data/sets.json)
// ชุด Listening จัดเข้าหมวด Listening อัตโนมัติจากฟิลด์ type
// ชุด Reading ที่ไม่อยู่ในรายการ ids จะไปอยู่หมวด "อื่นๆ"
export const CATEGORIES = [
  {
    id: 'science', icon: '🌍', name: 'วิทยาศาสตร์และสิ่งแวดล้อม',
    ids: [3, 9, 14, 15, 21, 26, 30, 34, 43, 54, 60, 70],
  },
  {
    id: 'history', icon: '🏛️', name: 'ประวัติศาสตร์และอารยธรรม',
    ids: [2, 5, 6, 10, 38, 44, 48, 51, 56, 62, 67, 74],
  },
  {
    id: 'economy', icon: '💰', name: 'เศรษฐกิจและการเงิน',
    ids: [7, 8, 11, 45, 57, 68, 71],
  },
  {
    id: 'health', icon: '🧠', name: 'จิตวิทยาและสุขภาพ',
    ids: [16, 20, 47, 59, 61, 63, 66, 73],
  },
  {
    id: 'edu', icon: '🎓', name: 'ภาษาและการศึกษา',
    ids: [13, 46, 53, 64],
  },
  {
    id: 'tech', icon: '💻', name: 'เทคโนโลยีและการคมนาคม',
    ids: [27, 35, 37, 49, 50, 55, 58, 72],
  },
  {
    id: 'arts', icon: '🎬', name: 'ศิลปะ สื่อ และบันเทิง',
    ids: [0, 17, 18, 19, 25, 28, 29, 36, 52, 65],
  },
  {
    id: 'society', icon: '👥', name: 'สังคมและวัฒนธรรม',
    ids: [1, 12, 69],
  },
  { id: 'listening', icon: '🎧', name: 'Listening', type: 'Listening', ids: [] },
  { id: 'other', icon: '📄', name: 'อื่นๆ', ids: [] },
]

const idToCat = new Map()
for (const c of CATEGORIES) for (const id of c.ids) idToCat.set(id, c.id)

export function categoryOf(set) {
  if (set.type === 'Listening') return 'listening'
  return idToCat.get(set.id) || 'other'
}

export const getCategory = (id) => CATEGORIES.find((c) => c.id === id)

// ตัดคำนำหน้าอย่าง "Reading_", "Reading Passage :", "LISTENING TEST –" ออกจากชื่อชุด
export function cleanTitle(t) {
  const out = t
    .replace(/^\s*(reading|listening)(\s+(passage|questions?|practice|test|dialogue))*\s*[_:\-–]*\s*/i, '')
    .replace(/_/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
  return out || t
}
