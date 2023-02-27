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
      <div class="ext">
        <slot name="ext"></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>
<style lang="scss" scoped>
.container {
  align-items: center;
}
.icon {
  height: 100px;
  margin-bottom: var(--s-large);
}
.form {
  min-width: 300px;
  background: rgb(240, 250, 240);
  border-radius: var(--br-large);
  padding: var(--s-large);
  box-shadow: -2px -2px 2px var(--bs-color), 2px 2px 2px var(--bs-color);
}
.section {
  width: 100%;
}
.fields {
  gap: var(--s-medium);
  width: 100%;
  border-top: 1px solid var(--c-grey);
  padding-top: var(--s-small);
  margin-bottom: var(--s-large);
}
.btn {
  font-size: var(--fs-s-large);
  font-weight: var(--fw-medium);
  flex-grow: 1;
  border-bottom: none;
}
.ext {
  padding-top: var(--s-medium);
}
</style>
