<template>
  <div class="container">
    <div class="title">{{ $t(title) }}</div>
    <input
      :type="type"
      :placeholder="$t(placeHolder)"
      v-model="value"
      @input="$emit('content', value)"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    title: { type: String, required: true },
    type: { type: String, default: "text" },
    placeHolder: { type: String, default: "" },
  },
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
</style>
