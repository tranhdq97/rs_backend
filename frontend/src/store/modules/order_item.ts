import authAxios from "@/axios";
import { EAOrder, EAOrderItem } from "@/enums/api";
import { ESAuth, ESOrder, ESOrderItem, ESTable } from "@/enums/store";
import { IFCustomer } from "@/interfaces/customer";
import { IFMenuItem } from "@/interfaces/menu";
import { IFOrderItem, IFOrder } from "@/interfaces/order";
import { IFStaff } from "@/interfaces/staff";
import { IFTable, IFTableRep } from "@/interfaces/tables";
import { formURL } from "@/utils/url";
import { ERouterParams } from "@/enums/common";
import { Commit, Dispatch } from "vuex";
import { EPCommon, EPOrderItem } from "@/enums/params";
import { concatProperty } from "@/utils/common";
import { IAListRes } from "@/interfaces/api";

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
        (item) => item?.table?.id === table.id && !item.updated_at
      );
    },
    orderedItemList: (state: IFState) => (table: IFTable) => {
      return state.orderItemList.filter(
        (item) => item?.table?.id === table.id && item.updated_at
      );
    },
    tableRepData: (state: IFState) => (table: IFTable) => {
      let lastServedAt: Date = null as unknown as Date;
      let newestOrderedAt: Date = null as unknown as Date;
      let numServed = 0;
      let numOrders = 0;
      let phoneNumer = undefined;
      state.orderItemList
        .filter((item) => {
          return item?.table?.id === table.id && item.order;
        })
        .map((item, i) => {
          if (i === 0) {
            phoneNumer = item.order?.customer?.profile?.phone_number;
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
      // eslint-disable-next-line
      //@ts-ignore
      { state, rootGetters },
      params: {
        menu: IFMenuItem;
        table: IFTable;
        order?: IFOrder;
      }
    ) {
      if (
        state.orderItemList.some(
          (item: IFOrderItem) =>
            item.menu.id === params.menu.id &&
            item.table === params.table &&
            !item.created_at
        )
      )
        return;
      const staff: IFStaff = rootGetters[ESAuth.G_USER];
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
    async getOrderItems({ state }: { state: IFState }, orders: IFOrder[]) {
      if (!orders.length) {
        state.orderItemList = [];
        return;
      }
      const orderIDs = concatProperty(orders, EPCommon.ID, ",");
      const URL = formURL(
        EAOrderItem.LIST,
        [],
        [{ key: EPOrderItem.ORDER_ID__IN, value: orderIDs }]
      );
      const res: IAListRes = await authAxios.get(URL);
      state.orderItemList = res.results as IFOrderItem[];
      state.orderItemList.map((item) => {
        if (item.order) {
          item.table = item.order?.table;
        }
      });
    },
    async order(
      {
        state,
        commit,
        dispatch,
      }: { state: IFState; commit: Commit; dispatch: Dispatch },
      params: {
        table: IFTable;
        items: IFOrderItem[];
        tableOrder?: IFOrder;
        customer?: IFCustomer;
      }
    ) {
      let table: IFTable = params.table;
      let tableOrder = params.tableOrder;
      if (table.is_available) {
        table = await dispatch(
          ESTable.A_UPDATE_TABLE,
          {
            table: params.table,
            updateData: { is_available: false },
          },
          { root: true }
        );
      }
      if (!params.tableOrder) {
        const newOrder: IFOrder = { table_id: table.id, num_people: 1 };
        if (params.customer) newOrder.customer_id = params.customer.id;
        tableOrder = await dispatch(ESOrder.A_ADD_ORDER, newOrder, {
          root: true,
        });
      }
      params.items.map(async (newOrder: IFOrderItem) => {
        const orderItems = state.orderItemList.filter(
          (item) =>
            item?.table?.id === table.id &&
            item.menu.name === newOrder.menu.name
        ) as IFOrderItem[];
        const previewItem = orderItems.find((item: IFOrderItem) => !item.order);
        const orderedItem = orderItems.find((item: IFOrderItem) => item.order);
        if (orderedItem && previewItem) {
          const updateURL = formURL(EAOrderItem.UPDATE, [
            { key: ERouterParams.INDEX, value: orderedItem.id },
          ]);
          const res: IFOrderItem = await authAxios.put(updateURL, {
            quantity: orderedItem.quantity + previewItem.quantity,
          });
          orderedItem.quantity = res.quantity;
          orderedItem.updated_at = new Date(res.updated_at as string);
          commit(ESOrderItem.M_REMOVE_ORDER_ITEM, previewItem, {
            root: true,
          });
        } else if (!orderedItem && previewItem) {
          const res: IFOrderItem = await authAxios.post(EAOrderItem.CREATE, {
            quantity: previewItem.quantity,
            order_id: tableOrder?.id,
            menu_id: previewItem.menu.id,
          });
          previewItem.id = res.id;
          previewItem.order = res.order;
          previewItem.table = table;
          previewItem.served_quantity = res.served_quantity;
          previewItem.created_at = new Date(res.created_at as string);
          previewItem.updated_at = new Date(res.updated_at as string);
        }
      });
    },
    async serve(
      { state }: { state: IFState },
      params: { item: IFOrderItem; serveQuantity: number }
    ) {
      const URL = formURL(EAOrderItem.UPDATE, [
        { key: ERouterParams.INDEX, value: params.item.id },
      ]);
      const res: IFOrderItem = await authAxios.put(URL, {
        served_quantity:
          (params.item?.served_quantity || 0) + params.serveQuantity,
        served_at: new Date(Date.now()).toISOString(),
      });
      params.item.served_quantity = res.served_quantity;
      params.item.served_at = new Date(res.served_at as string);
    },
    async pay(
      {
        state,
        commit,
        dispatch,
      }: { state: IFState; commit: Commit; dispatch: Dispatch },
      params: {
        order: IFOrder;
        orderItems: IFOrderItem[];
      }
    ) {
      params.orderItems.map((item) =>
        commit(ESOrderItem.M_REMOVE_ORDER_ITEM, item, { root: true })
      );
      const URL = formURL(EAOrder.UPDATE, [
        { key: ERouterParams.INDEX, value: params.order.id },
      ]);
      await authAxios.put(URL, {
        paid_at: new Date(Date.now()).toISOString(),
      });
      await dispatch(
        ESTable.A_UPDATE_TABLE,
        {
          table: params.order.table,
          updateData: { is_availabel: true },
        },
        { root: true }
      );
      commit(ESOrder.M_REMOVE_ORDER, params.order, { root: true });
    },
  },
  mutations: {
    removeOrderItem(state: IFState, item: IFOrderItem) {
      const index = state.orderItemList.indexOf(item);
      index > -1 ? state.orderItemList.splice(index, 1) : null;
    },
  },
};
