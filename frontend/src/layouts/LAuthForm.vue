<template>
  <div class="container">
    <div class="container form">
      <div class="section icon">
        <slot name="icon"></slot>
      </div>
      <div class="container fields">
        <slot name="fields"></slot>
      </div>
      <div class="section btn">
        <slot name="button"></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>
<style lang="scss" scoped>
.icon {
  height: 100px;
}
.form {
  min-width: 300px;
  background: rgba(0, 0, 0, 0.219);
  border-radius: var(--br-large);
  padding: 0 var(--s-large);
}
.section {
  padding: var(--s-medium) 0;
  width: 100%;
}
.fields {
  gap: var(--s-medium);
  width: 100%;
  border-top: 1px solid var(--c-white);
  padding-top: var(--s-small);
}
.btn {
  font-size: var(--fs-s-large);
  font-weight: var(--fw-large);
  flex-grow: 1;
  border-bottom: none;
}
</style>
