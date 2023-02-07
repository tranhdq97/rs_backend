export enum ESSideBar {
  G_IS_SIDEBAR_COLLAPSED = "sideBar/isSideBarCollapsed",
  A_TOGGLE_SIDEBAR = "sideBar/toggleSideBar",
  A_COLLAPSE_SIDEBAR = "sideBar/collapseSideBar",
}

export enum ESMenu {
  G_MENU = "menu/menu",
  G_AVAILABLE_MENU = "menu/availableMenu",
  A_GET_MENU = "menu/getMenu",
}

export enum ESOrderItem {
  G_ORDER_PREVIEW_LIST = "order_item/orderItemPreviewList",
  G_ORDERED_LIST = "order_item/orderedItemList",
  G_TABLE_REP_DATA = "order_item/tableRepData",
  A_GET_ORDER_ITEMS = "order_item/getOrderItems",
  A_ADD_TO_ORDER_PREVIEW = "order_item/addToOrderPreview",
  M_REMOVE_ORDER_ITEM = "order_item/removeOrderItem",
  A_INCREASE_QUANTITY = "order_item/increaseQuantity",
  A_DECREASE_QUANTITY = "order_item/decreaseQuantity",
  A_ORDER = "order_item/order",
  A_SERVE = "order_item/serve",
  A_PAY = "order_item/pay",
}

export enum ESOrder {
  G_ORDER_LIST = "order/orderList",
  G_ORDER = "order/order",
  G_ORDER_BY_TABLE = "order/orderByTable",
  A_ADD_ORDER = "order/addOrder",
  A_GET_ORDERS = "order/getOrders",
  M_REMOVE_ORDER = "order/removeOrder",
}

export enum ESTable {
  G_TABLES = "table/tables",
  G_TABLE = "table/table",
  A_ADD_TABLE = "table/addTable",
  A_GET_TABLES = "table/getTables",
  A_UPDATE_TABLE = "table/updateTable",
}

export enum ESBill {
  G_VAT = "bill/VAT",
}

export enum ESAuth {
  G_USER = "auth/user",
  A_SIGN_UP = "auth/signUp",
  A_SIGN_IN = "auth/signIn",
  A_SIGN_OUT = "auth/signOut",
  A_REFRESH = "auth/refreshToken",
  A_GET_ME = "auth/getMe",
  M_REMOVE_CURRENT_USER = "auth/removeCurrentUser",
  M_SET_USER = "auth/setUser",
}

export enum ESCustomer {
  A_SEARCH_CUSTOMER_BY_PN = "customer/searchCustomerByPhoneNumber",
}
