<template>
  <tr>
    <td>{{ item.menu.name }}</td>
    <td class="text-center">{{ item.quantity }}</td>
    <td class="text-center">{{ item?.served_quantity }}</td>
    <td class="text-right mobile-hidden">{{ toExchange(item.menu.price) }}</td>
    <td class="text-right">{{ toTime(item.updated_at) }}</td>
    <td class="text-right">{{ toTime(item?.served_at) }}</td>
    <td class="text-right mobile-hidden">
      {{ toExchange(item.menu.price * item.served_quantity) }}
    </td>
    <td>
      <span
        :class="'material-icons ' + (isFullServed ? 'disabled' : '')"
        @click="$emit('serve')"
      >
        set_meal
      </span>
    </td>
  </tr>
</template>

<script lang="ts">
import { ECommon } from "@/enums/common";
import { toExchange } from "@/utils/common";
import { toTime } from "@/utils/time";
import { computed, defineComponent } from "vue";

export default defineComponent({
  props: {
    item: { type: Object, required: true },
  },
  emits: ["serve"],
  setup(props) {
    const isFullServed = computed(
      () => !(props.item.quantity - props.item.served_quantity)
    );
    return { ECommon, toExchange, toTime, isFullServed };
  },
});
</script>

<style lang="scss" scoped>
.wrap {
  justify-content: space-between;
}
.text-left {
  flex-grow: 1;
}
span {
  padding-left: var(--s-medium);
  &:hover {
    color: var(--c-primary);
  }
}
td {
  padding-top: var(--s-small);
}
@media screen and (max-width: 480px) {
  .mobile-hidden {
    visibility: hidden;
    display: none;
  }
}
</style>
