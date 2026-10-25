<template>
  <div class="customers">
    <header class="customers__header">
      <div>
        <h1 class="customers__title">Customers</h1>
        <p class="customers__subtitle">{{ total }} total</p>
      </div>
      <RouterLink to="/customer" class="customers__add">+ Add customer</RouterLink>
    </header>

    <section class="customers__card">
      <div class="customers__toolbar">
        <CustomerSearch v-model="search" />
      </div>
      <CustomerTable :customers="customers" :loading="loading" :error="error" />
      <CustomerPagination v-model:skip="skip" :limit="limit" :total="total" />
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { RouterLink } from "vue-router";
import CustomerSearch from "./components/customer-search/index.vue";
import CustomerTable from "./components/customer-table/index.vue";
import CustomerPagination from "./components/customer-pagination/index.vue";
import { listCustomers } from "./api";
import type { CustomerListItem } from "./types";

const limit = 20;

const search = ref("");
const skip = ref(0);
const customers = ref<CustomerListItem[]>([]);
const total = ref(0);
const loading = ref(false);
const error = ref<string | null>(null);

// Ignores responses from older requests when the user types or pages quickly.
let requestId = 0;

async function load() {
  const id = ++requestId;
  loading.value = true;
  error.value = null;
  try {
    const result = await listCustomers({ skip: skip.value, limit, search: search.value });
    if (id !== requestId) return;
    customers.value = result.items;
    total.value = result.total;
  } catch (e) {
    if (id !== requestId) return;
    customers.value = [];
    total.value = 0;
    error.value = e instanceof Error ? e.message : String(e);
  } finally {
    if (id === requestId) loading.value = false;
  }
}

let searchTimer: ReturnType<typeof setTimeout> | undefined;
watch(search, () => {
  clearTimeout(searchTimer);
  searchTimer = setTimeout(() => {
    if (skip.value === 0) load();
    else skip.value = 0; // the skip watcher reloads
  }, 300);
});

watch(skip, load);

load();
</script>

<style scoped>
.customers {
  max-width: 72rem;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.customers__header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.customers__title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
}

.customers__subtitle {
  margin: 0.25rem 0 0;
  font-size: 0.875rem;
  color: #6b7280;
}

.customers__add {
  border-radius: 0.5rem;
  background: #111827;
  padding: 0.625rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #ffffff;
  text-decoration: none;
  white-space: nowrap;
  transition: background-color 0.15s ease;
}

.customers__add:hover {
  background: #374151;
}

.customers__card {
  border: 1px solid #d1d5db;
  border-radius: 0.75rem;
  background: #ffffff;
  overflow: hidden;
}

.customers__toolbar {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
}

@media (max-width: 640px) {
  .customers {
    padding: 1.5rem 1rem;
  }

  .customers__title {
    font-size: 1.25rem;
  }
}
</style>
