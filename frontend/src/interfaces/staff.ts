import { IFMasterData, IFProfile } from "./common";

export interface IFStaff {
  id?: number;
  type?: IFMasterData;
  email: string;
  password?: string;
  profile?: IFProfile;
}
