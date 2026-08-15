<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    <span>Requirement <span style="color: #dc2626">*</span></span>
    <BaseSelect :model-value="modelValue" :options="options" placeholder="Requirement" @update:model-value="$emit('update:modelValue', $event)" />
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
  { label: "TRIAL", value: "TRIAL" },
  { label: "CONSULT_CODING", value: "CONSULT_CODING" },
  { label: "ENTREPRENEUR_CAMP", value: "ENTREPRENEUR_CAMP" },
  { label: "TECHZANIA_CAMP", value: "TECHZANIA_CAMP" },
  { label: "AI_CAMP", value: "AI_CAMP" },
  { label: "DIGITAL_ART", value: "DIGITAL_ART" },
  { label: "BOOK", value: "BOOK" },
  { label: "FREE_INFORMATION", value: "FREE_INFORMATION" },
  { label: "ABOUT_CODEKIDS", value: "ABOUT_CODEKIDS" },
  { label: "IN_HOUSE", value: "IN_HOUSE" },
  { label: "SUMMER_CAMP", value: "SUMMER_CAMP" },
  { label: "OTHER", value: "OTHER" },
];
</script>