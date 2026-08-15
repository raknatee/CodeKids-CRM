export interface CustomerIdentity {
  codeKidsId: string;
  nickname: string;
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  dateOfBirth: string | null;
}

export interface CustomerLocation {
  district: string;
  city: string;
}

export type CodingExperience = "EVER" | "LITTLE" | "NEVER";

export interface CustomerBackground {
  education: string;
  workplace: string;
  codingExperience: CodingExperience | null;
}

export type LeadStatus = "NEW_LEAD" | "OLD_LEAD" | "OLD_CUSTOMER";

export type LeadReason =
  | "ADS"
  | "TIKTOK"
  | "COMMENT_RESPONSE"
  | "WORD_OF_MOUTH";

export interface LeadInfo {
  status: LeadStatus;
  reason: LeadReason | null;
  notes: string;
}

export type SocialPlatform = "FACEBOOK" | "LINE" | "INSTAGRAM";

export interface SocialAccount {
  id: string;
  platform: SocialPlatform | null;
  userId: string;
}

export type RelationshipType =
  | "FATHER"
  | "MOTHER"
  | "SIBLING"
  | "RELATIVE"
  | "OTHER";

export interface Relationship {
  id: string;
  type: RelationshipType | null;
  name: string;
}