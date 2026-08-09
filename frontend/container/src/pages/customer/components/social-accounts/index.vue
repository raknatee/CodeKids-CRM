<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Social Accounts</h2>

    <div style="display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 0.75rem">
      <SocialAccountRow
        v-for="account in local"
        :key="account.id"
        :model-value="account"
        @update:model-value="(v) => updateAccount(account.id, v)"
        @remove="remove(account.id)"
      />
    </div>

    <button type="button" :style="addButtonStyle" @click="add">+ Add social account</button>
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import SocialAccountRow from "./components/social-account-row/index.vue";
import type { SocialAccount } from "../../types.ts";

const props = defineProps<{
  modelValue: SocialAccount[];
}>();

const emit = defineEmits<{
  "update:modelValue": [SocialAccount[]];
}>();

const local = reactive<SocialAccount[]>(props.modelValue.map((a) => ({ ...a })));

watch(local, (value) => emit("update:modelValue", value.map((a) => ({ ...a }))), { deep: true });

function add(): void {
  local.push({ id: crypto.randomUUID(), platform: null, userId: "" });
}

function remove(id: string): void {
  const index = local.findIndex((a) => a.id === id);
  if (index !== -1) local.splice(index, 1);
}

function updateAccount(id: string, value: SocialAccount): void {
  const index = local.findIndex((a) => a.id === id);
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