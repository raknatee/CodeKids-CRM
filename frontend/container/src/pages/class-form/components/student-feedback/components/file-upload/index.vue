<template>
  <div class="file-upload">
    <label class="file-upload__label">{{ label }}</label>
    <label class="file-upload__dropzone">
      <input type="file" class="file-upload__input" @change="handleChange" />
      <span class="file-upload__icon">⬆️</span>
      <span class="file-upload__text file-upload__text--desktop">
        ลากไฟล์มาวางหรือคลิกเพื่ออัปโหลด
      </span>
      <span class="file-upload__text file-upload__text--mobile">
        แตะเพื่ออัปโหลดไฟล์
      </span>
      <span class="file-upload__caption">Upload capture / VDO file</span>
    </label>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  label: string;
}>();

const emit = defineEmits<{
  "update:modelValue": [File | null];
}>();

function handleChange(event: Event): void {
  const file = (event.target as HTMLInputElement).files?.[0] ?? null;
  emit("update:modelValue", file);
}
</script>

<style scoped>
.file-upload {
  margin-top: 1rem;
}

.file-upload__label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.file-upload__dropzone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  border: 2px dashed #d1d5db;
  border-radius: 0.75rem;
  background: #f9fafb;
  padding: 2rem 1rem;
  cursor: pointer;
  text-align: center;
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.file-upload__dropzone:hover {
  border-color: #9ca3af;
  background: #f3f4f6;
}

.file-upload__input {
  display: none;
}

.file-upload__icon {
  font-size: 1.25rem;
}

.file-upload__text {
  font-size: 0.85rem;
  color: #374151;
}

.file-upload__text--mobile {
  display: none;
}

.file-upload__caption {
  font-size: 0.75rem;
  color: #9ca3af;
}

@media (max-width: 640px) {
  .file-upload__text--desktop {
    display: none;
  }

  .file-upload__text--mobile {
    display: block;
  }

  .file-upload__dropzone {
    padding: 1.5rem 1rem;
  }
}
</style>