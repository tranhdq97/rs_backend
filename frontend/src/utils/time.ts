import { IFTimeDiff } from "@/interfaces/common";

export function untilNow(fromDate: Date): IFTimeDiff | null {
  const now = Date.now();
  const mockTime = new Date(fromDate).getTime();
  if (!fromDate) return null;
  const diff = now - mockTime;
  const diffDays = Math.floor(diff / 86400000);
  const diffHours = Math.floor((diff % 86400000) / 3600000);
  const diffMins = Math.floor(((diff % 86400000) % 3600000) / 60000);
  const diffSecs = Math.floor((((diff % 86400000) % 3600000) % 60000) / 1000);
  return {
    diffDays: diffDays,
    diffHours: diffHours,
    diffMins: diffMins,
    diffSecs: diffSecs,
  };
}

export function toTime(time: Date): string {
  if (time) return new Date(time).toTimeString().split(" ")[0];
  else return "";
}
