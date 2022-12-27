export function routeToIndex(baseRoute: string, index: number) {
  return baseRoute.replace(":index", index.toString());
}
