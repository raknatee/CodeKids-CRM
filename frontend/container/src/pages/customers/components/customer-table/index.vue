<template>
  <div class="customer-table">
    <table class="customer-table__table">
      <thead>
        <tr>
          <th v-for="column in columns" :key="column" class="customer-table__head">{{ column }}</th>
        </tr>
      </thead>
      <tbody>
        <CustomerRow v-for="customer in customers" :key="customer.uid" :customer="customer" />
      </tbody>
    </table>

    <p v-if="loading" class="customer-table__state">Loading customers...</p>
    <p v-else-if="error" class="customer-table__state customer-table__state--error">{{ error }}</p>
    <p v-else-if="customers.length === 0" class="customer-table__state">No customers found.</p>
  </div>
</template>

<script setup lang="ts">
import CustomerRow from "./components/customer-row/index.vue";
import type { CustomerListItem } from "../../types";

defineProps<{
  customers: CustomerListItem[];
  loading: boolean;
  error: string | null;
}>();

const columns = ["Name", "Nickname", "Phone", "Email", "City", "Lead status", "Updated"];
</script>

<style scoped>
.customer-table {
  overflow-x: auto;
}

.customer-table__table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.customer-table__head {
  padding: 0.75rem 1rem;
  background: #f9fafb;
  font-size: 0.75rem;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  white-space: nowrap;
}

.customer-table__state {
  margin: 0;
  padding: 2.5rem 1rem;
  text-align: center;
  font-size: 0.875rem;
  color: #6b7280;
}

.customer-table__state--error {
  color: #b91c1c;
}
</style>
