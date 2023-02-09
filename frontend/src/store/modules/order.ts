import authAxios from "@/axios";
import { EAOrder } from "@/enums/api";
import { ERouterParams } from "@/enums/common";
import { EPCommon, EPOrder } from "@/enums/params";
import { IAListRes } from "@/interfaces/api";
import { IFOrder } from "@/interfaces/order";
import { IFTable } from "@/interfaces/tables";
import { concatProperty } from "@/utils/common";
import { formURL } from "@/utils/url";

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
      return state.orderList.find(
        (item) => item?.table?.id === table.id && !item.paid_at
      );
    },
  },
  actions: {
    async addOrder({ state }: { state: IFState }, order: IFOrder) {
      const res: IFOrder = await authAxios.post(EAOrder.CREATE, order);
      state.orderList.push(res);
      return res;
    },
    async getOrders({ state }: { state: IFState }, tables: IFTable[]) {
      if (!tables?.length) return state.orderList;
      const tableIDs = concatProperty(tables, EPCommon.ID, ",");
      const URL = formURL(
        EAOrder.LIST,
        [],
        [{ key: EPOrder.TABLE_ID__IN, value: tableIDs }]
      );
      const res: IAListRes = await authAxios.get(URL);
      state.orderList = res.results as Array<IFOrder>;
      return state.orderList;
    },
    async updateOrder(
      { state }: { state: IFState },
      params: { order: IFOrder; updateData: IFOrder }
    ) {
      console.log("ININI");
      const URL = formURL(EAOrder.UPDATE, [
        { key: ERouterParams.INDEX, value: params.order.id },
      ]);
      const res: IFOrder = await authAxios.put(URL, params.updateData);
      params.order = { ...res };
      return params.order;
    },
  },
  mutations: {
    removeOrder(state: IFState, order: IFOrder) {
      const index = state.orderList.indexOf(order);
      index > -1 ? state.orderList.splice(index, 1) : null;
    },
  },
};
