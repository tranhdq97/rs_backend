<template>
  <div class="container">
    <div class="wrap">
      <input :type="type" :placeholder="$t(placeHolder)" />
      <span class="material-icons">search</span>
    </div>
    <div class="recommend" v-if="data.length">
      <div
        v-for="(item, i) in data"
        :key="i"
        class="option"
        @click="$emit('handleClick')"
      >
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    type: { type: String, default: "text" },
    placeHolder: { type: String, default: "" },
    data: { type: Array, default: () => [] },
  },
  emits: ["handleClick"],
  setup() {
    const handleClick = (item: object) => {
      return item;
    };
    return { handleClick };
  },
});
</script>

<style lang="scss" scoped>
.wrap {
  align-items: center;
}
input {
  background: var(--c-background);
}
span {
  padding-left: var(--s-small);
  &:hover {
    color: var(--c-primary);
  }
}
.recommend {
  margin-top: 42px;
  flex-direction: column;
  justify-content: flex-start;
  position: absolute;
  z-index: 99;
  background: rgb(50, 50, 50, 0.1);
  max-height: 200px;
  overflow-y: auto;
  &::-webkit-scrollbar {
    width: 3px;
  }
}
.option {
  cursor: pointer;
  justify-content: stretch;
  padding: 1px var(--s-small);
  font-size: var(--fs-s-medium);
  &:hover {
    color: var(--c-white);
  }
}
</style>
