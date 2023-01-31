<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    icon: { type: String, required: false },
    placeHolder: { type: String, default: "" },
    info: { type: String, default: "" },
  },
  setup() {
    const value = ref();
    return { value };
  },
});
</script>

<template>
  <div class="wrap">
    <span class="material-icons" v-if="icon">{{ icon }}</span>
    <input class="default" :placeholder="placeHolder" :value="info" />
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  align-items: center;
  gap: var(--s-medium);
}
.default {
  font-weight: var(--fw-small);
  border-radius: var(--br-small);
  border: 1px solid var(--c-greyLight);
  padding: var(--s-sp-small) var(--s-small);
}
</style>
