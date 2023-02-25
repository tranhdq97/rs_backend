<script lang="ts">
import { toExchange } from "@/utils/common";
import { ESCart } from "@/enums/store";
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  props: {
    meal: { type: Object, required: true },
  },
  setup(props) {
    const store = useStore();
    const isInCart = computed(() =>
      store.getters[ESCart.G_IS_IN_CART](props.meal?.id)
    );
    return { store, isInCart, toExchange };
  },
});
</script>

<template>
  <div
    :class="
      'wrap' +
      (isInCart ? ' in-cart' : '' + (!meal?.is_available ? ' disabled' : ''))
    "
  >
    <img v-if="meal?.photo" :src="meal?.photo?.file" />
    <img v-else src="@/assets/images/defaultImg.png" />
    <div class="info">
      <div class="text-info">
        <div class="title">{{ meal?.name }}</div>
        <div class="money">
          <span class="material-icons-round">paid</span>
          {{ toExchange(meal?.price) }}
        </div>
        <div class="money">
          <span class="material-icons-round">local_mall</span>
          {{ meal?.num_ordered }}
        </div>
      </div>
      <div class="btn" v-if="isInCart">
        <span class="material-icons">add</span>
        {{ 0 }}
        <span class="material-icons">remove</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
img {
  width: 100%;
  height: 100%;
}
.wrap {
  width: 240px;
  padding: var(--s-medium);
  background: var(--c-white);
  border-radius: var(--br-medium);
  box-shadow: 0px 2px 5px var(--c-grey);
  flex-direction: column;
  gap: var(--s-small);

  &:hover {
    box-shadow: 0px 4px 5px var(--c-grey);
  }
}
.title {
  white-space: normal;
  text-align: center;
  width: 100%;
  text-transform: capitalize;
  font-weight: var(--fw-large);
  padding: var(--s-small) 0;
}
.info {
  justify-content: space-between;
  flex-direction: column;
  gap: var(--s-medium);
}
.text-info {
  align-items: flex-start;
  flex-direction: column;
  gap: var(--s--small);
}
.btn {
  gap: var(--s-medium);
  align-items: center;
}
.money {
  gap: var(--s-small);
  align-items: center;
}
.in-cart {
  border-radius: 1px solid var(--c-primary);
}
@media screen and (max-width: 480px) {
  .wrap {
    width: 100%;
    min-width: 300px;
  }
  .info {
    width: 100%;
    flex-direction: row;
  }
  .btn {
    flex-direction: column;
    gap: var(--s-small);
  }
  .title {
    justify-content: left;
  }
}
</style>
