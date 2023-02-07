<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    icon: { type: String, required: false },
    type: { type: String, required: false },
    actionIcon: { type: String, required: false },
    placeHolder: { type: String, default: "" },
    content: { type: String || Number, default: "" },
    contentList: { type: Array, required: false },
    isDisabled: { type: Boolean, required: false },
  },
  emits: ["change"],
  setup(props, { emit }) {
    const isChanging = ref(false);
    const change = (e: EventTarget | null) => {
      isChanging.value = true;
      emit("change", e);
    };
    return { isChanging, change };
  },
});
</script>

<template>
  <div class="container">
    <div :class="'wrap' + (isDisabled ? ' disabled' : '')">
      <span
        class="material-icons action-icon"
        v-if="!isDisabled && isChanging && content.length > 0"
      >
        {{ actionIcon || "check" }}
      </span>
      <span
        :class="'material-icons' + (isDisabled ? ' disabled' : '')"
        v-else-if="icon"
        >{{ icon }}</span
      >
      <input
        class="default"
        :type="type || 'text'"
        :placeholder="placeHolder"
        :value="content"
        @input="(e) => change(e?.target)"
      />
    </div>
    <div class="recommend" v-if="contentList?.length">
      <div v-for="(item, i) in contentList" :key="i" class="option">
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  align-items: center;
}
.default {
  font-weight: var(--fw-small);
  border-radius: var(--br-small);
  border: 1px solid var(--c-greyLight);
  padding: var(--s-sp-small) var(--s-small);
}
span {
  padding-right: var(--s-medium);
}
input:hover {
  border: 1px solid var(--c-primary);
}
.action-icon:hover {
  color: var(--c-primary);
}
.disabled {
  pointer-events: none;
  cursor: not-allowed;
  color: var(--c-grey);
}
.recommend {
  margin-left: 44px;
  margin-top: 26px;
  padding: var(--s-small) var(--s-small);
  gap: var(--s-small);
  border-radius: var(--br-small);
  flex-direction: column;
  justify-content: flex-start;
  position: absolute;
  z-index: 99;
  background: rgb(50, 50, 50, 0.75);
  overflow-y: auto;
  &::-webkit-scrollbar {
    width: 3px;
  }
}
.option {
  font-weight: var(--fw-small);
  cursor: pointer;
  justify-content: stretch;
  font-size: var(--fs-s-medium);
  color: var(--c-white);
  &:hover {
    color: var(--c-primary);
  }
}
</style>
