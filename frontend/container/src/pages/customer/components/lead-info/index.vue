<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Lead Info</h2>

    <div style="margin-bottom: 1rem">
      <LeadStatusRadio v-model="local.status" />
    </div>

    <div style="margin-bottom: 1rem">
      <WhyCodekidsDropdown v-model="reason" />
    </div>

    <NotesInputFill v-model="local.notes" />
  </section>
</template>

<script setup lang="ts">
import { computed, reactive, watch } from "vue";
import LeadStatusRadio from "./components/lead-status-radio/index.vue";
import WhyCodekidsDropdown from "./components/why-codekids-dropdown/index.vue";
import NotesInputFill from "./components/notes-input-fill/index.vue";
import type { LeadInfo, LeadReason, LeadStatus } from "../../types";

const props = defineProps<{
  modelValue: LeadInfo;
}>();

const emit = defineEmits<{
  "update:modelValue": [LeadInfo];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value as LeadInfo }), { deep: true });

const reason = computed({
  get: () => local.reason,
  set: (value: string) => {
    local.reason = value as LeadReason;
  },
});
</script>