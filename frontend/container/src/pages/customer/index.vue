<template>
  <div style="max-width: 48rem; margin: 0 auto; padding: 2rem 1rem">
    <h1 style="font-size: 1rem; font-weight: 500; color: #6b7280; margin-bottom: 1.5rem">customer</h1>

    <CustomerIdentity v-model="identity" />
    <Location v-model="location" />
    <Background v-model="background" />
    <LeadInfo v-model="leadInfo" />
    <SocialAccounts v-model="socialAccounts" />
    <Relationship v-model="relationships" />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CustomerIdentity from "./components/customer-identity/index.vue";
import Location from "./components/location/index.vue";
import Background from "./components/background/index.vue";
import LeadInfo from "./components/lead-info/index.vue";
import SocialAccounts from "./components/social-accounts/index.vue";
import Relationship from "./components/relationship/index.vue";
import type {
  CustomerIdentity as CustomerIdentityType,
  CustomerLocation,
  CustomerBackground,
  LeadInfo as LeadInfoType,
  SocialAccount,
  Relationship as RelationshipType,
} from "./types";

const identity = ref<CustomerIdentityType>({
  codeKidsId: "",
  nickname: "",
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  dateOfBirth: null,
});

const location = ref<CustomerLocation>({ district: "", city: "" });

const background = ref<CustomerBackground>({
  education: "",
  workplace: "",
  codingExperience: null,
});

const leadInfo = ref<LeadInfoType>({
  status: "NEW_LEAD",
  reason: null,
  notes: "",
});

const socialAccounts = ref<SocialAccount[]>([{ id: crypto.randomUUID(), platform: null, userId: "" }]);

const relationships = ref<RelationshipType[]>([{ id: crypto.randomUUID(), type: null, name: "" }]);
</script>