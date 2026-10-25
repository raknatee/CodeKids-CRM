<template>
  <section class="card">
    <h2 class="card__title">
      <IconBadge>
        <svg viewBox="0 0 24 24"><path d="M7 3h10a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm1 4h8v2H8V7zm0 4h8v2H8v-2zm0 4h5v2H8v-2z"/></svg>
      </IconBadge>
      รายละเอียดการสอน
    </h2>

    <TextField label="ชื่อคุณครู (เช่น ครูพี่อ้อม)" required v-model="local.teacherName" />
    <TextField label="teacher_id" required v-model="local.teacherId" />
    <TextField
      label="หลักสูตรที่สอน (เช่น game level 1, PrePython, Website)"
      required
      v-model="local.course"
    />

    <div class="card__row">
      <TextField label="class_id" required v-model="local.classId" />
      <TextField
        label="ครั้งที่เรียน (เฉพาะตัวเลข)"
        required
        placeholder="e.g. 3"
        v-model="local.sessionNumber"
      />
    </div>

    <TextField label="ชื่อนักเรียน" required v-model="local.studentName" />
    <TextField
      label="student_id"
      required
      hint="ถ้ามากกว่า 1 คนใส่ + เช่น s1+s2"
      v-model="local.studentId"
    />

    <DateField label="วันที่เรียน เพื่อทำการจ่ายเงิน" required v-model="local.paymentDate" />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import TextField from "./components/text-field/index.vue";
import DateField from "./components/date-field/index.vue";
import IconBadge from "../../../../components/icon-badge/index.vue";
import type { TeachingDetails } from "../../types";

const props = defineProps<{
  modelValue: TeachingDetails;
}>();

const emit = defineEmits<{
  "update:modelValue": [TeachingDetails];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>

<style scoped>
.card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  margin-bottom: 1.5rem;
}

.card__title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 1.25rem;
}

.card__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 1.25rem;
}

@media (max-width: 640px) {
  .card {
    padding: 1.25rem;
    border-radius: 0.75rem;
  }

  .card__row {
    grid-template-columns: 1fr;
  }
}
</style>