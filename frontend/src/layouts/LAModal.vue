<template>
  <div class="bg">
    <div class="modal">
      <div>
        <span class="material-icons close" @click="$emit('close')">close</span>
      </div>
      <div class="scope">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>
<style lang="scss" scoped>
.bg {
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  align-items: center;
  background: var(--c-modal);
  z-index: 105;
  position: fixed;
}
.modal {
  flex-direction: column;
  align-items: stretch;
}
.scope {
  margin-top: -10%;
  padding: var(--s-large);
  flex-direction: column;
  background: var(--c-white);
  border-radius: var(--br-medium);
  gap: var(--s-small);
}
.close {
  margin-right: -100%;
  background: var(--c-white);
  padding: var(--s-small);
  border-radius: 50%;
  z-index: 100;
  &:hover {
    color: var(--c-alert);
  }
}
</style>
