import { IFProfile } from "./common";
import { IFTable } from "./tables";

export interface IFCustomer {
  id?: number;
  profile?: IFProfile;
  table?: IFTable;
}
