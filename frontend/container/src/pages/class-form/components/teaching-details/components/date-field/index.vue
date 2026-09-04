<template>
  <div class="date-field">
    <label class="date-field__label">
      {{ label }} <span v-if="required" class="required">*</span>
    </label>
    <DatePicker :model-value="modelValue" @update:model-value="$emit('update:modelValue', $event)" />
  </div>
</template>

<script setup lang="ts">
import DatePicker from "../../../../../../components/date-picker/index.vue";

defineProps<{
  modelValue: string | null;
  label: string;
  required?: boolean;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();
</script>

<style scoped>
.date-field {
  margin-bottom: 1.25rem;
}

.date-field__label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}

.required {
  color: #dc2626;
}
</style>