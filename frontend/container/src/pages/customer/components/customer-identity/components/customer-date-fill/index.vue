<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    {{ label }}
    <DatePicker :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)" />
  </label>
</template>

<script setup lang="ts">
import DatePicker from "../../../../../../components/date-picker/index.vue";

defineProps<{
  label: string;
  modelValue: string | null;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();
</script>