import { createI18n } from "vue3-i18n";

const messages = {
  en: {
    id: "ID",
    home: "home",
    sign_up: "sign up",
    sign_in: "sign in",
    sign_out: "sign out",
    username: "username",
    password: "password",
    first_name: "first name",
    last_name: "last name",
    email: "email",
    phone_number: "phone number",
    enter_email: "enter your email",
    enter_phone_number: "enter your phone number",
    enter_password: "enter your password",
    tables: "tables",
    table: "table",
    order: "order",
    add: "add",
    remove: "remove",
    bill: "bill",
    desserts: "desserts",
    drinks: "drinks",
    appetizers: "appetizer",
    pay: "pay",
    menu: "menu",
    main_course: "main course",
    setting: "setting",
    days: "days",
    hours: "hours",
    minutes: "minutes",
    seconds: "seconds",
    search: "search",
    meal_name: "name",
    quantity: "quantity",
    unit_price: "unit price",
    total: "total",
    ordered_at: "order at",
    preview: "preview",
    served: "served",
    served_at: "served at",
    served_quantity: "served quantity",
    serving_quantity: "serving quantity",
    serve: "serve",
    pay_bill: "pay bill",
    VAT: "VAT",
    amount: "amount",
    permission_denied: "permission denied",
    num_people: "no. people",
    staffs: "staffs",
    staff: "staff",
    type: "role",
    sex: "sex",
    dob: "date of birth",
    address: "address",
    detail: "detail",
    update: "update",
  },
  vi: {
    id: "#",
    home: "trang chủ",
    sign_up: "đăng ký",
    sign_in: "đăng nhập",
    sign_out: "đăng xuất",
    username: "tên tài khoản",
    password: "mật khẩu",
    first_name: "tên",
    last_name: "họ",
    email: "địa chỉ email",
    phone_number: "số điện thoại",
    enter_email: "nhập địa chỉ email",
    enter_phone_number: "nhập số điện thoại",
    enter_password: "nhập mât khẩu",
    tables: "bàn",
    table: "bàn",
    order: "đặt món",
    add: "thêm",
    remove: "xóa",
    bill: "hóa đơn",
    desserts: "món tráng miệng",
    drinks: "đồ uống",
    appetizers: "món khai vị",
    pay: "thanh toán",
    menu: "thực đơn",
    main_course: "món chính",
    setting: "cài đặt",
    days: "ngày",
    hours: "giờ",
    minutes: "phút",
    seconds: "giây",
    search: "tìm kiếm",
    meal_name: "tên món",
    quantity: "số lượng",
    unit_price: "đơn giá",
    total: "tổng tiền",
    ordered_at: "gọi món lúc",
    preview: "xem trước",
    served: "đã lên món",
    served_at: "lên món lúc",
    served_quantity: "số lượng đã phục vụ",
    serving_quantity: "số lượng lên món",
    serve: "lên món",
    pay_bill: "thanh toán hóa đơn",
    VAT: "thuế VAT",
    amount: "thành tiền",
    permission_denied: "bạn không có quyền truy cập",
    num_people: "số người",
    staffs: "nhân viên",
    staff: "nhân viên",
    type: "chức vụ",
    sex: "giới tính",
    dob: "ngày sinh",
    address: "địa chỉ",
    detail: "chi tiết",
    update: "cập nhật",
  },
};

const i18n = createI18n({
  locale: "vi",
  messages: messages,
});

export default i18n;
