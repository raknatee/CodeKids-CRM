<template>
  <span class="lead-status-badge" :class="`lead-status-badge--${status ?? 'NONE'}`">
    {{ status ?? "—" }}
  </span>
</template>

<script setup lang="ts">
import type { LeadStatus } from "../../../../types";

defineProps<{
  status?: LeadStatus;
}>();
</script>

<style scoped>
.lead-status-badge {
  display: inline-block;
  border-radius: 9999px;
  padding: 0.2rem 0.6rem;
  font-size: 0.7rem;
  font-weight: 600;
  white-space: nowrap;
}

.lead-status-badge--NEW_LEAD {
  background: #dbeafe;
  color: #1d4ed8;
}

.lead-status-badge--OLD_LEAD {
  background: #fef3c7;
  color: #b45309;
}

.lead-status-badge--OLD_CUSTOMER {
  background: #dcfce7;
  color: #15803d;
}

.lead-status-badge--NONE {
  background: #f3f4f6;
  color: #6b7280;
}
</style>
