import { ERouterParams, EMasterModel } from "@/enums/common";
import { IAListRes } from "@/interfaces/api";
import { IFMasterData } from "@/interfaces/common";
import { formURL } from "@/utils/url";
import { EAMaster } from "@/enums/api";
import axios from "axios";

export interface IFState {
  typeList: IFMasterData[];
}

export default {
  namespaced: true,
  state: {
    typeList: [],
  } as IFState,
  getters: {
    menuTypes: (state: IFState) => state.typeList,
  },
  actions: {
    async getMenuTypes({ state }: { state: IFState }) {
      const URL = formURL(EAMaster.LIST, [
        { key: ERouterParams.MASTER_NAME, value: EMasterModel.MENU_TYPE },
      ]);
      const res: IAListRes = await axios.get(URL);
      state.typeList = res.results as IFMasterData[];
    },
  },
};
