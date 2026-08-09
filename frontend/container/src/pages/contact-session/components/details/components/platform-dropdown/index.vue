<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    <span>Platform <span style="color: #dc2626">*</span></span>
    <BaseSelect :model-value="modelValue" :options="options" placeholder="Platform" @update:model-value="$emit('update:modelValue', $event)" />
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
  { label: "FACEBOOK", value: "FACEBOOK" },
  { label: "LINE", value: "LINE" },
  { label: "INSTAGRAM", value: "INSTAGRAM" },
];
</script>