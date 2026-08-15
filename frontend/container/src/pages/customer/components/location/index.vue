<template>
  <section style="border: 1px solid #d1d5db; border-radius: 0.75rem; padding: 1.5rem; margin-top: 1.5rem">
    <h2 style="font-size: 0.9rem; font-weight: 600; margin: 0 0 1rem">Location</h2>

    <LocationInputFill label="District" v-model="local.district" />
    <LocationInputFill label="City" v-model="local.city" />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import LocationInputFill from "./components/location-input-fill/index.vue";
import type { CustomerLocation } from "../../types";

const props = defineProps<{
  modelValue: CustomerLocation;
}>();

const emit = defineEmits<{
  "update:modelValue": [CustomerLocation];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>