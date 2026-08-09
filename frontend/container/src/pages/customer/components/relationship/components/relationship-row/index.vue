<template>
  <div style="display: grid; grid-template-columns: 1fr 1fr auto; gap: 0.75rem; align-items: center">
    <BaseSelect
      :model-value="modelValue.type"
      :options="typeOptions"
      placeholder="Relationship"
      @update:model-value="handleTypeChange"
    />
    <input
      :value="modelValue.name"
      placeholder="Name"
      :style="inputStyle"
      @input="$emit('update:modelValue', { ...modelValue, name: ($event.target as HTMLInputElement).value })"
    />
    <button type="button" :style="removeButtonStyle" @click="$emit('remove')">&times;</button>
  </div>
</template>

<script setup lang="ts">
import BaseSelect from "../../../../../../components/base-select/index.vue";
import type { Relationship, RelationshipType } from "../../../../types";

const props = defineProps<{
  modelValue: Relationship;
}>();

const emit = defineEmits<{
  "update:modelValue": [Relationship];
  remove: [];
}>();

const typeOptions = [
  { label: "FATHER", value: "FATHER" },
  { label: "MOTHER", value: "MOTHER" },
  { label: "SIBLING", value: "SIBLING" },
  { label: "RELATIVE", value: "RELATIVE" },
  { label: "OTHER", value: "OTHER" },
];

function handleTypeChange(value: string): void {
  emit("update:modelValue", { ...props.modelValue, type: value as RelationshipType });
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

const removeButtonStyle = {
  border: "1px solid #d1d5db",
  borderRadius: "0.5rem",
  width: "2.25rem",
  height: "2.25rem",
  backgroundColor: "#ffffff",
  cursor: "pointer",
  color: "#6b7280",
};
</script>