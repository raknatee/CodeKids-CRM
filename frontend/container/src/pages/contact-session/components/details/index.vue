<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem; display: flex; align-items: center; gap: 0.375rem">
      <span style="width: 6px; height: 6px; border-radius: 9999px; background: #111827"></span>
      ContactSession · Details
    </h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.5rem; margin-bottom: 1rem">
      <PlatformDropdown v-model="local.platform" />
      <ContactTypeDropdown v-model="local.contactType" />
      <ContactedAtFill v-model="local.contactedAt" />
      <AdminRespondedAtFill v-model="local.adminRespondedAt" />
    </div>

    <div style="margin-bottom: 1rem">
      <RequirementDropdown v-model="local.requirement" />
    </div>

    <InsightTextareaFill v-model="local.insight" />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import PlatformDropdown from "./components/platform-dropdown/index.vue";
import ContactTypeDropdown from "./components/contact-type-dropdown/index.vue";
import ContactedAtFill from "./components/contacted-at-fill/index.vue";
import AdminRespondedAtFill from "./components/admin-responded-at-fill/index.vue";
import RequirementDropdown from "./components/requirement-dropdown/index.vue";
import InsightTextareaFill from "./components/insight-textarea-fill/index.vue";
import type { ContactSessionDetails } from "../../types.ts";

const props = defineProps<{
  modelValue: ContactSessionDetails;
}>();

const emit = defineEmits<{
  "update:modelValue": [ContactSessionDetails];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>