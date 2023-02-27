<template>
  <div>
    <span class="material-icons">{{ icon }}</span>
    <span>{{ amountTime }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { ECommon } from "@/enums/common";
import { untilNow } from "@/utils/time";
import { useI18n } from "vue3-i18n";
import { IFTimeDiff } from "@/interfaces/common";

export default defineComponent({
  props: {
    icon: { type: String, required: true },
    mockTime: { type: Date, required: true },
  },
  setup(props) {
    const { t } = useI18n();
    const amountTime = ref<string | null>("");
    function toDisplayingTime() {
      const timeDiff: IFTimeDiff | null = untilNow(props.mockTime);
      if (!timeDiff) return null;
      if (timeDiff.diffDays)
        return timeDiff.diffDays.toString() + " " + t(ECommon.DAYS);
      else if (timeDiff.diffHours)
        return timeDiff.diffHours.toString() + " " + t(ECommon.HOURS);
      else if (timeDiff.diffMins)
        return timeDiff.diffMins.toString() + " " + t(ECommon.MINUTES);
      else if (timeDiff.diffSecs)
        return timeDiff.diffSecs.toString() + " " + t(ECommon.SECONDS);
      else return null;
    }
    amountTime.value = toDisplayingTime();
    setInterval(() => {
      amountTime.value = toDisplayingTime();
    }, 60000);
    return { ECommon, amountTime };
  },
});
</script>

<style lang="scss" scoped>
div {
  display: flex;
  align-items: center;
  gap: var(--s-sp-small);
}
span {
  text-transform: lowercase;
}
</style>
