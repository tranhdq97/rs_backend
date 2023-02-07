import authAxios from "@/axios";
import { EACustomer } from "@/enums/api";
import { EPCommon } from "@/enums/params";
import { IAListRes } from "@/interfaces/api";
import { IFCustomer } from "@/interfaces/customer";
import { IFTable } from "@/interfaces/tables";
import { formURL } from "@/utils/url";
import { EOCustomer } from "@/enums/ordering";

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
    async searchCustomerByPhoneNumber(
      { state }: { state: IFState },
      phoneNumber: string
    ) {
      const URL = formURL(
        EACustomer.LIST,
        [],
        [
          { key: EPCommon.SEARCH, value: phoneNumber },
          { key: EPCommon.PAGE_SIZE, value: 20 },
          { key: EPCommon.PAGE, value: 1 },
          { key: EPCommon.ORDERING, value: EOCustomer.PROFILE__PHONE_NUMBER },
        ]
      );
      const res: IAListRes = await authAxios.get(URL);
      return res.results as IFCustomer[];
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
