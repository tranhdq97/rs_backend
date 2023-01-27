import axios from "axios";
import { EAAuth, EAStaff } from "@/enums/api";
import { EToken } from "@/enums/common";
import { IFToken } from "@/interfaces/common";
import { IFStaff } from "@/interfaces/staff";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();

export interface IFState {
  user: IFStaff | null;
}

export default {
  namespaced: true,
  state: {
    user: null,
  } as IFState,
  getters: {},
  actions: {
    async signUp({ state }: { state: IFState }, user: IFStaff) {
      await axios.post(EAStaff.CREATE, user);
    },
    async signIn({ state }: { state: IFState }, user: IFStaff) {
      const res: IFToken = await axios.post(EAAuth.TOKEN, user);
      cookies.set(EToken.ACCESS, res.access);
      cookies.set(EToken.REFRESH, res.refresh);
    },
    signOut() {
      cookies.remove(EToken.ACCESS);
      cookies.remove(EToken.REFRESH);
    },
    async refreshToken() {
      return;
    },
    async getMe() {
      return;
    },
  },
};
