import { IFTable } from "@/interfaces/tables";

export interface IFState {
  tables: Array<IFTable>;
}

export default {
  namespaced: true,
  state: {
    tables: [],
  } as IFState,
  getters: {
    tables: (state: IFState) => state.tables,
    table: (state: IFState) => (id: number) =>
      state.tables.find((table) => table.id === id),
  },
  actions: {
    async addTable({ state }: { state: IFState }) {
      const listLength = state.tables.length;
      // Mock api
      const table: IFTable = {
        id: listLength,
        name: (listLength + 1).toString(),
        is_available: true,
      };
      state.tables.push(table);
    },
  },
};
