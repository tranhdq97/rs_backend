<template>
  <div class="btn">{{ $t(name) }}</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    name: {
      type: String,
      required: true,
    },
  },
});
</script>

<style lang="scss" scoped>
.btn {
  outline: none;
  border-radius: var(--br-small);
  cursor: pointer;
  background: var(--c-primary);
  color: var(--c-white);
  padding: var(--s-small);
  font-size: inherit;
  flex-grow: 1;
  &:hover {
    background: var(--c-primaryDark);
  }
}
</style>
