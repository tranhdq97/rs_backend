import { IFMasterData, IFProfile } from "./common";

export interface IFStaff {
  id?: number;
  role?: IFMasterData;
  email: string;
  password?: string;
  profile?: IFProfile;
}
