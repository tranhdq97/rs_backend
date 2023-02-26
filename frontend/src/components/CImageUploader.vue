<template>
  <div class="container">
    <div class="title">{{ $t(title) }}</div>
    <input
      type="file"
      @change="(e) => $emit('onFileSelected', e.target?.files[0])"
    />
    <img v-if="preview" :src="preview || ''" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    title: { type: String, required: true },
    type: { type: String, default: "text" },
    preview: { type: String, default: "false" },
  },
  emits: ["onFileSelected"],
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
img {
  max-width: 500px;
}
</style>
