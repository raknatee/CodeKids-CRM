<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    Admin responded at
    <DateTimePicker :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)" />
  </label>
</template>

<script setup lang="ts">
import DateTimePicker from "../../../../../../components/date-time-picker/index.vue";

defineProps<{
  modelValue: string | null;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();
</script>