<script lang="ts">
import CTableOrder from "@/components/CTableOrder.vue";
import CTableOverview from "@/components/CTableOverview.vue";
import { ERouter } from "@/enums/routers";
import { ESCustomer, ESOrder, ESOrderItem, ESTable } from "@/enums/store";
import { IFMenuItem } from "@/interfaces/menu";
import { computed, defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default defineComponent({
  setup() {
    const store = useStore();
    const router = useRouter();
    const tableIndex = router.currentRoute.value.params.id as string;
    const table = computed(() =>
      store.getters[ESTable.G_TABLE](parseInt(tableIndex))
    );
    store.dispatch(ESTable.A_INIT_TABLE, table.value);
    if (!table.value) router.push(ERouter.TABLES);
    const orderItemPreviewList = computed(() =>
      store.getters[ESOrderItem.G_ORDER_PREVIEW_LIST](table.value)
    );
    const tableOrder = computed(() =>
      store.getters[ESOrder.G_ORDER_BY_TABLE](table.value)
    );
    const customer = computed(() =>
      store.getters[ESCustomer.G_CUSTOMER_BY_ORDER](tableOrder.value)
    );
    const orderedItemList = computed(() =>
      store.getters[ESOrderItem.G_ORDERED_LIST](table.value)
    );
    const handleSelect = (item: IFMenuItem) => {
      store.dispatch(ESOrderItem.A_ADD_TO_ORDER_PREVIEW, {
        menu: item,
        table: table.value,
      });
    };
    return {
      orderItemPreviewList,
      orderedItemList,
      handleSelect,
      customer,
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
      :customer="customer"
      @handleSelect="(item) => handleSelect(item)"
    />
    <CTableOrder
      :orderedItemList="orderedItemList"
      :table="table"
      :order="tableOrder"
      :customer="customer"
    />
  </div>
</template>

<style lang="scss" scoped>
.wrap {
  gap: var(--s-large);
}
</style>
