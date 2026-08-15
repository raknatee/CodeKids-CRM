<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem; display: flex; align-items: center; gap: 0.375rem">
      <span style="width: 6px; height: 6px; border-radius: 9999px; background: #111827"></span>
      Follow-up
    </h2>

    <FollowUpTagFill v-model="local.tag" />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import FollowUpTagFill from "./components/follow-up-tag-fill/index.vue";
import type { FollowUp } from "../../types.ts";

const props = defineProps<{
  modelValue: FollowUp;
}>();

const emit = defineEmits<{
  "update:modelValue": [FollowUp];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>