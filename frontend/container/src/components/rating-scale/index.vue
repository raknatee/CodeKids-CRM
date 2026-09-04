<template>
  <div class="rating-scale">
    <label class="rating-scale__label">
      {{ label }} <span v-if="required" class="required">*</span>
    </label>
    <div class="rating-scale__options">
      <button
        v-for="n in 10"
        :key="n"
        type="button"
        class="rating-scale__option"
        @click="$emit('update:modelValue', n)"
      >
        <span class="rating-scale__number">{{ n }}</span>
        <span class="rating-scale__dot" :class="{ 'rating-scale__dot--active': modelValue === n }"></span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  modelValue: number | null;
  label: string;
  required?: boolean;
}>();

defineEmits<{
  "update:modelValue": [number];
}>();
</script>

<style scoped>
.rating-scale__label {
  display: block;
  font-size: 0.85rem;
  color: #1f2937;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

.required {
  color: #dc2626;
}

.rating-scale__options {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: 0.5rem;
}

.rating-scale__option {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
}

.rating-scale__number {
  font-size: 0.75rem;
  color: #6b7280;
}

.rating-scale__dot {
  width: 1.1rem;
  height: 1.1rem;
  border-radius: 9999px;
  border: 1px solid #d1d5db;
  background: #ffffff;
  transition: background-color 0.15s ease, border-color 0.15s ease;
}

.rating-scale__option:hover .rating-scale__dot {
  border-color: #f5a623;
}

.rating-scale__dot--active {
  background: #f5a623;
  border-color: #f5a623;
}

@media (max-width: 640px) {
  .rating-scale__options {
    grid-template-columns: repeat(5, 1fr);
    row-gap: 0.75rem;
  }
}
</style>