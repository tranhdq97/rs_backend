import { ESAuth, ESOrder, ESOrderItem } from "@/enums/store";
import { IFMenuItem } from "@/interfaces/menu";
import { IFOrderItem, IFOrder } from "@/interfaces/order";
import { IFStaff } from "@/interfaces/staff";
import { IFTable, IFTableRep } from "@/interfaces/tables";
import { Commit, Dispatch } from "vuex";
import auth from "./auth";

export interface IFState {
  orderItemList: Array<IFOrderItem>;
}

export default {
  namespaced: true,
  state: {
    orderItemList: [],
  },
  getters: {
    orderItemPreviewList: (state: IFState) => (table: IFTable) => {
      return state.orderItemList.filter(
        (item) => item.table.id === table.id && !item.updated_at
      );
    },
    orderedItemList: (state: IFState) => (table: IFTable) => {
      return state.orderItemList.filter(
        (item) => item.table.id === table.id && item.updated_at
      );
    },
    tableRepData: (state: IFState) => (table: IFTable) => {
      let lastServedAt: Date = null as unknown as Date;
      let newestOrderedAt: Date = null as unknown as Date;
      let numServed = 0;
      let numOrders = 0;
      let phoneNumer = undefined;
      state.orderItemList
        .filter((item) => item.table.id === table.id && item.order)
        .map((item, i) => {
          if (i === 0) {
            phoneNumer = item.order?.customer?.profile.phone_number;
          }
          if (item.served_at) {
            if (lastServedAt) {
              lastServedAt = new Date(
                item.served_at > lastServedAt ? item.served_at : lastServedAt
              );
            } else {
              lastServedAt = new Date(item.served_at);
            }
          }
          if (item.updated_at) {
            if (newestOrderedAt) {
              newestOrderedAt = new Date(
                item.updated_at > newestOrderedAt
                  ? item.updated_at
                  : newestOrderedAt
              );
            } else {
              newestOrderedAt = new Date(item.updated_at);
            }
          }
          numServed += item.served_quantity ? item.served_quantity : 0;
          numOrders += item.quantity;
        });

      const tableRepData: IFTableRep = {
        phoneNumber: phoneNumer,
        lastServedAt: lastServedAt,
        newestOrderedAt: newestOrderedAt,
        numOrders: numOrders,
        numServed: numServed,
      };
      return tableRepData;
    },
  },
  actions: {
    addToOrderPreview(
      { state, rootGetters }: { state: IFState; rootGetters: any },
      params: {
        menu: IFMenuItem;
        table: IFTable;
        order?: IFOrder;
      }
    ) {
      if (
        state.orderItemList.some(
          (item) =>
            item.menu.id === params.menu.id &&
            item.table === params.table &&
            !item.created_at
        )
      )
        return;
      // Mock staff
      const staff = auth.getters.user;
      console.log("STAFF", staff);
      const newOrderItem = {
        order: params?.order,
        menu: params.menu,
        staff: staff,
        quantity: 1,
        table: params.table,
      };
      state.orderItemList.push(newOrderItem);
    },
    increaseQuantity({ state }: { state: IFState }, item: IFOrderItem) {
      item.quantity += 1;
    },
    decreaseQuantity({ state }: { state: IFState }, item: IFOrderItem) {
      item.quantity -= 1;
    },
    async order(
      {
        state,
        commit,
        dispatch,
      }: { state: IFState; commit: Commit; dispatch: Dispatch },
      params: { table: IFTable; items: IFOrderItem[] }
    ) {
      params.table.is_available = false;
      // Mock order
      const order = await dispatch(
        ESOrder.A_ADD_ORDER,
        {
          id: 1,
          table: params.table,
        },
        { root: true }
      );
      // Mock response
      params.items.map((newOrder: IFOrderItem) => {
        const orderItems = state.orderItemList.filter(
          (item) =>
            item.table === params.table && item.menu.name === newOrder.menu.name
        ) as IFOrderItem[];
        const previewItem = orderItems.find((item: IFOrderItem) => !item.order);
        const orderedItem = orderItems.find((item: IFOrderItem) => item.order);
        if (orderedItem && previewItem) {
          orderedItem.quantity += previewItem.quantity;
          orderedItem.updated_at = new Date(Date.now());
          commit(ESOrderItem.M_REMOVE_ORDER_ITEM, previewItem, {
            root: true,
          });
        } else if (!orderedItem && previewItem) {
          previewItem.order = order;
          previewItem.table = params.table;
          previewItem.served_quantity = 0;
          previewItem.created_at = new Date(Date.now());
          previewItem.updated_at = new Date(Date.now());
        }
      });
    },
    async serve(
      { state }: { state: IFState },
      params: { item: IFOrderItem; serveQuantity: number }
    ) {
      // Mock successed api call
      if (params.item.served_quantity !== undefined) {
        params.item.served_quantity += params.serveQuantity;
      } else params.item.served_quantity = 0;
      params.item.served_at = new Date(Date.now());
    },
  },
  mutations: {
    removeOrderItem(state: IFState, item: IFOrderItem) {
      const index = state.orderItemList.indexOf(item);
      index > -1 ? state.orderItemList.splice(index, 1) : null;
    },
  },
};
