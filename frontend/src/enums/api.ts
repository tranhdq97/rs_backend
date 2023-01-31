export enum EAFileManagement {
  CREATE = "/storagge/file-management/create",
  LIST = "/storagge/file-management/list",
  DETAIL = "/storagge/file-management/:index/detail",
  UPDATE = "/storagge/file-management/:index/update",
  DELETE = "/storagge/file-management/:index/delete",
}

export enum EAAuth {
  TOKEN = "/staff/auth/token",
  REFRESH_TOKEN = "/staff/auth/token/refresh",
  GET_ME = "/staff/auth/get-me",
  CHANGE_PASSWORD = "staff/auth/change-password",
}

export enum EAStaff {
  CREATE = "/staff/staff/create",
  LIST = "/staff/staff/list",
  DETAIL = "/staff/staff/:index/detail",
  UPDATE = "/staff/staff/:index/update",
  DELETE = "/staff/staff/:index/delete",
}

export enum EAMaster {
  CREATE = "staff/master/:master_name/create",
  LIST = "staff/master/:master_name/list",
  DELETE = "staff/master/:master_name/:id/list",
}
