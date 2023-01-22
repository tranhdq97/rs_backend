import { IFMasterData, IFProfile } from "./common";

export default interface IFStaff {
  id: number;
  role: IFMasterData;
  email: string;
  password?: string;
  profile?: IFProfile;
}
