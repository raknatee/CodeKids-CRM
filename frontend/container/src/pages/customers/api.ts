import { listCustomersMockup } from "./customer-mockup";
import type { CustomerListQuery, CustomerListResponse } from "./types";

const CUSTOMER_LIST_URL = "/api/backend/customer/list";

// Set to false once the backend has GET /api/backend/customer/list.
const USE_MOCKUP = true;

export async function listCustomers(query: CustomerListQuery): Promise<CustomerListResponse> {
  if (USE_MOCKUP) return listCustomersMockup(query);

  const { skip, limit, search } = query;
  const params = new URLSearchParams({ skip: String(skip), limit: String(limit) });
  if (search.trim()) params.set("search", search.trim());

  const res = await fetch(`${CUSTOMER_LIST_URL}?${params}`);
  if (!res.ok) {
    throw new Error(`Could not load customers (${res.status})`);
  }
  return res.json();
}
