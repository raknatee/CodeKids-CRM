<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    Insight
    <textarea
      :value="modelValue"
      placeholder="What did we learn about this customer's motivation..."
      rows="3"
      :style="textareaStyle"
      @input="$emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
    />
  </label>
</template>

<script setup lang="ts">
defineProps<{
  modelValue: string;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();

const textareaStyle = {
  width: "100%",
  borderRadius: "0.5rem",
  border: "1px solid #d1d5db",
  backgroundColor: "#f9fafb",
  padding: "0.625rem 0.875rem",
  fontSize: "0.875rem",
  color: "#111827",
  fontFamily: "inherit",
  resize: "vertical" as const,
};
</script>