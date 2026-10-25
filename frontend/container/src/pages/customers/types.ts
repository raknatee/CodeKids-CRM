export type LeadStatus = "NEW_LEAD" | "OLD_LEAD" | "OLD_CUSTOMER";

// One customer as the backend returns it (flat snake_case).
export interface CustomerListItem {
  uid: string;
  codekids_id?: string | null;
  first_name?: string | null;
  last_name?: string | null;
  nickname?: string | null;
  email?: string | null;
  phone?: string | null;
  city?: string | null;
  lead_status?: LeadStatus;
  updated_at: string;
}

export interface CustomerListResponse {
  total: number;
  items: CustomerListItem[];
}

export interface CustomerListQuery {
  skip: number;
  limit: number;
  search: string;
}
