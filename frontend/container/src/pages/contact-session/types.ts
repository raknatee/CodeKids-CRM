export type Platform = "FACEBOOK" | "LINE" | "INSTAGRAM";

export type ContactType = "INBOUND_ADS" | "INBOUND_ORGANIC" | "OUTBOUND_FOLLOWUP";

export type Requirement =
  | "TRIAL"
  | "CONSULT_CODING"
  | "ENTREPRENEUR_CAMP"
  | "TECHZANIA_CAMP"
  | "AI_CAMP"
  | "DIGITAL_ART"
  | "BOOK"
  | "FREE_INFORMATION"
  | "ABOUT_CODEKIDS"
  | "IN_HOUSE"
  | "SUMMER_CAMP"
  | "OTHER";

export interface ContactSessionDetails {
  platform: Platform | null;
  contactType: ContactType | null;
  contactedAt: string | null;
  adminRespondedAt: string | null;
  requirement: Requirement | null;
  insight: string;
}

export interface FollowUp {
  tag: string;
}

export interface AdsInteraction {
  id: string;
  platform: Platform | null;
  value: string;
}