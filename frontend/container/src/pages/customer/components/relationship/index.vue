<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Relationships</h2>

    <div style="display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 0.75rem">
      <RelationshipRow
        v-for="relationship in local"
        :key="relationship.id"
        :model-value="relationship"
        @update:model-value="(v) => updateRelationship(relationship.id, v)"
        @remove="remove(relationship.id)"
      />
    </div>

    <button type="button" :style="addButtonStyle" @click="add">+ Add relationship</button>
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import RelationshipRow from "./components/relationship-row/index.vue";
import type { Relationship } from "../../types";

const props = defineProps<{
  modelValue: Relationship[];
}>();

const emit = defineEmits<{
  "update:modelValue": [Relationship[]];
}>();

const local = reactive<Relationship[]>(props.modelValue.map((r) => ({ ...r })));

watch(local, (value) => emit("update:modelValue", value.map((r) => ({ ...r }))), { deep: true });

function add(): void {
  local.push({ id: crypto.randomUUID(), type: null, name: "" });
}

function remove(id: string): void {
  const index = local.findIndex((r) => r.id === id);
  if (index !== -1) local.splice(index, 1);
}

function updateRelationship(id: string, value: Relationship): void {
  const index = local.findIndex((r) => r.id === id);
  if (index !== -1) local[index] = value;
}

const addButtonStyle = {
  width: "100%",
  borderRadius: "0.5rem",
  border: "1px dashed #d1d5db",
  backgroundColor: "#f9fafb",
  padding: "0.625rem 0.875rem",
  fontSize: "0.8rem",
  color: "#374151",
  cursor: "pointer",
};
</script>