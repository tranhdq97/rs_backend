<script lang="ts">
import { computed, defineComponent } from "vue";
import { ECommon, ERouterParams } from "@/enums/common";
import CTableTimer from "./CTableTimer.vue";
import { formRouter } from "@/utils/route";
import { ERouter } from "@/enums/routers";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ESOrderItem } from "@/enums/store";

export default defineComponent({
  props: {
    table: { type: Object, required: true },
  },
  setup(props) {
    const router = useRouter();
    const store = useStore();
    const data = computed(() =>
      store.getters[ESOrderItem.G_TABLE_REP_DATA](props.table)
    );
    const handleClick = () => {
      const toRouter = formRouter(ERouter.TABLE, [
        { key: ERouterParams.INDEX, value: props.table.id },
      ]);
      router.push(toRouter);
    };
    return { ECommon, handleClick, data };
  },
  components: { CTableTimer },
});
</script>

<template>
  <div class="plate" @click="handleClick">
    <div class="outer">
      <div :class="'inner' + (table.is_available ? ' avail' : '')">
        <div class="index">{{ table.name }}</div>
        <div class="header" v-if="!table.is_available">
          <div class="numServed">
            <span
              :class="
                'material-icons' +
                (data.numServed === data.numOrders ? ' identified' : '')
              "
              >restaurant_menu</span
            >
            <span>{{ data.numServed }} / {{ data.numOrders }}</span>
          </div>
          <span
            :class="
              'material-icons' + (data.isHavePhoneNumber ? ' identified' : '')
            "
          >
            person
          </span>
        </div>
        <CTableTimer
          v-if="
            !table.is_available &&
            data.lastServedAt &&
            data.numOrders != data.numServed
          "
          icon="set_meal"
          :mockTime="data.lastServedAt"
        />
        <CTableTimer
          v-if="
            !table.is_available &&
            data.newestOrderedAt &&
            data.numOrders != data.numServed
          "
          icon="hourglass_empty"
          :mockTime="data.newestOrderedAt"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.header,
.numServed {
  align-items: center;
  gap: var(--s-sp-small);
}
.index {
  font-size: var(--f-medium);
  font-weight: var(--fw-s-large);
  position: absolute;
  color: var(--c-primary);
  margin-top: -140px;
  text-shadow: -1px -1px 2px var(--bs-colorLight);
}
.identified {
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
.avail {
  background: var(--c-greyLight);
}
</style>
