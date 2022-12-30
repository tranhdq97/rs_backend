<template>
  <div class="wrap">
    <span class="material-icons delete" @click="removeOrderItem">
      delete_outline
    </span>
    <div class="name">{{ item.menu.name }}</div>
    <span
      :class="'material-icons remove ' + (isDecreaseDisabled ? 'disabled' : '')"
      @click="decreaseQuantity"
    >
      remove
    </span>
    <div class="quantity">{{ item.quantity }}</div>
    <span class="material-icons" @click="increaseQuantity"> add </span>
  </div>
</template>

<script lang="ts">
import { ESOrderItem } from "@/enums/store";
import { computed, defineComponent } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  props: {
    item: { type: Object, required: true },
  },
  setup(props) {
    const store = useStore();
    const isDecreaseDisabled = computed(() => props.item.quantity <= 1);
    const increaseQuantity = () =>
      store.dispatch(ESOrderItem.A_INCREASE_QUANTITY, props.item);
    const decreaseQuantity = () =>
      store.dispatch(ESOrderItem.A_DECREASE_QUANTITY, props.item);
    const removeOrderItem = () =>
      store.commit(ESOrderItem.M_REMOVE_ORDER_ITEM, props.item);
    return {
      isDecreaseDisabled,
      increaseQuantity,
      decreaseQuantity,
      removeOrderItem,
    };
  },
});
</script>

<style lang="scss" scoped>
.wrap {
  justify-content: space-between;
  align-items: center;
  gap: var(--s-medium);
}
.name {
  flex-grow: 1;
  text-align: left;
  justify-content: flex-start;
  white-space: break-spaces;
}
span {
  border: 1px solid var(--c-grey);
  border-radius: var(--br-small);
  &:hover {
    color: var(--c-primary);
    border: 1px solid var(--c-primary);
  }
}
.delete,
.remove {
  font-weight: var(--fw-small);
  &:hover {
    color: var(--c-alert);
    border: 1px solid var(--c-alert);
  }
}
.disabled {
  border: 1px solid var(--c-grey);
}
</style>
