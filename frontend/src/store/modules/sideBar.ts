export interface IFstate {
  isSideBarHide: boolean;
  isSideBarCollapsed: boolean;
}

export default {
  namespaced: true,
  state: {
    isSideBarHide: false,
    isSideBarCollapsed: true,
  },
  getters: {
    isSideBarCollapsed: (state: IFstate) => state.isSideBarCollapsed,
  },
  actions: {
    toggleSideBar({ state }: { state: IFstate }) {
      state.isSideBarCollapsed = !state.isSideBarCollapsed;
    },
    collapseSideBar({ state }: { state: IFstate }) {
      state.isSideBarCollapsed = true;
    },
  },
};
