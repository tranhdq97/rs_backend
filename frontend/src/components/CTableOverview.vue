<script lang="ts">
import { ECommon } from "@/enums/common";
import { ESMenu, ESTable } from "@/enums/store";
import { IFTable } from "@/interfaces/tables";
import { computed, defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import CButton from "./CButton.vue";
import CPreOrder from "./CPreOrder.vue";
import CSearchField from "./CSearchField.vue";

export default defineComponent({
  props: {
    orderItemPreviewList: { type: Array, default: () => [] },
  },
  emits: ["handleSelect", "handleOrder"],
  setup() {
    const router = useRouter();
    const store = useStore();
    const tableIndex: number = parseInt(
      router.currentRoute.value.params.index as string
    );
    const table: IFTable = store.getters[ESTable.G_TABLE](tableIndex);
    const searchData = computed(() => store.getters[ESMenu.G_AVAILABLE_MENU]);
    return { ECommon, searchData, table };
  },
  components: { CSearchField, CPreOrder, CButton },
});
</script>

<template>
  <div class="container area">
    <div class="head-info">
      <span class="material-icons">table_restaurant</span>
      {{ $t(ECommon.TABLE) }}: {{ table.name }}
    </div>
    <div class="head-info">
      <div class="sub-info">
        <span class="material-icons">contact_phone</span>
        <div>{{ "0934346270" }}</div>
      </div>
      <div class="sub-info">
        <span class="material-icons">badge</span>
        <div>{{ "Dong Quoc Tranh" }}</div>
      </div>
      <div class="sub-info">
        <span class="material-icons">groups</span>
        <div>{{ 5 }}</div>
      </div>
    </div>
    <div class="head-info search">
      <span class="material-icons">menu_book</span>
      <CSearchField
        :placeHolder="ECommon.SEARCH"
        :searchData="searchData"
        @handleSelect="(item) => $emit('handleSelect', item)"
      />
    </div>
    <div class="header" v-if="orderItemPreviewList.length">
      {{ $t(ECommon.PREVIEW) }}
    </div>
    <div class="container pre-order">
      <CPreOrder
        v-for="(item, i) in orderItemPreviewList"
        :key="i"
        :item="item"
      />
    </div>
    <CButton
      :name="ECommon.ORDER"
      @click="$emit('handleOrder')"
      v-if="orderItemPreviewList.length"
    />
  </div>
</template>

<style lang="scss" scoped>
.container {
  overflow-y: auto;
  justify-content: flex-start;
  gap: var(--s-small);
}
.header {
  border-bottom: 1px solid var(--c-grey);
  justify-content: flex-start;
  padding: var(--s-small) 0;
  font-weight: var(--fw-medium);
}
.head-info {
  justify-content: flex-start;
  align-items: center;
  text-transform: capitalize;
  font-weight: var(--fw-large);
  gap: var(--s-medium);
  span {
    font-weight: var(--fw-small);
  }
}
.sub-info {
  align-items: center;
  gap: var(--s-medium);
}
.pre-order {
  gap: var(--s-small);
  overflow-y: auto;
  max-height: 300px;
}
.search {
  justify-content: stretch;
}
</style>
