export interface IFSearchItem {
  id: number;
  name?: string;
}

export interface IFMasterData {
  id: number;
  name?: string;
}

export interface IFCity {
  id: number;
  country?: IFMasterData;
}

export interface IFDistrict {
  id: number;
  zipcode?: string;
  city: IFCity;
}

export interface IFAddress {
  id: number;
  district: IFDistrict;
  street?: string;
}

export interface IFProfile {
  id: number;
  phone_number: string;
  firstname?: string;
  lastname?: string;
  dob?: Date;
  address?: IFAddress;
}

export interface IFToken {
  access: string;
  refresh: string;
}
