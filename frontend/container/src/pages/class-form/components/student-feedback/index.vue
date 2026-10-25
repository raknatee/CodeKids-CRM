<template>
  <section class="card">
    <h2 class="card__title">
      <IconBadge>
        <svg viewBox="0 0 24 24"><path d="M12 2l2.9 6.26L22 9.27l-5 4.87L18.18 21 12 17.27 5.82 21 7 14.14l-5-4.87 7.1-1.01z"/></svg>
      </IconBadge>
      Feed Forward นักเรียน
    </h2>

    <RatingScale
      label="สอบถามนักเรียนให้คะแนนในการตั้งใจเรียนเท่าไหร่"
      required
      v-model="local.engagementScore"
    />

    <div class="field">
      <label class="field__label">ถามน้องว่าได้เรียนรู้อะไรบ้าง <span class="required">*</span></label>
      <textarea class="field__textarea" placeholder="Your answer" v-model="local.learnings" />
    </div>

    <div class="field">
      <label class="field__label">กรุณาใส่ link ผลงานของน้อง (เช่น scratch)</label>
      <input class="field__input" placeholder="https://scratch.mit.edu/..." v-model="local.portfolioLink" />
    </div>

    <FileUpload
      label="Capture หน้าจอผลงาน / Code ล่าสุด / VDO การสอน"
      @update:model-value="(file) => (local.captureFile = file)"
    />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import RatingScale from "../../../../components/rating-scale/index.vue";
import IconBadge from "../../../../components/icon-badge/index.vue";
import FileUpload from "./components/file-upload/index.vue";
import type { StudentFeedback } from "../../types";

const props = defineProps<{
  modelValue: StudentFeedback;
}>();

const emit = defineEmits<{
  "update:modelValue": [StudentFeedback];
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

.field {
  margin-top: 1.25rem;
}

.field__label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.required {
  color: #dc2626;
}

.field__input,
.field__textarea {
  width: 100%;
  border: 1px solid #e5e7eb;
  border-bottom-width: 2px;
  border-radius: 0.25rem;
  padding: 0.6rem 0.75rem;
  font-size: 0.875rem;
  color: #111827;
  background: #ffffff;
  font-family: inherit;
}

.field__textarea {
  min-height: 5rem;
  resize: vertical;
}

.field__input:focus,
.field__textarea:focus {
  outline: none;
  border-color: #f5a623;
}

@media (max-width: 640px) {
  .card {
    padding: 1.25rem;
    border-radius: 0.75rem;
  }
}
</style>