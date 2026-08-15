<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 2rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem; display: flex; align-items: center; gap: 0.375rem">
      <span style="width: 6px; height: 6px; border-radius: 9999px; background: #111827"></span>
      Background
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.5rem; margin-bottom: 1rem">
      <BackgroundInputFill label="Education" v-model="local.education" />
      <BackgroundInputFill label="Workplace" v-model="local.workplace" />
    </div>

    <CodingExperienceDropdown v-model="codingExperience" />
  </section>
</template>

<script setup lang="ts">
import { computed, reactive, watch } from "vue";
import BackgroundInputFill from "./components/background-input-fill/index.vue";
import CodingExperienceDropdown from "./components/coding-experience-dropdown/index.vue";
import type { CodingExperience, CustomerBackground } from "../../types";

const props = defineProps<{
  modelValue: CustomerBackground;
}>();

const emit = defineEmits<{
  "update:modelValue": [CustomerBackground];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });

const codingExperience = computed({
  get: () => local.codingExperience,
  set: (value: string) => {
    local.codingExperience = value as CodingExperience;
  },
});
</script>