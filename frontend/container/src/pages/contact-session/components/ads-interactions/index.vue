<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Ads Interactions</h2>

    <div style="display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 0.75rem">
      <AdsInteractionRow
        v-for="interaction in local"
        :key="interaction.id"
        :model-value="interaction"
        @update:model-value="(v) => updateInteraction(interaction.id, v)"
        @remove="remove(interaction.id)"
      />
    </div>

    <button
      type="button"
      :style="addButtonStyle(isAddHover)"
      @click="add"
      @mouseenter="isAddHover = true"
      @mouseleave="isAddHover = false"
    >
      + Attach ads interaction
    </button>
  </section>
</template>

<script setup lang="ts">
import { reactive, ref, watch } from "vue";
import AdsInteractionRow from "./components/ads-interaction-row/index.vue";
import type { AdsInteraction } from "../../types";

const props = defineProps<{
  modelValue: AdsInteraction[];
}>();

const emit = defineEmits<{
  "update:modelValue": [AdsInteraction[]];
}>();

const local = reactive<AdsInteraction[]>(props.modelValue.map((a) => ({ ...a })));
const isAddHover = ref(false);

watch(local, (value) => emit("update:modelValue", value.map((a) => ({ ...a }))), { deep: true });

function add(): void {
  local.push({ id: crypto.randomUUID(), platform: null, value: "" });
}

function remove(id: string): void {
  const index = local.findIndex((a) => a.id === id);
  if (index !== -1) local.splice(index, 1);
}

function updateInteraction(id: string, value: AdsInteraction): void {
  const index = local.findIndex((a) => a.id === id);
  if (index !== -1) local[index] = value;
}

function addButtonStyle(hover: boolean) {
  return {
    width: "100%",
    borderRadius: "0.5rem",
    border: `1px dashed ${hover ? "#9ca3af" : "#d1d5db"}`,
    backgroundColor: hover ? "#f3f4f6" : "#f9fafb",
    padding: "0.625rem 0.875rem",
    fontSize: "0.8rem",
    color: "#374151",
    cursor: "pointer",
    transition: "background-color 0.1s ease, border-color 0.1s ease",
  };
}
</script>