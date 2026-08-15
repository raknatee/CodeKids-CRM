<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    Why CodeKids<span style="color: #dc2626">*</span>
    <BaseSelect :model-value="modelValue" :options="options" placeholder="Select a reason..." @update:model-value="$emit('update:modelValue', $event)" />
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
  { label: "ADS", value: "ADS" },
  { label: "TIKTOK", value: "TIKTOK" },
  { label: "COMMENT_RESPONSE", value: "COMMENT_RESPONSE" },
  { label: "WORD_OF_MOUTH", value: "WORD_OF_MOUTH" },
];
</script>