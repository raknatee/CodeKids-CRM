<template>
  <div style="max-width: 48rem; margin: 0 auto; padding: 2rem 1rem">
    <h1 style="font-size: 1rem; font-weight: 500; color: #6b7280; margin-bottom: 1.5rem">customer</h1>

    <!-- key remounts the sections: each keeps a local copy of its modelValue, so this is how the form resets -->
    <div :key="formKey">
      <CustomerIdentity v-model="identity" />
      <Location v-model="location" />
      <Background v-model="background" />
      <LeadInfo v-model="leadInfo" />
      <SocialAccounts v-model="socialAccounts" />
      <Relationship v-model="relationships" />
    </div>

    <div style="display: flex; align-items: center; justify-content: flex-end; gap: 1rem; margin-top: 1.5rem">
      <span v-if="savedUid" style="font-size: 0.875rem; color: #15803d">Saved customer {{ savedUid }}</span>
      <span v-if="errorMessage" style="font-size: 0.875rem; color: #b91c1c">{{ errorMessage }}</span>
      <button
        type="button"
        :disabled="saving"
        :style="{
          borderRadius: '0.5rem',
          border: 'none',
          backgroundColor: saving ? '#9ca3af' : isSaveHover ? '#1d4ed8' : '#2563eb',
          color: '#ffffff',
          padding: '0.625rem 1.5rem',
          fontSize: '0.875rem',
          fontWeight: 600,
          cursor: saving ? 'not-allowed' : 'pointer',
          transition: 'background-color 0.15s ease',
        }"
        @click="save"
        @mouseenter="isSaveHover = true"
        @mouseleave="isSaveHover = false"
      >
        {{ saving ? "Saving..." : "Save" }}
      </button>
    </div>
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
import { createCustomer, toCustomerCreatePayload } from "./api";
import type {
  CustomerIdentity as CustomerIdentityType,
  CustomerLocation,
  CustomerBackground,
  LeadInfo as LeadInfoType,
  SocialAccount,
  Relationship as RelationshipType,
} from "./types";

const emptyIdentity = (): CustomerIdentityType => ({
  codeKidsId: "",
  nickname: "",
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  dateOfBirth: null,
});
const emptyLocation = (): CustomerLocation => ({ district: "", city: "" });
const emptyBackground = (): CustomerBackground => ({
  education: "",
  workplace: "",
  codingExperience: null,
});
const emptyLeadInfo = (): LeadInfoType => ({
  status: "NEW_LEAD",
  reason: null,
  notes: "",
});
const emptySocialAccounts = (): SocialAccount[] => [{ id: crypto.randomUUID(), platform: null, userId: "" }];
const emptyRelationships = (): RelationshipType[] => [{ id: crypto.randomUUID(), type: null, name: "" }];

const identity = ref(emptyIdentity());
const location = ref(emptyLocation());
const background = ref(emptyBackground());
const leadInfo = ref(emptyLeadInfo());
const socialAccounts = ref(emptySocialAccounts());
const relationships = ref(emptyRelationships());

const formKey = ref(0);
const saving = ref(false);
const isSaveHover = ref(false);
const savedUid = ref<string | null>(null);
const errorMessage = ref<string | null>(null);

function resetForm() {
  identity.value = emptyIdentity();
  location.value = emptyLocation();
  background.value = emptyBackground();
  leadInfo.value = emptyLeadInfo();
  socialAccounts.value = emptySocialAccounts();
  relationships.value = emptyRelationships();
  formKey.value++;
}

async function save() {
  saving.value = true;
  savedUid.value = null;
  errorMessage.value = null;
  try {
    const customer = await createCustomer(
      toCustomerCreatePayload({
        identity: identity.value,
        location: location.value,
        background: background.value,
        leadInfo: leadInfo.value,
      }),
    );
    savedUid.value = customer.uid;
    resetForm();
  } catch (error) {
    errorMessage.value = error instanceof Error ? error.message : String(error);
  } finally {
    saving.value = false;
  }
}
</script>
