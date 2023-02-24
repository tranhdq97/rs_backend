<script lang="ts">
import { IFMasterData } from "@/interfaces/common";
import { defineComponent, ref } from "vue";

export default defineComponent({
  props: {
    type: { type: String, default: "text" },
    placeHolder: { type: String, default: "" },
    searchData: { type: Array, default: () => [] },
  },
  emits: ["handleSelect"],
  setup(props) {
    const searchedList = ref<IFMasterData[]>([]);
    const searchValue = ref("");
    const isRecommendClosed = ref(true);

    const closeRecommend = () => {
      isRecommendClosed.value = true;
    };
    const handleSearch = () => {
      isRecommendClosed.value = false;
      searchedList.value = (props.searchData as IFMasterData[]).filter((item) =>
        item?.name ? item?.name.includes(searchValue.value) : false
      );
    };
    return {
      searchValue,
      handleSearch,
      searchedList,
      isRecommendClosed,
      closeRecommend,
    };
  },
});
</script>

<template>
  <div class="container">
    <div class="wrap">
      <input
        :type="type"
        :placeholder="$t(placeHolder)"
        v-model="searchValue"
        @keyup="handleSearch"
      />
    </div>
    <div
      class="recommend"
      v-if="searchedList.length && searchValue.length && !isRecommendClosed"
      v-click-outside-element="closeRecommend"
    >
      <div
        v-for="(item, i) in searchedList"
        :key="i"
        class="option"
        @click="$emit('handleSelect', item)"
      >
        {{ item.name }}
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.container {
  flex-grow: 1;
}
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
  margin-top: 36px;
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
  cursor: pointer;
  justify-content: stretch;
  font-size: var(--fs-s-medium);
  color: var(--c-white);
  &:hover {
    color: var(--c-primary);
  }
}
</style>
