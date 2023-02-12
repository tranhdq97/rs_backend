import authAxios from "@/axios";
import { EACustomer } from "@/enums/api";
import { EPCommon } from "@/enums/params";
import { IAListRes } from "@/interfaces/api";
import { IFCustomer } from "@/interfaces/customer";
import { IFTable } from "@/interfaces/tables";
import { formURL } from "@/utils/url";
import { EOCustomer } from "@/enums/ordering";
import { ERouterParams } from "@/enums/common";

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
    async addPhoneNumber({ state }: { state: IFState }, phoneNumber: string) {
      const customer: IFCustomer = await authAxios.post(EACustomer.CREATE, {
        profile: { phone_number: phoneNumber },
      });
      state.customerList.push(customer);
      return customer;
    },
    async updateCustomer(
      { state }: { state: IFState },
      params: { customer: IFCustomer; updateData: IFCustomer }
    ) {
      const URL = formURL(EACustomer.UPDATE, [
        { key: ERouterParams.INDEX, value: params.customer.id },
      ]);
      await authAxios.put(URL, params.updateData);
      params.customer = { ...params.customer, ...params.updateData };
      return params.customer;
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
    update(state: IFState, customer: IFCustomer) {
      const updatingCustomer = state.customerList.find(
        (item) => customer.id === item?.id
      );
      if (updatingCustomer) {
        updatingCustomer.num_people = customer.num_people;
        updatingCustomer.paid_at = customer.paid_at;
        updatingCustomer.table = customer.table;
        updatingCustomer.customer = customer.customer;
      }
    }
  },
};
