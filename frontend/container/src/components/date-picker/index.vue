<template>
  <div ref="rootRef" style="position: relative">
    <button
      type="button"
      :style="{
        width: '100%',
        textAlign: 'left',
        borderRadius: '0.5rem',
        border: `1px solid ${isTriggerHover ? '#9ca3af' : '#d1d5db'}`,
        backgroundColor: '#f9fafb',
        padding: '0.625rem 0.875rem',
        fontSize: '0.875rem',
        color: modelValue ? '#111827' : '#9ca3af',
        cursor: 'pointer',
        transition: 'border-color 0.15s ease',
      }"
      @click="open = !open"
      @mouseenter="isTriggerHover = true"
      @mouseleave="isTriggerHover = false"
    >
      {{ modelValue ? formatDisplay(modelValue) : "dd/mm/yyyy" }}
    </button>

    <div
      v-if="open"
      style="
        position: absolute;
        top: calc(100% + 0.5rem);
        left: 0;
        z-index: 20;
        width: 17.5rem;
        border-radius: 0.75rem;
        background-color: #ffffff;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        padding: 0.75rem;
      "
    >
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem">
        <span style="font-weight: 600; font-size: 0.9rem">{{ monthLabel }}</span>
        <div style="display: flex; gap: 0.5rem">
          <button type="button" style="border: none; background: none; cursor: pointer" @click="shiftMonth(-1)">&#8249;</button>
          <button type="button" style="border: none; background: none; cursor: pointer" @click="shiftMonth(1)">&#8250;</button>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.25rem; font-size: 0.7rem; color: #9ca3af; text-transform: uppercase; margin-bottom: 0.25rem">
        <span v-for="day in weekdayLabels" :key="day" style="text-align: center">{{ day }}</span>
      </div>

      <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.25rem">
        <span
          v-for="cell in calendarCells"
          :key="cell.key"
          :style="cellStyle(cell)"
          @click="cell.date && select(cell.date)"
          @mouseenter="cell.date && (hoveredDate = cell.key)"
          @mouseleave="hoveredDate = null"
        >
          {{ cell.date ? cell.date.getDate() : "" }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from "vue";

const props = defineProps<{
  modelValue: string | null;
}>();

const emit = defineEmits<{
  "update:modelValue": [string];
}>();

const open = ref(false);
const rootRef = ref<HTMLElement | null>(null);
const isTriggerHover = ref(false);
const hoveredDate = ref<string | null>(null);
const today = new Date();
const viewDate = ref(props.modelValue ? new Date(props.modelValue) : new Date(today));

const weekdayLabels = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

const monthLabel = computed(() =>
  viewDate.value.toLocaleDateString("en-US", { month: "long", year: "numeric" }),
);

interface Cell {
  key: string;
  date: Date | null;
}

const calendarCells = computed<Cell[]>(() => {
  const year = viewDate.value.getFullYear();
  const month = viewDate.value.getMonth();
  const firstDay = new Date(year, month, 1);
  const leadingBlanks = firstDay.getDay();
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  const cells: Cell[] = [];
  for (let i = 0; i < leadingBlanks; i++) {
    cells.push({ key: `blank-${i}`, date: null });
  }
  for (let day = 1; day <= daysInMonth; day++) {
    cells.push({ key: `day-${day}`, date: new Date(year, month, day) });
  }
  return cells;
});

function isSameDay(a: Date, b: Date): boolean {
  return a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate();
}

function cellStyle(cell: Cell) {
  if (!cell.date) return { visibility: "hidden" as const };

  const isToday = isSameDay(cell.date, today);
  const isSelected = props.modelValue ? isSameDay(cell.date, new Date(props.modelValue)) : false;
  const isHovered = hoveredDate.value === cell.key;

  return {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: "2rem",
    borderRadius: "9999px",
    fontSize: "0.8rem",
    cursor: "pointer",
    backgroundColor: isSelected ? "#000000" : isHovered ? "#e5e7eb" : isToday ? "#f3f4f6" : "transparent",
    color: isSelected ? "#ffffff" : "#111827",
    transition: "background-color 0.1s ease",
  };
}

function shiftMonth(delta: number): void {
  viewDate.value = new Date(viewDate.value.getFullYear(), viewDate.value.getMonth() + delta, 1);
}

function formatDisplay(value: string): string {
  const date = new Date(value);
  return date.toLocaleDateString("en-GB");
}

function select(date: Date): void {
  emit("update:modelValue", date.toISOString().slice(0, 10));
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