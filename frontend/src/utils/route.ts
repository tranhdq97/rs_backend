import { IFRouterParams } from "@/interfaces/common";

export function formRouter(
  baseRoute: string,
  replaced_params?: Array<IFRouterParams>,
  params?: Array<IFRouterParams>
) {
  replaced_params?.map((val) => {
    baseRoute = baseRoute.replace(val.key, val.value);
  });
  if (params) {
    baseRoute += "?";
    params.map((val) => {
      baseRoute += val.key + "=" + val.value;
    });
  }
  return baseRoute;
}
