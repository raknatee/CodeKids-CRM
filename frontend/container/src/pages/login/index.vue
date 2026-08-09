<template>
  <div
    style="
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #ffffff;
    "
  >
    <div
      style="
        width: 100%;
        max-width: 28rem;
        border-radius: 1rem;
        border: 1px solid #e5e7eb;
        padding: 2.5rem;
      "
    >
      <h1
        style="
          font-size: 1.5rem;
          font-weight: 700;
          color: #111827;
          text-align: center;
          margin: 0 0 2.5rem;
        "
      >
        Sign in to CodeKids CRM
      </h1>

      <GoogleSignIn :loading="isLoading" @click="handleGoogleLogin" />

      <div
        style="
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-top: 1.5rem;
        "
      >
        <span style="height: 1px; flex: 1; background-color: #e5e7eb"></span>
        <span style="font-size: 0.75rem; letter-spacing: 0.05em; color: #9ca3af">
          CODEKIDS INTERNAL
        </span>
        <span style="height: 1px; flex: 1; background-color: #e5e7eb"></span>
      </div>

      <p
        v-if="errorMessage"
        style="margin-top: 1.5rem; font-size: 0.875rem; color: #dc2626; text-align: center"
      >
        {{ errorMessage }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import GoogleSignIn from "./components/google-sign-in/index.vue";

const isLoading = ref(false);
const errorMessage = ref("");

async function handleGoogleLogin(): Promise<void> {
  errorMessage.value = "";
  isLoading.value = true;

  try {
    window.location.href = "/api/auth/google";
  } catch (err) {
    errorMessage.value = "Failed to start Google sign-in. Please try again.";
  } finally {
    isLoading.value = false;
  }
}
</script>