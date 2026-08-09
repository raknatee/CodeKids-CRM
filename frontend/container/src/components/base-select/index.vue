<template>
  <div ref="rootRef" style="position: relative">
    <button
      type="button"
      :style="{
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        borderRadius: '0.5rem',
        border: `1px solid ${isTriggerHover ? '#9ca3af' : '#d1d5db'}`,
        backgroundColor: '#f9fafb',
        padding: '0.625rem 0.875rem',
        fontSize: '0.875rem',
        color: selectedLabel ? '#111827' : '#9ca3af',
        cursor: 'pointer',
        transition: 'border-color 0.15s ease',
      }"
      @click="open = !open"
      @mouseenter="isTriggerHover = true"
      @mouseleave="isTriggerHover = false"
    >
      <span>{{ selectedLabel || placeholder }}</span>
      <span :style="{ transform: open ? 'rotate(180deg)' : 'rotate(0deg)', transition: 'transform 0.15s ease' }">
        &#9662;
      </span>
    </button>

    <div
      v-if="open"
      style="
        position: absolute;
        top: calc(100% + 0.25rem);
        left: 0;
        right: 0;
        z-index: 20;
        border-radius: 0.5rem;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
      "
    >
      <div
        v-for="option in options"
        :key="option.value"
        :style="{
          padding: '0.625rem 0.875rem',
          fontSize: '0.875rem',
          backgroundColor: optionBackground(option.value),
          color: '#111827',
          cursor: 'pointer',
          transition: 'background-color 0.1s ease',
        }"
        @click="select(option.value)"
        @mouseenter="hoveredOption = option.value"
        @mouseleave="hoveredOption = null"
      >
        {{ option.label }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

interface Option {
  label: string;
  value: string;
}

const props = defineProps<{
  modelValue: string | null;
  options: Option[];
  placeholder?: string;
}>();

const emit = defineEmits<{
  "update:modelValue": [string];
}>();

const open = ref(false);
const rootRef = ref<HTMLElement | null>(null);
const isTriggerHover = ref(false);
const hoveredOption = ref<string | null>(null);

const selectedLabel = computed(
  () => props.options.find((option) => option.value === props.modelValue)?.label ?? "",
);

function optionBackground(value: string): string {
  if (hoveredOption.value === value) return "#c7ccd1";
  if (props.modelValue === value) return "#d1d5db";
  return "#e5e7eb";
}

function select(value: string): void {
  emit("update:modelValue", value);
  open.value = false;
}

function handleClickOutside(event: MouseEvent): void {
  if (rootRef.value && !rootRef.value.contains(event.target as Node)) {
    open.value = false;
  }
}

onMounted(() => document.addEventListener("click", handleClickOutside));
onBeforeUnmount(() => document.removeEventListener("click", handleClickOutside));
</script>