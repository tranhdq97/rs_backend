<template>
  <thead v-if="isHeader">
    <tr>
      <th v-for="(column, i) in columns" :key="i">{{ $t(column) }}</th>
    </tr>
  </thead>
  <tr v-else>
    <td
      v-for="column in (columns as string[])"
      :key="column"
      @click="(funcs || {})[column]"
    >
      <div :class="(classes || {})[column]">
        {{ column ? (row || {})[column] : "" }}
        <span class="material-icons" @click="$emit('spanClicked', column)">{{
          (icons || {})[column]
        }}</span>
      </div>
    </td>
  </tr>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    isHeader: { type: Boolean, required: false },
    columns: { type: Array, required: true },
    row: { type: Object, required: false },
    icons: { type: Object, required: false },
    funcs: { type: Object, required: false },
    classes: { type: Object, required: false },
  },
  emits: ["spanClicked"],
});
</script>

<style lang="scss" scoped>
th,
td {
  padding: var(--s-medium);
}
thead {
  background: var(--c-primary);
}
th {
  color: var(--c-white);
  font-weight: var(--fw-medium);
}
span:hover {
  color: var(--c-primary);
}
div {
  gap: var(--s-small);
}
</style>
