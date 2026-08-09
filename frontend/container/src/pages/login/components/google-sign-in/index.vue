<template>
  <button
    type="button"
    :disabled="loading"
    :style="{
      width: '100%',
      display: 'flex',
      alignItems: 'center',
      gap: '0.75rem',
      borderRadius: '0.75rem',
      border: 'none',
      backgroundColor: isHovering ? '#1f2937' : '#000000',
      padding: '0.875rem 1.25rem',
      color: '#ffffff',
      fontWeight: 600,
      fontSize: '1rem',
      cursor: loading ? 'not-allowed' : 'pointer',
      opacity: loading ? 0.6 : 1,
      transition: 'background-color 0.15s ease',
    }"
    @click="$emit('click')"
    @mouseenter="isHovering = true"
    @mouseleave="isHovering = false"
  >
    <img
      src="../../../../assets/img/google-color-svgrepo-com.svg"
      alt="Google"
      style="height: 1.25rem; width: 1.25rem"
    />
    <span style="flex: 1; text-align: center">
      {{ loading ? "Signing in..." : "Continue with Google" }}
    </span>
  </button>
</template>

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