import { IFMenuItem } from "@/interfaces/menu";

export interface IFState {
  menu: Array<IFMenuItem>;
}

export default {
  namespaced: true,
  state: {
    menu: [
      {
        id: 1,
        name: "bo keo phao con heo ga vit",
        type: {
          id: 1,
          name: "main cource",
        },
        price: 100000,
        is_available: true,
      },
      {
        id: 2,
        name: "bo cong kenh",
        type: {
          id: 1,
          name: "main cource",
        },
        price: 130000,
        is_available: true,
      },
      {
        id: 3,
        name: "bo keo keo",
        type: {
          id: 1,
          name: "main cource",
        },
        price: 90000,
        is_available: true,
      },
      {
        id: 4,
        name: "bo an chay",
        type: {
          id: 1,
          name: "main cource",
        },
        price: 124000,
        is_available: false,
      },
    ],
  },
  getters: {
    menu: (state: IFState) => state.menu,
    availableMenu: (state: IFState) =>
      state.menu.filter((item) => item.is_available),
  },
};
