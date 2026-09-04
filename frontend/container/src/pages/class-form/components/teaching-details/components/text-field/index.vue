<template>
  <div class="text-field">
    <label class="text-field__label">
      {{ label }} <span v-if="required" class="required">*</span>
      <span v-if="hint" class="text-field__hint">{{ hint }}</span>
    </label>
    <input
      class="text-field__input"
      :placeholder="placeholder ?? 'Your answer'"
      :value="modelValue"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    />
  </div>
</template>

<script setup lang="ts">
defineProps<{
  modelValue: string;
  label: string;
  required?: boolean;
  hint?: string;
  placeholder?: string;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();
</script>

<style scoped>
.text-field {
  margin-bottom: 1.25rem;
}

.text-field__label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.required {
  color: #dc2626;
}

.text-field__hint {
  display: block;
  font-size: 0.7rem;
  font-weight: 400;
  color: #9ca3af;
  margin-top: 0.1rem;
}

.text-field__input {
  width: 100%;
  border: 1px solid #e5e7eb;
  border-bottom-width: 2px;
  border-radius: 0.25rem;
  padding: 0.6rem 0.75rem;
  font-size: 0.875rem;
  color: #111827;
  background: #ffffff;
}

.text-field__input::placeholder {
  color: #9ca3af;
}

.text-field__input:hover {
  border-color: #d1d5db;
}

.text-field__input:focus {
  outline: none;
  border-color: #f5a623;
}
</style>