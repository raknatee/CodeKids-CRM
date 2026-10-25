<template>
  <section class="card">
    <h2 class="card__title">
      <IconBadge>
        <svg viewBox="0 0 24 24"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm0 2c-4.42 0-8 2.24-8 5v1a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-1c0-2.76-3.58-5-8-5z"/></svg>
      </IconBadge>
      Feed Forward ตนเอง
    </h2>

    <RatingScale
      label="ให้คะแนนในการตั้งใจสอนเท่าไหร่"
      required
      v-model="local.engagementScore"
    />
  </section>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import RatingScale from "../../../../components/rating-scale/index.vue";
import IconBadge from "../../../../components/icon-badge/index.vue";
import type { SelfFeedback } from "../../types";

const props = defineProps<{
  modelValue: SelfFeedback;
}>();

const emit = defineEmits<{
  "update:modelValue": [SelfFeedback];
}>();

const local = reactive({ ...props.modelValue });

watch(local, (value) => emit("update:modelValue", { ...value }), { deep: true });
</script>

<style scoped>
.card {
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

.card__title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
  font-weight: 700;
  color: #111827;
  margin: 0 0 1.25rem;
}

@media (max-width: 640px) {
  .card {
    padding: 1.25rem;
    border-radius: 0.75rem;
  }
}
</style>