<script lang="ts">
import { ECommon } from "@/enums/common";
import { ESCustomer, ESMenu } from "@/enums/store";
import { IFMasterData } from "@/interfaces/common";
import { IFCustomer } from "@/interfaces/customer";
import { computed, defineComponent, ref } from "vue";
import { useStore } from "vuex";
import CButton from "./CButton.vue";
import CPreOrder from "./CPreOrder.vue";
import CSearchField from "./CSearchField.vue";
import CTableCustomerInfo from "./CTableCustomerInfo.vue";

export default defineComponent({
  props: {
    orderItemPreviewList: { type: Array, default: () => [] },
    table: { type: Object, required: true },
    order: { type: Object, required: false },
  },
  emits: ["handleSelect", "handleOrder"],
  setup(props) {
    const store = useStore();
    const phoneNumber = ref(
      props?.order?.customer?.profile?.phone_number || ""
    );
    const firstName = ref(props?.order?.customer?.profile?.firstname || "");
    const lastName = ref(props?.order?.customer?.profile?.lastName || "");
    const numPeople = ref(props?.order?.num_people?.toString() || "0");
    const searchData = computed(() => store.getters[ESMenu.G_AVAILABLE_MENU]);
    const customer = ref<IFCustomer | null>();
    const customers = ref<IFCustomer[]>([]);
    const customerList = computed(() => {
      const data: IFMasterData[] = [];
      customers.value.map((item) =>
        data.push({
          id: item.id,
          name:
            item?.profile?.phone_number +
            " - " +
            item?.profile?.first_name +
            " " +
            item?.profile?.last_name,
        })
      );
      return data;
    });
    async function searchCustomer(val: string) {
      phoneNumber.value = val;
      let res: IFCustomer[] = [];
      if (val.length) {
        res = await store.dispatch(ESCustomer.A_SEARCH_CUSTOMER_BY_PN, val);
      }
      customers.value = res;
    }
    return {
      ECommon,
      searchData,
      phoneNumber,
      firstName,
      lastName,
      numPeople,
      customer,
      customers,
      customerList,
      searchCustomer,
    };
  },
  components: { CSearchField, CPreOrder, CButton, CTableCustomerInfo },
});
</script>

<template>
  <div class="container area">
    <div class="head-info">
      <span class="material-icons">table_restaurant</span>
      <div>{{ table.name }}</div>
    </div>
    <div class="head-info">
      <CTableCustomerInfo
        icon="contact_phone"
        :content="phoneNumber"
        :contentList="customerList"
        :placeHolder="$t(ECommon.PHONE_NUMBER)"
        actionIcon="add"
        @change="(content) => searchCustomer(content.value)"
      />
      <CTableCustomerInfo
        icon="badge"
        :content="lastName"
        :placeHolder="$t(ECommon.LASTNAME)"
        :isDisabled="!customer"
        @change="(content) => (lastName = content.value)"
      />
      <CTableCustomerInfo
        :content="firstName"
        :placeHolder="$t(ECommon.FIRSTNAME)"
        :isDisabled="!customer"
        @change="(content) => (firstName = content.value)"
      />
      <CTableCustomerInfo
        icon="groups"
        type="number"
        :content="numPeople"
        :placeHolder="$t(ECommon.NUM_PEOPLE)"
        @change="(content) => (numPeople = content.value)"
      />
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
.pre-order {
  gap: var(--s-small);
  overflow-y: auto;
  max-height: 300px;
}
.search {
  justify-content: stretch;
}
</style>
