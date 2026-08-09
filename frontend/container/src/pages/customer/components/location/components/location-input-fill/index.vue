<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151; margin-bottom: 1rem">
    {{ label }}
    <input
      :value="modelValue"
      :style="inputStyle"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    />
  </label>
</template>

<script setup lang="ts">
defineProps<{
  label: string;
  modelValue: string;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();

const inputStyle = {
  width: "100%",
  borderRadius: "0.5rem",
  border: "1px solid #d1d5db",
  backgroundColor: "#f9fafb",
  padding: "0.625rem 0.875rem",
  fontSize: "0.875rem",
  color: "#111827",
};
</script>