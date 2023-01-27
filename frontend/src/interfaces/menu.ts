import { IFMasterData } from "./common";

export interface IFMenuItem {
  id: number;
  name: string;
  type: IFMasterData;
  price: number;
  is_available: boolean;
}
