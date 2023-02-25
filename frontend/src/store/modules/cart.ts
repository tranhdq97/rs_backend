import { IFMenuItem } from "@/interfaces/menu";

export interface IFState {
  menuList: IFMenuItem[];
}

export default {
  namespaced: true,
  state: {
    menuList: [],
  } as IFState,
  getters: {
    isInCart: (state: IFState) => (menuID: number) =>
      state.menuList.find((item) => item?.id === menuID),
  },
  actions: {},
};
