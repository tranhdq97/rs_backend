import authAxios from "@/axios";
import { EAMenu } from "@/enums/api";
import { IAListRes } from "@/interfaces/api";
import { IFMenuItem } from "@/interfaces/menu";
import axios from "axios";

export interface IFState {
  menu: Array<IFMenuItem>;
}

export default {
  namespaced: true,
  state: {
    menu: [],
  },
  getters: {
    menu: (state: IFState) => state.menu,
    availableMenu: (state: IFState) =>
      state.menu.filter((item) => item.is_available),
  },
  actions: {
    async getMenu({ state }: { state: IFState }) {
      const res: IAListRes = await axios.get(EAMenu.LIST);
      state.menu = res.results as IFMenuItem[];
    },
    async addMeal({ state }: { state: IFState }, meal: IFMenuItem) {
      const res: IFMenuItem = await authAxios.post(EAMenu.CREATE, meal);
      state.menu.push(res);
    },
  },
};
