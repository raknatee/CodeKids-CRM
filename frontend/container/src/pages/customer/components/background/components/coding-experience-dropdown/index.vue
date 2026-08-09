<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    Coding experience <span style="color: #dc2626">*</span>
    <BaseSelect :model-value="modelValue" :options="options" placeholder="Select experience..." @update:model-value="$emit('update:modelValue', $event)" />
  </label>
</template>

<script setup lang="ts">
import BaseSelect from "../../../../../../components/base-select/index.vue";

defineProps<{
  modelValue: string | null;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();

const options = [
  { label: "EVER", value: "EVER" },
  { label: "LITTLE", value: "LITTLE" },
  { label: "NEVER", value: "NEVER" },
];
</script>