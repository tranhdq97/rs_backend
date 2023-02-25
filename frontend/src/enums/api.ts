export enum EAFileManagement {
  CREATE = "/stg/file-management/create",
  LIST = "/stg/file-management/list",
  DETAIL = "/stg/file-management/:id/detail",
  UPDATE = "/stg/file-management/:id/update",
  DELETE = "/stg/file-management/:id/delete",
}

export enum EAAddress {}

export enum EAAuth {
  TOKEN = "/stf/auth/token",
  REFRESH_TOKEN = "/stf/auth/token/refresh",
  GET_ME = "/stf/auth/get-me",
  CHANGE_PASSWORD = "stf/auth/change-password",
}

export enum EACustomer {
  CREATE = "/stf/customer/create",
  LIST = "/stf/customer/list",
  DETAIL = "/stf/customer/:id/detail",
  DELETE = "/stf/customer/:id/delete",
  UPDATE = "/stf/customer/:id/update",
}

export enum EAMaster {
  CREATE = "stf/master/:master_name/create",
  LIST = "stf/master/:master_name/list",
  DELETE = "stf/master/:master_name/:id/list",
}

export enum EAMenu {
  CREATE = "/stf/menu/create",
  LIST = "/stf/menu/list",
  DETAIL = "/stf/menu/:id/detail",
  UPDATE = "/stf/menu/:id/update",
  DELETE = "/stf/menu/:id/delete",
}

export enum EAOrder {
  CREATE = "/stf/order/create",
  LIST = "/stf/order/list",
  DETAIL = "/stf/order/:id/detail",
  UPDATE = "/stf/order/:id/update",
  DELETE = "/stf/order/:id/delete",
}
export enum EAOrderItem {
  CREATE = "/stf/order_item/create",
  LIST = "/stf/order_item/list",
  DETAIL = "/stf/order_item/:id/detail",
  UPDATE = "/stf/order_item/:id/update",
  DELETE = "/stf/order_item/:id/delete",
}
export enum EAProfile {
  CREATE = "/stf/profile/create",
  DETAIL = "/stf/profile/:id/detail",
  UPDATE = "/stf/profile/:id/update",
  DELETE = "/stf/profile/:id/delete",
}

export enum EAStaff {
  CREATE = "/stf/staff/create",
  LIST = "/stf/staff/list",
  DETAIL = "/stf/staff/:id/detail",
  UPDATE = "/stf/staff/:id/update",
  DELETE = "/stf/staff/:id/delete",
}

export enum EATable {
  CREATE = "/stf/table/create",
  LIST = "/stf/table/list",
  DETAIL = "/stf/table/:id/detail",
  UPDATE = "/stf/table/:id/update",
  DELETE = "/stf/table/:id/delete",
}
