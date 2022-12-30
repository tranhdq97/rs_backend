export function untilNow(fromDate: Date): number {
  if (!fromDate) return 0;
  const diff = new Date(Date.now() - new Date(fromDate).getTime());
  return diff.getMinutes();
}

export function toTime(time: Date): string {
  if (time) return new Date(time).toTimeString().split(" ")[0];
  else return "";
}
