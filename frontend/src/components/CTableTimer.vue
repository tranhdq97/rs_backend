<template>
  <div>
    <span class="material-icons">{{ icon }}</span>
    <span>{{ amountTime }} {{ $t(ECommon.MINUTES) }}</span>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { ECommon } from "@/enums/common";
import { untilNow } from "@/utils/time";

export default defineComponent({
  props: {
    icon: { type: String, required: true },
    mockTime: { type: Date, required: true },
  },
  setup(props) {
    const amountTime = ref(0);
    amountTime.value = untilNow(props.mockTime);
    setInterval(() => {
      amountTime.value = untilNow(props.mockTime);
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
