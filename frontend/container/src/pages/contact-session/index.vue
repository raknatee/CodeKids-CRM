<template>
  <div style="max-width: 48rem; margin: 0 auto; padding: 2rem 1rem">
    <h1 style="font-size: 1rem; font-weight: 500; color: #6b7280; margin-bottom: 1.5rem">ContactSession</h1>

    <Details v-model="details" />
    <FollowUp v-model="followUp" />
    <AdsInteractions v-model="adsInteractions" />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Details from "./components/details/index.vue";
import FollowUp from "./components/follow-up/index.vue";
import AdsInteractions from "./components/ads-interactions/index.vue";
import type { ContactSessionDetails, FollowUp as FollowUpType, AdsInteraction } from "./types";

const details = ref<ContactSessionDetails>({
  platform: null,
  contactType: null,
  contactedAt: null,
  adminRespondedAt: null,
  requirement: null,
  insight: "",
});

const followUp = ref<FollowUpType>({ tag: "" });

const adsInteractions = ref<AdsInteraction[]>([{ id: crypto.randomUUID(), platform: null, value: "" }]);
</script>