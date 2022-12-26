export function untilNow(fromDate: Date): number {
  const diff = new Date(Date.now() - new Date(fromDate).getTime());
  return diff.getMinutes();
}
