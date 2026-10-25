import type { CustomerListItem, CustomerListQuery, CustomerListResponse } from "./types";

// Mock data while the backend has no GET /customer/list endpoint.
export const customerMockup: CustomerListItem[] = [
  {
    uid: "mock-0001",
    codekids_id: "CK1001",
    first_name: "Somchai",
    last_name: "Jaidee",
    nickname: "Chai",
    phone: "0812345678",
    email: "somchai@example.com",
    city: "Bangkok",
    lead_status: "NEW_LEAD",
    updated_at: "2026-10-24T03:15:00Z",
  },
  {
    uid: "mock-0002",
    codekids_id: null,
    first_name: "Malee",
    last_name: "Srisuk",
    nickname: "Mali",
    phone: "0898765432",
    email: null,
    city: "Chiang Mai",
    lead_status: "OLD_LEAD",
    updated_at: "2026-10-22T09:40:00Z",
  },
  {
    uid: "mock-0003",
    codekids_id: "CK1003",
    first_name: "Anan",
    last_name: "Wongsawat",
    nickname: null,
    phone: "0861122334",
    email: "anan.w@example.com",
    city: "Nonthaburi",
    lead_status: "OLD_CUSTOMER",
    updated_at: "2026-10-20T14:05:00Z",
  },
  {
    uid: "mock-0004",
    codekids_id: null,
    first_name: "Pimchanok",
    last_name: "Rattanakul",
    nickname: "Pim",
    phone: null,
    email: "pim.r@example.com",
    city: "Bangkok",
    lead_status: "NEW_LEAD",
    updated_at: "2026-10-18T07:30:00Z",
  },
  {
    uid: "mock-0005",
    codekids_id: "CK1005",
    first_name: "Krit",
    last_name: "Thongdee",
    nickname: "Krit",
    phone: "0825556677",
    email: null,
    city: "Khon Kaen",
    lead_status: "OLD_LEAD",
    updated_at: "2026-10-15T11:20:00Z",
  },
];

// Same search and paging rules as the backend list endpoint.
export function listCustomersMockup({ skip, limit, search }: CustomerListQuery): CustomerListResponse {
  const query = search.trim().toLowerCase();
  const matches = customerMockup.filter(
    (customer) =>
      !query ||
      [customer.first_name, customer.last_name, customer.nickname, customer.phone, customer.email, customer.codekids_id].some(
        (value) => value?.toLowerCase().includes(query),
      ),
  );
  return { total: matches.length, items: matches.slice(skip, skip + limit) };
}
