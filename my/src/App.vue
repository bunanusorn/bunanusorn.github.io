<script setup>
import { ref } from "vue";

const logoUrl = `${import.meta.env.BASE_URL}logo.png`;

const profile = ref({
  name: "ครู อนุสรณ์ บุญเจริญปัญญา",
  role: "ครูผู้สอน / นักพัฒนาสื่อการเรียนรู้และเทคโนโลยี",
  institution: "วิทยาลัยอาชีวศึกษาเทคโนโลยีฐานวิทยาศาสตร์ (ชลบุรี)",
  bio: "มุ่งมั่นพัฒนาการเรียนการสอนด้านคอมพิวเตอร์ เครือข่าย และการประยุกต์ใช้เทคโนโลยีเพื่อการศึกษา",
  email: "anusorn.bun@example.com",
  github: "https://github.com/bunanusorn",
});

const skills = ref([
  {
    category: "การสอนและวิชาการ",
    items: [
      "คอมพิวเตอร์และการบำรุงรักษา",
      "ระบบเครือข่าย (Cisco / VLAN)",
      "ระบบเลขฐานและการคำนวณ",
    ],
  },
  {
    category: "การพัฒนาและเครื่องมือ",
    items: [
      "Vue.js & Tailwind CSS",
      "Google Apps Script",
      "การออกแบบสื่อและแบบทดสอบอัตโนมัติ",
    ],
  },
]);

const projects = ref([
  {
    title: "ระบบแบบทดสอบอัตโนมัติ (Google Apps Script)",
    desc: "พัฒนาสคริปต์สร้างแบบทดสอบก่อนเรียน-หลังเรียน พร้อมระบบจัดการข้อมูลผู้เรียนอัตโนมัติ",
  },
  {
    title: "ชุดสื่อการเรียนรู้ฮาร์ดแวร์และเครือข่าย",
    desc: "ใบความรู้ สไลด์นำเสนอ และใบงานปฏิบัติการสำหรับรายวิชาคอมพิวเตอร์และการบำรุงรักษา",
  },
]);
</script>

<template>
  <div class="min-h-screen bg-stone-50 text-slate-800">
    <div class="mx-auto max-w-4xl px-4 py-10 sm:px-6">
      <!-- Hero Section -->
      <header
        class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-red-950 via-red-900 to-red-800 px-6 py-10 text-center text-white shadow-xl ring-1 ring-amber-400/40"
      >
        <div
          class="mx-auto mb-4 flex h-28 w-28 items-center justify-center overflow-hidden rounded-full bg-white p-1 shadow-lg ring-4 ring-amber-400"
        >
          <img
            :src="logoUrl"
            alt="ตราสัญลักษณ์วิทยาลัยอาชีวศึกษาเทคโนโลยีฐานวิทยาศาสตร์ (ชลบุรี)"
            class="h-full w-full rounded-full object-contain"
          />
        </div>

        <p
          class="font-heading mb-1 text-xs font-semibold tracking-wide text-amber-300 sm:text-sm"
        >
          {{ profile.institution }}
        </p>
        <h1 class="text-2xl font-bold tracking-tight sm:text-3xl">
          {{ profile.name }}
        </h1>
        <p
          class="font-heading mt-2 text-sm font-medium text-amber-200 sm:text-base"
        >
          {{ profile.role }}
        </p>
        <p
          class="mx-auto mt-3 max-w-xl text-base leading-relaxed text-red-50/95"
        >
          {{ profile.bio }}
        </p>

        <div
          class="font-heading mt-6 flex flex-wrap items-center justify-center gap-3"
        >
          <a
            :href="profile.github"
            target="_blank"
            rel="noopener noreferrer"
            class="rounded-lg bg-amber-400 px-5 py-2.5 text-sm font-semibold text-red-950 shadow transition hover:-translate-y-0.5 hover:bg-amber-300"
          >
            GitHub
          </a>
          <a
            :href="`mailto:${profile.email}`"
            class="rounded-lg border border-amber-300/50 bg-white/10 px-5 py-2.5 text-sm font-semibold text-white backdrop-blur transition hover:-translate-y-0.5 hover:bg-white/20"
          >
            ติดต่อสอบถาม
          </a>
        </div>
      </header>

      <!-- Skills Section -->
      <section class="mt-10">
        <h2
          class="mb-4 border-l-4 border-red-800 pl-3 text-xl font-bold text-red-950"
        >
          ความเชี่ยวชาญและทักษะ
        </h2>
        <div class="grid gap-5 md:grid-cols-2">
          <div
            v-for="(skillGroup, index) in skills"
            :key="index"
            class="rounded-xl border border-amber-200/70 bg-white p-6 shadow-sm transition hover:border-amber-400"
          >
            <h3 class="text-lg font-semibold text-red-900">
              {{ skillGroup.category }}
            </h3>
            <ul
              class="mt-3 list-disc space-y-1.5 pl-5 text-base leading-relaxed text-slate-700"
            >
              <li v-for="(item, idx) in skillGroup.items" :key="idx">
                {{ item }}
              </li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section class="mt-10">
        <h2
          class="mb-4 border-l-4 border-red-800 pl-3 text-xl font-bold text-red-950"
        >
          ผลงานและสื่อการสอน
        </h2>
        <div class="grid gap-5 md:grid-cols-2">
          <div
            v-for="(project, index) in projects"
            :key="index"
            class="rounded-xl border border-amber-200/70 bg-white p-6 shadow-sm transition hover:border-amber-400"
          >
            <h3 class="text-lg font-semibold text-red-900">
              {{ project.title }}
            </h3>
            <p class="mt-2 text-base leading-relaxed text-slate-600">
              {{ project.desc }}
            </p>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer
        class="mt-12 flex flex-col items-center justify-between gap-2 border-t border-slate-200 pt-6 text-sm text-slate-500 sm:flex-row"
      >
        <span>© {{ new Date().getFullYear() }} {{ profile.name }}</span>
        <span class="font-heading">bunanusorn.github.io</span>
      </footer>
    </div>
  </div>
</template>
