import IFCustomer from "./customer";
import IFMenuItem from "./menu";
import IFStaff from "./staff";
import { IFTable } from "./tables";

export interface IFOrder {
  id?: number;
  table: IFTable;
  customer?: IFCustomer;
  paid_at?: Date;
  num_people?: number;
}

export interface IFOrderItem {
  id?: number;
  table: IFTable;
  order?: IFOrder;
  menu: IFMenuItem;
  staff: IFStaff;
  quantity: number;
  served_quantity?: number;
  served_at?: Date;
  created_at?: Date;
  updated_at?: Date;
}
