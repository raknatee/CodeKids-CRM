<template>
  <label class="customer-search">
    <svg class="customer-search__icon" viewBox="0 0 24 24" aria-hidden="true">
      <path d="M10 2a8 8 0 0 1 6.32 12.9l5.39 5.4-1.41 1.4-5.4-5.39A8 8 0 1 1 10 2zm0 2a6 6 0 1 0 0 12 6 6 0 0 0 0-12z" />
    </svg>
    <input
      class="customer-search__input"
      type="search"
      placeholder="Search name, nickname, phone, email, CodeKids ID"
      :value="modelValue"
      @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
    />
  </label>
</template>

<script setup lang="ts">
defineProps<{
  modelValue: string;
}>();

defineEmits<{
  "update:modelValue": [string];
}>();
</script>

<style scoped>
.customer-search {
  position: relative;
  display: block;
  width: 100%;
  max-width: 24rem;
}

.customer-search__icon {
  position: absolute;
  top: 50%;
  left: 0.75rem;
  width: 1rem;
  height: 1rem;
  transform: translateY(-50%);
  fill: #9ca3af;
  pointer-events: none;
}

.customer-search__input {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  background: #f9fafb;
  padding: 0.625rem 0.875rem 0.625rem 2.25rem;
  font-size: 0.875rem;
  color: #111827;
  transition: border-color 0.15s ease;
}

.customer-search__input::placeholder {
  color: #9ca3af;
}

.customer-search__input:hover {
  border-color: #9ca3af;
}

.customer-search__input:focus {
  outline: none;
  border-color: #111827;
  background: #ffffff;
}

@media (max-width: 640px) {
  .customer-search {
    max-width: none;
  }
}
</style>
