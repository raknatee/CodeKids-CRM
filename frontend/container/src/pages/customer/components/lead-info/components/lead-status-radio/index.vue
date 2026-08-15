<template>
  <div>
    <p style="font-size: 0.8rem; color: #374151; margin: 0 0 0.5rem">
      Lead status <span style="color: #dc2626">*</span>
    </p>
    <div style="display: flex; gap: 0.5rem">
      <button
        v-for="status in options"
        :key="status"
        type="button"
        :style="pillStyle(status)"
        @click="$emit('update:modelValue', status)"
        @mouseenter="hoveredStatus = status"
        @mouseleave="hoveredStatus = null"
      >
        {{ status }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
  modelValue: string;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();

const options = ["NEW_LEAD", "OLD_LEAD", "OLD_CUSTOMER"];
const hoveredStatus = ref<string | null>(null);

function pillStyle(status: string) {
  const isSelected = props.modelValue === status;
  const isHovered = hoveredStatus.value === status;

  return {
    borderRadius: "9999px",
    padding: "0.4rem 0.9rem",
    fontSize: "0.75rem",
    fontWeight: 600,
    border: isSelected ? "none" : `1px solid ${isHovered ? "#9ca3af" : "#d1d5db"}`,
    backgroundColor: isSelected ? "#000000" : isHovered ? "#f3f4f6" : "#ffffff",
    color: isSelected ? "#ffffff" : "#374151",
    cursor: "pointer",
    transition: "background-color 0.1s ease, border-color 0.1s ease",
  };
}
</script>