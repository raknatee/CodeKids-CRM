<template>
  <label style="display: flex; flex-direction: column; gap: 0.375rem; font-size: 0.8rem; color: #374151">
    <span>Contact type <span style="color: #dc2626">*</span></span>
    <BaseSelect :model-value="modelValue" :options="options" placeholder="Contact Type" @update:model-value="$emit('update:modelValue', $event)" />
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
  { label: "INBOUND_ADS", value: "INBOUND_ADS" },
  { label: "INBOUND_ORGANIC", value: "INBOUND_ORGANIC" },
  { label: "OUTBOUND_FOLLOWUP", value: "OUTBOUND_FOLLOWUP" },
];
</script>