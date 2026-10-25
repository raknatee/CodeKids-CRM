<template>
  <tr class="customer-row">
    <td class="customer-row__cell">
      <RouterLink :to="`/customers/${customer.uid}`" class="customer-row__name">{{ fullName }}</RouterLink>
      <span v-if="customer.codekids_id" class="customer-row__sub">{{ customer.codekids_id }}</span>
    </td>
    <td class="customer-row__cell">{{ customer.nickname || "—" }}</td>
    <td class="customer-row__cell">{{ customer.phone || "—" }}</td>
    <td class="customer-row__cell">{{ customer.email || "—" }}</td>
    <td class="customer-row__cell">{{ customer.city || "—" }}</td>
    <td class="customer-row__cell">
      <LeadStatusBadge :status="customer.lead_status" />
    </td>
    <td class="customer-row__cell customer-row__cell--muted">{{ updatedAt }}</td>
  </tr>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { RouterLink } from "vue-router";
import LeadStatusBadge from "../lead-status-badge/index.vue";
import type { CustomerListItem } from "../../../../types";

const props = defineProps<{
  customer: CustomerListItem;
}>();

const fullName = computed(
  () => [props.customer.first_name, props.customer.last_name].filter(Boolean).join(" ") || "(no name)",
);

// Backend sends UTC without a "Z"; add it so the browser converts to local time.
const updatedAt = computed(() => {
  const raw = props.customer.updated_at;
  const date = new Date(/[zZ]|[+-]\d\d:\d\d$/.test(raw) ? raw : `${raw}Z`);
  return date.toLocaleDateString("en-GB", { day: "2-digit", month: "short", year: "numeric" });
});
</script>

<style scoped>
.customer-row {
  border-top: 1px solid #f3f4f6;
  transition: background-color 0.15s ease;
}

.customer-row:hover {
  background: #f9fafb;
}

.customer-row__cell {
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  color: #111827;
  white-space: nowrap;
}

.customer-row__cell--muted {
  color: #6b7280;
}

.customer-row__name {
  display: block;
  font-weight: 600;
  color: #111827;
  text-decoration: none;
}

.customer-row__name:hover {
  color: #2563eb;
  text-decoration: underline;
}

.customer-row__sub {
  display: block;
  font-size: 0.75rem;
  color: #9ca3af;
}
</style>
