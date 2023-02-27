<script lang="ts">
import { ECommon } from "@/enums/common";
import { ERouter } from "@/enums/routers";
import { ESBill, ESOrderItem } from "@/enums/store";
import { IFOrderItem } from "@/interfaces/order";
import LAModal from "@/layouts/LAModal.vue";
import router from "@/router";
import { sumProperty, toExchange } from "@/utils/common";
import { computed, defineComponent, ref } from "vue";
import { useStore } from "vuex";
import CButton from "./CButton.vue";
import COrder from "./COrder.vue";
import COrderServe from "./COrderServe.vue";

export default defineComponent({
  props: {
    table: { type: Object, required: true },
    order: { type: Object, required: false },
    customer: { type: Object, required: false },
    orderedItemList: { type: Array, default: [] as IFOrderItem[] },
  },
  setup(props) {
    const store = useStore();
    const isServing = ref(false);
    const VAT = computed(() => store.getters[ESBill.G_VAT]);
    const modal = ref<IFOrderItem | null>();
    const total_quantity = computed(() =>
      sumProperty(props.orderedItemList, ["quantity"])
    );
    const total_served = computed(() =>
      sumProperty(props.orderedItemList, ["served_quantity"])
    );
    const amount = computed(() => {
      let sum = 0;
      (props.orderedItemList as IFOrderItem[]).map((item) => {
        sum += (item?.served_quantity || 0) * (item.menu?.price || 0);
      });
      return sum;
    });
    const serve = (item: IFOrderItem) => {
      isServing.value = true;
      modal.value = item;
    };
    async function serveSubmit(item: IFOrderItem, serveQuantity: number) {
      await store.dispatch(ESOrderItem.A_SERVE, {
        item: item,
        serveQuantity: serveQuantity,
      });
      isServing.value = false;
    }
    async function payBill() {
      await store.dispatch(ESOrderItem.A_PAY, {
        order: props.order,
        customer: props.customer,
        orderItems: props.orderedItemList,
      });
      router.push(ERouter.TABLES);
    }
    return {
      ECommon,
      total_quantity,
      total_served,
      amount,
      isServing,
      modal,
      VAT,
      serve,
      serveSubmit,
      toExchange,
      payBill,
    };
  },
  components: { COrder, LAModal, COrderServe, CButton },
});
</script>

<template>
  <div class="container area">
    <table>
      <thead>
        <tr>
          <th>{{ $t(ECommon.MEAL_NAME) }}</th>
          <th>{{ $t(ECommon.QUANTITY) }}</th>
          <th>{{ $t(ECommon.SERVED) }}</th>
          <th class="mobile-hidden">{{ $t(ECommon.UNIT_PRICE) }}</th>
          <th>{{ $t(ECommon.ORDERED_AT) }}</th>
          <th>{{ $t(ECommon.SERVED_AT) }}</th>
          <th class="mobile-hidden">{{ $t(ECommon.TOTAL) }}</th>
        </tr>
      </thead>
      <tbody>
        <COrder
          v-for="(item, i) in orderedItemList"
          :key="i"
          :item="item || {}"
          @serve="serve(item as IFOrderItem)"
        />
      </tbody>
      <tfoot v-if="orderedItemList.length">
        <tr>
          <td class="padding">{{ $t(ECommon.AMOUNT) }}</td>
          <td class="text-center padding">{{ total_quantity }}</td>
          <td class="text-center padding">{{ total_served }}</td>
          <td v-for="i in 3" :key="i" class="mobile-hidden"></td>
          <td class="text-right padding mobile-hidden">
            {{ toExchange(amount) }}
          </td>
        </tr>
        <tr>
          <td class="padding">{{ $t(ECommon.VAT) }}</td>
          <td v-for="i in 5" :key="i" class="mobile-hidden"></td>
          <td class="text-right padding mobile-hidden">
            ({{ VAT }}%) {{ toExchange((amount * VAT) / 100) }}
          </td>
        </tr>
        <tr>
          <td>{{ $t(ECommon.TOTAL) }}</td>
          <td v-for="i in 5" :key="i" class="mobile-hidden"></td>
          <td class="text-right mobile-hidden">
            {{ toExchange(amount * (1 + VAT / 100)) }}
          </td>
        </tr>
      </tfoot>
    </table>
    <div class="paybill" v-if="order">
      <CButton :name="ECommon.PAY_BILL" @click="payBill" />
      <span class="material-icons preview">preview</span>
    </div>
    <LAModal v-if="isServing" @close="isServing = false">
      <COrderServe
        :data="modal || {}"
        @serveSubmit="
          (payload) => serveSubmit(payload.item, payload.serveQuantity)
        "
      />
    </LAModal>
  </div>
</template>

<style lang="scss" scoped>
.container {
  overflow-y: auto;
  justify-content: flex-start;
  gap: var(--s-small);
}
table {
  gap: var(--s-small);
}
thead {
  background: var(--c-primary);
  color: var(--c-white);
  th {
    padding: var(--s-small);
    font-weight: var(--fw-small);
  }
}
.padding {
  padding-top: var(--s-large);
}
.paybill {
  width: 100%;
  align-items: center;
}
.preview {
  margin-left: var(--s-medium);
  border-radius: var(--br-small);
  border: 1px solid var(--c-text);
  font-size: var(--fs-large);
  font-weight: var(--fw-small);
  &:hover {
    border: 1px solid var(--c-primary);
    color: var(--c-primary);
  }
}
@media screen and (max-width: 480px) {
  .mobile-hidden {
    visibility: hidden;
    display: none;
  }
}
</style>
