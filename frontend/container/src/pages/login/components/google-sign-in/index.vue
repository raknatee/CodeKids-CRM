<template>
  <button type="button" :disabled="loading" class="btn" :style="{

    backgroundColor: isHovering ? '#1f2937' : '#000000',
    cursor: loading ? 'not-allowed' : 'pointer',
    opacity: loading ? 0.6 : 1,
    transition: 'background-color 0.15s ease',
  }" @click="$emit('click')" @mouseenter="isHovering = true" @mouseleave="isHovering = false">
    <img src="../../../../assets/img/google-color-svgrepo-com.svg" alt="Google"
      style="height: 1.25rem; width: 1.25rem" />
    <span style="flex: 1; text-align: center">
      {{ loading ? "Signing in..." : "Continue with Google" }}
    </span>
  </button>
</template>

<style scoped>
.btn {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  border-radius: 0.75rem;
  border: none;
  padding: 0.875rem 1.25rem;
  color: #ffffff;
    font-weight: 600;
    font-size: 1rem;
}
</style>


<script setup lang="ts">
import { ref } from "vue";

defineProps<{
  loading?: boolean;
}>();

defineEmits<{
  click: [];
}>();

const isHovering = ref(false);
</script>