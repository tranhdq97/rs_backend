<script lang="ts">
import CTableOrder from "@/components/CTableOrder.vue";
import CTableOverview from "@/components/CTableOverview.vue";
import { ERouter } from "@/enums/routers";
import { ESCustomer, ESOrder, ESOrderItem, ESTable } from "@/enums/store";
import { IFCustomer } from "@/interfaces/customer";
import { IFMenuItem } from "@/interfaces/menu";
import { computed, defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default defineComponent({
  setup() {
    const store = useStore();
    const router = useRouter();
    const tableIndex = router.currentRoute.value.params.id as string;
    const table = store.getters[ESTable.G_TABLE](parseInt(tableIndex));
    if (!table) router.push(ERouter.TABLES);
    const orderItemPreviewList = computed(() =>
      store.getters[ESOrderItem.G_ORDER_PREVIEW_LIST](table)
    );
    const tableOrder = computed(() =>
      store.getters[ESOrder.G_ORDER_BY_TABLE](table)
    );
    const orderedItemList = computed(() =>
      store.getters[ESOrderItem.G_ORDERED_LIST](table)
    );
    const handleSelect = (item: IFMenuItem) => {
      store.dispatch(ESOrderItem.A_ADD_TO_ORDER_PREVIEW, {
        menu: item,
        table: table,
      });
    };
    async function order() {
      await store.dispatch(ESOrderItem.A_ORDER, {
        table: table,
        tableOrder: tableOrder.value,
        items: orderItemPreviewList.value,
        customer: null,
      });
    }
    return {
      orderItemPreviewList,
      orderedItemList,
      handleSelect,
      order,
      table,
      tableOrder,
    };
  },
  components: { CTableOverview, CTableOrder },
});
</script>

<template>
  <div class="container wrap" v-if="table">
    <CTableOverview
      :orderItemPreviewList="orderItemPreviewList"
      :table="table"
      :order="tableOrder"
      @handleSelect="(item) => handleSelect(item)"
      @handleOrder="order"
    />
    <CTableOrder :orderedItemList="orderedItemList" :table="table" />
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  gap: var(--s-large);
}
</style>
