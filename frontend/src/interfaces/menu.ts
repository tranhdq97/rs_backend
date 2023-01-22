import { IFMasterData } from "./common";

export default interface IFMenuItem {
  id: number;
  name: string;
  type: IFMasterData;
  price: number;
  is_available: boolean;
}
