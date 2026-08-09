<template>
  <div style="display: grid; grid-template-columns: 1fr 1fr auto; gap: 0.75rem; align-items: center">
    <BaseSelect
      :model-value="modelValue.platform"
      :options="platformOptions"
      placeholder="Platform"
      @update:model-value="handlePlatformChange"
    />
    <input
      :value="modelValue.value"
      :style="inputStyle"
      @input="$emit('update:modelValue', { ...modelValue, value: ($event.target as HTMLInputElement).value })"
    />
    <button
      type="button"
      :style="removeButtonStyle(isRemoveHover)"
      @click="$emit('remove')"
      @mouseenter="isRemoveHover = true"
      @mouseleave="isRemoveHover = false"
    >
      &times;
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import BaseSelect from "../../../../../../components/base-select/index.vue";
import type { AdsInteraction, Platform } from "../../../../types";

const props = defineProps<{
  modelValue: AdsInteraction;
}>();

const emit = defineEmits<{
  "update:modelValue": [AdsInteraction];
  remove: [];
}>();

const platformOptions = [
  { label: "FACEBOOK", value: "FACEBOOK" },
  { label: "LINE", value: "LINE" },
  { label: "INSTAGRAM", value: "INSTAGRAM" },
];

const isRemoveHover = ref(false);

function handlePlatformChange(value: string): void {
  emit("update:modelValue", { ...props.modelValue, platform: value as Platform });
}

const inputStyle = {
  width: "100%",
  borderRadius: "0.5rem",
  border: "1px solid #d1d5db",
  backgroundColor: "#f9fafb",
  padding: "0.625rem 0.875rem",
  fontSize: "0.875rem",
  color: "#111827",
};

function removeButtonStyle(hover: boolean) {
  return {
    border: "1px solid #d1d5db",
    borderRadius: "0.5rem",
    width: "2.25rem",
    height: "2.25rem",
    backgroundColor: hover ? "#fee2e2" : "#ffffff",
    cursor: "pointer",
    color: hover ? "#dc2626" : "#6b7280",
    transition: "background-color 0.1s ease, color 0.1s ease",
  };
}
</script>