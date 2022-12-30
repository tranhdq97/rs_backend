import { ECommon } from "@/enums/common";

export function toExchange(money: number): string {
  const currentLocale = localStorage.getItem(ECommon.LOCALE)?.toString();
  const currency = currentLocale === "vi" ? "VND" : "USD";
  return money.toLocaleString(currentLocale, {
    style: "currency",
    currency: currency,
  });
}

export function sumProperty(array: any[], properties: string[]): number {
  let sum = 0;
  array.map((item: any) => {
    let mul = 1;
    properties.map((prop) => (mul *= item[prop]));
    sum += mul;
  });
  return sum;
}
