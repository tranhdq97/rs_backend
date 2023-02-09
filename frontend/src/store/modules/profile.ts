import authAxios from "@/axios";
import { EAProfile } from "@/enums/api";
import { IFProfile } from "@/interfaces/common";

export interface IFState {
  customerList: IFProfile[];
}

export default {
  namespaced: true,
  state: {},
  actions: {
    async addProfile({ state }: { state: IFState }, phoneNumber: string) {
      const res: IFProfile = await authAxios.post(EAProfile.CREATE, {
        phone_number: phoneNumber,
      });
      return res;
    },
  },
  mutations: {
    removeCustomer(state: IFState, customer: IFProfile) {
      const index = state.customerList.indexOf(customer);
      if (index > -1) {
        state.customerList.splice(index, 1);
      }
    },
    addCustomer(state: IFState, customer: IFProfile) {
      state.customerList.push(customer);
    },
  },
};
