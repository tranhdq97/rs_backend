import { IFOrder } from "@/interfaces/order";
import { IFTable } from "@/interfaces/tables";

export interface IFState {
  // not have paid_at
  orderList: Array<IFOrder>;
}

export default {
  namespaced: true,
  state: {
    orderList: [],
  } as IFState,
  getters: {
    orderList: (state: IFState) => state.orderList,
    order: (state: IFState) => (order: IFOrder) => {
      return state.orderList.find((item: IFOrder) => item.id === order.id);
    },
    orderByTable: (state: IFState) => (table: IFTable) => {
      return state.orderList.find((item) => item.table.id === table.id);
    },
  },
  actions: {
    async addOrder({ state }: { state: IFState }, order: IFOrder) {
      // Call add Order API
      let existedOrder = state.orderList.find(
        (item: IFOrder) => item.id === order.id
      );
      if (!existedOrder) {
        state.orderList.push(order);
        existedOrder = order;
      }
      return existedOrder;
    },
  },
  mutations: {
    removePaidOrder(state: IFState, order: IFOrder) {
      const index = state.orderList.indexOf(order);
      index > -1 ? state.orderList.splice(index, 1) : null;
    },
  },
};
