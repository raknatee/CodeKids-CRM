import type {
  CodingExperience,
  CustomerBackground,
  CustomerIdentity,
  CustomerLocation,
  LeadInfo,
  LeadReason,
  LeadStatus,
} from "./types";

const CUSTOMER_URL = "/api/backend/customer";

// Backend shape (flat snake_case). socialAccounts / relationships have no backend field yet.
export interface CustomerCreatePayload {
  codekids_id: string | null;
  first_name: string | null;
  last_name: string | null;
  nickname: string | null;
  dob: string | null;
  email: string | null;
  phone: string | null;
  district: string | null;
  city: string | null;
  education: string | null;
  workplace: string | null;
  lead_status: LeadStatus;
  experience: CodingExperience | null;
  notes: string | null;
  why_codekids: LeadReason | null;
}

export interface CustomerOut extends CustomerCreatePayload {
  uid: string;
  updated_at: string;
}

export interface CustomerForm {
  identity: CustomerIdentity;
  location: CustomerLocation;
  background: CustomerBackground;
  leadInfo: LeadInfo;
}

// Empty strings become null so Mongo does not store "".
const orNull = (value: string | null): string | null => value?.trim() || null;

export function toCustomerCreatePayload({ identity, location, background, leadInfo }: CustomerForm): CustomerCreatePayload {
  return {
    codekids_id: orNull(identity.codeKidsId),
    first_name: orNull(identity.firstName),
    last_name: orNull(identity.lastName),
    nickname: orNull(identity.nickname),
    dob: identity.dateOfBirth,
    email: orNull(identity.email),
    phone: orNull(identity.phone),
    district: orNull(location.district),
    city: orNull(location.city),
    education: orNull(background.education),
    workplace: orNull(background.workplace),
    lead_status: leadInfo.status,
    experience: background.codingExperience,
    notes: orNull(leadInfo.notes),
    why_codekids: leadInfo.reason,
  };
}

export async function createCustomer(payload: CustomerCreatePayload): Promise<CustomerOut> {
  const res = await fetch(CUSTOMER_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    throw new Error(`Save failed (${res.status}): ${await res.text()}`);
  }
  return res.json();
}
