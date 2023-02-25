<template>
  <div class="container">
    <div v-if="title" class="title">{{ $t(title) }}</div>
    <select @change="(e) => $emit('select', parseInt(e.target?.value))">
      <option
        v-for="(item, idx) in selectList"
        :key="idx"
        :selected="item?.id === defaultID"
        :value="item.id"
      >
        {{ item?.name || "" }}
      </option>
    </select>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    title: { type: String, required: false },
    selectList: { type: Array, required: false },
    defaultID: { type: Number, required: false },
  },
  emits: ["select"],
  setup() {
    const value = ref("");
    return { value };
  },
});
</script>

<style lang="scss" scoped>
.container {
  width: 100%;
  gap: var(--s-small);
}
.title {
  width: 100%;
  justify-content: left;
  font-size: var(--fs-medium);
}
select {
  background: var(--c-white);
  border-radius: var(--br-small);
  border: 1px solid var(--c-grey);
  &:hover {
    border: 1px solid var(--c-primary);
  }
}
</style>
