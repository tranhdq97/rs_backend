<script lang="ts">
import { ECommon } from "@/enums/common";
import {
  ESAuth,
  ESCustomer,
  ESMenu,
  ESOrder,
  ESOrderItem,
} from "@/enums/store";
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
    customer: { type: Object, required: false },
  },
  emits: ["handleSelect"],
  setup(props) {
    const store = useStore();
    const staff = computed(() => store.getters[ESAuth.G_USER]);
    const phoneNumber = ref(props?.customer?.profile?.phone_number || "");
    const firstName = ref(props?.customer?.profile?.first_name || "");
    const lastName = ref(props?.customer?.profile?.last_name || "");
    const numPeople = ref<number>(props?.order?.num_people || 0);
    const searchData = computed(() => store.getters[ESMenu.G_AVAILABLE_MENU]);
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
    async function selectCustomer(item: IFMasterData) {
      const selectedCustomer: IFCustomer | null = customers.value.find(
        (cus) => cus.id === item.id
      ) as IFCustomer;
      if (selectedCustomer) {
        const res = await store.dispatch(ESOrder.A_UPDATE_ORDER, {
          order: props.order,
          updateData: { customer_id: selectedCustomer.id },
        });
        phoneNumber.value = res?.customer?.profile?.phone_number || "";
        firstName.value = res?.customer?.profile?.first_name || "";
        lastName.value = res?.customer?.profile?.last_name || "";
      }
    }
    async function addPhoneNumber() {
      await store.dispatch(ESCustomer.A_ADD_PHONE_NUMBER, {
        order: props.order,
        phoneNumber: phoneNumber.value,
      });
    }
    async function updateLastName() {
      await store.dispatch(ESCustomer.A_UPDATE_CUSTOMER, {
        customer: props?.customer,
        updateData: { profile: { last_name: lastName.value } },
      });
    }
    async function updateFirstName() {
      await store.dispatch(ESCustomer.A_UPDATE_CUSTOMER, {
        customer: props?.customer,
        updateData: { profile: { first_name: firstName.value } },
      });
    }
    async function updateNumPeople() {
      if (!props.order) {
        await store.dispatch(ESOrder.A_ADD_ORDER, {
          table_id: props.table.id,
          num_people: numPeople.value,
        });
      } else {
        await store.dispatch(ESOrder.A_UPDATE_ORDER, {
          order: props.order,
          updateData: { num_people: numPeople.value },
        });
      }
    }
    async function handleOrder() {
      await store.dispatch(ESOrderItem.A_ORDER, {
        table: props.table,
        tableOrder: props.order,
        items: props.orderItemPreviewList,
        customer: props.customer,
        staff: staff.value,
      });
    }
    return {
      staff,
      ECommon,
      searchData,
      phoneNumber,
      firstName,
      lastName,
      numPeople,
      customers,
      customerList,
      searchCustomer,
      selectCustomer,
      addPhoneNumber,
      updateLastName,
      updateFirstName,
      updateNumPeople,
      handleOrder,
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
    <div class="head-info info-detail">
      <CTableCustomerInfo
        icon="contact_phone"
        :content="phoneNumber"
        :contentList="customerList"
        :placeHolder="$t(ECommon.PHONE_NUMBER)"
        actionIcon="add"
        @change="(content) => searchCustomer(content.value)"
        @selectCustomer="(item) => selectCustomer(item)"
        @addInfo="addPhoneNumber"
        :isDisabled="!order"
      />
      <div class="name">
        <CTableCustomerInfo
          icon="badge"
          :content="firstName"
          :placeHolder="$t(ECommon.FIRSTNAME)"
          :isDisabled="!customer"
          @change="(content) => (firstName = content.value)"
          @addInfo="updateFirstName"
        />
        <CTableCustomerInfo
          :content="lastName"
          :placeHolder="$t(ECommon.LASTNAME)"
          :isDisabled="!customer"
          @change="(content) => (lastName = content.value)"
          @addInfo="updateLastName"
        />
      </div>
      <CTableCustomerInfo
        icon="groups"
        type="number"
        :content="numPeople.toString()"
        :placeHolder="$t(ECommon.NUM_PEOPLE)"
        min="0"
        @change="(content) => (numPeople = parseInt(content.value))"
        @addInfo="updateNumPeople"
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
      @click="handleOrder"
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
.name {
  gap: var(--s-small);
}
@media screen and (max-width: 480px) {
  .info-detail {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
