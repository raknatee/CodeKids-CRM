<template>
  <span class="icon-badge">
    <slot />
  </span>
</template>

<script setup lang="ts">
</script>

<style scoped>
.icon-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 9999px;
  background: #f5a623;
  flex-shrink: 0;
}

.icon-badge :deep(svg) {
  width: 0.85rem;
  height: 0.85rem;
  fill: #ffffff;
}
</style>