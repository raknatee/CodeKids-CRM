<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Customer · Identity</h2>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.5rem">
      <CustomerInputFill label="CodeKids ID" v-model="local.codeKidsId" />
      <CustomerInputFill label="Nickname" v-model="local.nickname" />
      <CustomerInputFill label="First name" v-model="local.firstName" />
      <CustomerInputFill label="Last name" v-model="local.lastName" />
      <CustomerInputFill label="Email" type="email" v-model="local.email" />
      <CustomerInputFill label="Phone" type="tel" v-model="local.phone" />
      <CustomerDateFill label="Date of birth" v-model="local.dateOfBirth" />
    </div>
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import CustomerInputFill from "./components/customer-input-fill/index.vue";
import CustomerDateFill from "./components/customer-date-fill/index.vue";
import type { CustomerIdentity } from "../../types";

const props = defineProps<{
  modelValue: CustomerIdentity;
}>();

const emit = defineEmits<{
  "update:modelValue": [CustomerIdentity];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>