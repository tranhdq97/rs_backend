<template>
  <div class="container wrap">
    <CTableOverview
      :orderItemPreviewList="orderItemPreviewList"
      @handleSelect="(item) => handleSelect(item)"
      @handleOrder="order"
    />
    <CTableOrder :orderedItemList="orderedItemList" />
  </div>
</template>

<script lang="ts">
import CTableOrder from "@/components/CTableOrder.vue";
import CTableOverview from "@/components/CTableOverview.vue";
import { ESOrderItem, ESTable } from "@/enums/store";
import IFMenuItem from "@/interfaces/menu";
import { computed, defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

export default defineComponent({
  setup() {
    const store = useStore();
    const router = useRouter();
    const tableIndex = router.currentRoute.value.params.index as string;
    const table = store.getters[ESTable.G_TABLE](parseInt(tableIndex));
    const orderItemPreviewList = computed(() =>
      store.getters[ESOrderItem.G_ORDER_PREVIEW_LIST](table)
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
        items: orderItemPreviewList.value,
      });
    }
    return { orderItemPreviewList, orderedItemList, handleSelect, order };
  },
  components: { CTableOverview, CTableOrder },
});
</script>

<style lang="scss" scoped>
.wrap {
  gap: var(--s-large);
}
</style>
