<template>
  <div class="plate">
    <div class="outer">
      <div class="inner">
        <div class="name">{{ name }}</div>
        <div class="header">
          <div class="numServed">
            <span class="material-icons">restaurant_menu</span>
            <span>{{ data.numServed }} / {{ data.numOrders }}</span>
          </div>
          <span
            :class="
              'material-icons' + (data.isHavePhoneNumber ? ' indentified' : '')
            "
          >
            person
          </span>
        </div>
        <CTableTimer icon="set_meal" :mockTime="data.lastServedAt" />
        <CTableTimer icon="hourglass_empty" :mockTime="data.oldestOrderAt" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ECommon } from "@/enums/common";
import CTableTimer from "./CTableTimer.vue";

export default defineComponent({
  props: {
    name: { type: String, reqquired: true },
    data: { type: Object, required: true },
  },
  setup() {
    return { ECommon };
  },
  components: { CTableTimer },
});
</script>

<style lang="scss" scoped>
.header,
.numServed {
  align-items: center;
  gap: var(--s-sp-small);
}
.name {
  font-size: var(--f-medium);
  font-weight: var(--fw-s-large);
  position: absolute;
  color: var(--c-primary);
  margin-top: -140px;
  text-shadow: -1px -1px 2px var(--bs-colorLight);
}
.indentified {
  color: var(--c-primary);
}
.plate,
.outer {
  width: 160px;
  height: 160px;
  position: relative;
  cursor: pointer;
}
.outer,
.inner {
  border-radius: 50%;
}
.outer {
  padding: 20px;
  box-shadow: 6px 6px 10px -1px var(--bs-color),
    -6px -6px 10px -1px var(--bs-colorLight);
  &:hover {
    box-shadow: 10px 10px 10px -1px var(--bs-color),
      -2px -2px 10px -1px var(--bs-colorLight);
  }
}
.inner {
  height: 120px;
  width: 120px;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  box-shadow: inset 4px 4px 6px -1px var(--bs-color),
    inset -4px -4px 6px -1px var(--bs-colorLight);
  &:hover {
    box-shadow: inset 2px 2px 6px -1px var(--bs-color),
      inset -6px -6px 10px -1px var(--bs-colorLight);
  }
}
circle {
  fill: none;
  stroke: var(--c-primary);
  stroke-width: 20px;
  stroke-dasharray: 472;
  stroke-dashoffset: 100;
}
</style>
