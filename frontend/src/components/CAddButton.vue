<template>
  <span class="material-icons btn">add</span>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>

<style lang="scss" scoped>
.btn {
  color: var(--c-white);
  background: var(--c-primaryTransparent);
  padding: var(--s-small);
  border-radius: var(--br-medium);
  position: fixed;
  z-index: 100;
  right: var(--s-large);
  bottom: var(--s-large);
  &:hover {
    background: var(--c-primaryDark);
  }
}
</style>
