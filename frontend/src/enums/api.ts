export enum EAFileManagement {
  CREATE = "/storagge/file-management/create",
  LIST = "/storagge/file-management/list",
  DETAIL = "/storagge/file-management/:index/detail",
  UPDATE = "/storagge/file-management/:index/update",
  DELETE = "/storagge/file-management/:index/delete",
}

export enum EAAddress {}

export enum EAAuth {
  TOKEN = "/staff/auth/token",
  REFRESH_TOKEN = "/staff/auth/token/refresh",
  GET_ME = "/staff/auth/get-me",
  CHANGE_PASSWORD = "staff/auth/change-password",
}

export enum EACustomer {}

export enum EAMaster {
  CREATE = "staff/master/:master_name/create",
  LIST = "staff/master/:master_name/list",
  DELETE = "staff/master/:master_name/:id/list",
}

export enum EAMenu {
  CREATE = "/staff/menu/create",
  LIST = "/staff/menu/list",
  DETAIL = "/staff/menu/:id/detail",
  UPDATE = "/staff/menu/:id/update",
  DELETE = "/staff/menu/:id/delete",
}

export enum EAOrder {
  CREATE = "/staff/order/create",
  LIST = "/staff/order/list",
  DETAIL = "/staff/order/:id/detail",
  UPDATE = "/staff/order/:id/update",
  DELETE = "/staff/order/:id/delete",
}
export enum EAOrderItem {
  CREATE = "/staff/order_item/create",
  LIST = "/staff/order_item/list",
  DETAIL = "/staff/order_item/:id/detail",
  UPDATE = "/staff/order_item/:id/update",
  DELETE = "/staff/order_item/:id/delete",
}
export enum EAProfile {}

export enum EAStaff {
  CREATE = "/staff/staff/create",
  LIST = "/staff/staff/list",
  DETAIL = "/staff/staff/:id/detail",
  UPDATE = "/staff/staff/:id/update",
  DELETE = "/staff/staff/:id/delete",
}

export enum EATable {
  CREATE = "/staff/table/create",
  LIST = "/staff/table/list",
  DETAIL = "/staff/table/:id/detail",
  UPDATE = "/staff/table/:id/update",
  DELETE = "/staff/table/:id/delete",
}
