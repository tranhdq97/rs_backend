import { IFCustomer } from "@/interfaces/customer";
import { IFTable } from "@/interfaces/tables";

export interface IFState {
  customerList: IFCustomer[];
}

export default {
  namespaced: true,
  state: {
    customerList: [],
  } as IFState,
  getters: {
    customerList: (state: IFState) => state.customerList,
    tableCustomer: (state: IFState) => (table: IFTable) => {
      return state.customerList.find(
        (item: IFCustomer) => item?.table?.id === table.id
      );
    },
  },
  actions: {
    async addCustomer(
      { state }: { state: IFState },
      params: { customer: IFCustomer; table: IFTable }
    ) {
      return null;
    },
  },
  mutations: {
    removeCustomer(state: IFState, customer: IFCustomer) {
      const index = state.customerList.indexOf(customer);
      if (index > -1) {
        state.customerList.splice(index, 1);
      }
    },
    addCustomer(state: IFState, customer: IFCustomer) {
      state.customerList.push(customer);
    },
  },
};
