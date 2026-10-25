<template>
  <div class="customer-pagination">
    <span class="customer-pagination__summary">
      {{ total === 0 ? "0 customers" : `${from}–${to} of ${total}` }}
    </span>
    <div class="customer-pagination__buttons">
      <button type="button" class="customer-pagination__button" :disabled="skip === 0" @click="$emit('update:skip', Math.max(0, skip - limit))">
        Prev
      </button>
      <button type="button" class="customer-pagination__button" :disabled="to >= total" @click="$emit('update:skip', skip + limit)">
        Next
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = defineProps<{
  skip: number;
  limit: number;
  total: number;
}>();

defineEmits<{
  "update:skip": [number];
}>();

const from = computed(() => props.skip + 1);
const to = computed(() => Math.min(props.skip + props.limit, props.total));
</script>

<style scoped>
.customer-pagination {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0.75rem 1rem;
  border-top: 1px solid #e5e7eb;
}

.customer-pagination__summary {
  font-size: 0.8rem;
  color: #6b7280;
}

.customer-pagination__buttons {
  display: flex;
  gap: 0.5rem;
}

.customer-pagination__button {
  border: 1px solid #d1d5db;
  border-radius: 0.5rem;
  background: #ffffff;
  padding: 0.4rem 0.9rem;
  font-size: 0.8rem;
  color: #111827;
  cursor: pointer;
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.customer-pagination__button:hover:not(:disabled) {
  border-color: #9ca3af;
  background: #f9fafb;
}

.customer-pagination__button:disabled {
  color: #d1d5db;
  cursor: not-allowed;
}
</style>
