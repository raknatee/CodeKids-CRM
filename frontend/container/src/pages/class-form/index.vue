<template>
  <div class="class-form">
    <header class="class-form__header">
      <img src="../../assets/img/logo-color-codekids.png" alt="CodeKids" class="class-form__logo" />
      <h1 class="class-form__title">ระบบบันทึกการเรียนสำหรับคุณครู CodeKids</h1>
    </header>

    <div class="class-form__body">
      <TeachingDetails v-model="teachingDetails" />
      <StudentFeedback v-model="studentFeedback" />
      <SelfFeedback v-model="selfFeedback" />

      <button type="button" class="class-form__submit">ส่งแบบฟอร์ม</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import TeachingDetails from "./components/teaching-details/index.vue";
import StudentFeedback from "./components/student-feedback/index.vue";
import SelfFeedback from "./components/self-feedback/index.vue";
import type {
  TeachingDetails as TeachingDetailsType,
  StudentFeedback as StudentFeedbackType,
  SelfFeedback as SelfFeedbackType,
} from "./types";

const teachingDetails = ref<TeachingDetailsType>({
  teacherName: "",
  teacherId: "",
  course: "",
  classId: "",
  sessionNumber: "",
  studentName: "",
  studentId: "",
  paymentDate: null,
});

const studentFeedback = ref<StudentFeedbackType>({
  engagementScore: null,
  learnings: "",
  portfolioLink: "",
  captureFile: null,
});

const selfFeedback = ref<SelfFeedbackType>({
  engagementScore: null,
});
</script>

<style scoped>
.class-form {
  position: relative;
  min-height: 100vh;
  background-color: #f7c948;
  padding: 2.5rem 1.5rem 4rem;
  overflow: hidden;
}

.class-form::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image: url("../../assets/img/kids-pattern-01.png");
  background-repeat: repeat;
  background-size: 350px 350px;
  opacity: 0.5;
  pointer-events: none;
}

.class-form__header {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-bottom: 2rem;
}

.class-form__body {
  position: relative;
  z-index: 1;
  max-width: 44rem;
  margin: 0 auto;
}

.class-form__logo {
  height: 2rem;
  width: auto;
  display: block;
  margin: 0 auto 0.5rem;
}

.class-form__title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin: 0;

}

.class-form__submit {
  display: block;
  width: 100%;
  border: none;
  border-radius: 9999px;
  background: #111827;
  color: #ffffff;
  font-size: 0.95rem;
  font-weight: 600;
  padding: 0.9rem;
  cursor: pointer;
  transition: background-color 0.15s ease;
  margin-top: 24px;
}

.class-form__submit:hover {
  background: #f7c948;
  color:#111827;
}

@media (max-width: 640px) {
  .class-form {
    padding: 2rem 1rem 3rem;
  }

  .class-form__title {
    font-size: 1.1rem;
  }
}
</style>