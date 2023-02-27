<script lang="ts">
import { ECommon } from "@/enums/common";
import { computed, defineComponent, ref } from "vue";
import CButton from "./CButton.vue";

export default defineComponent({
  props: {
    data: { type: Object, required: true },
  },
  emits: ["serveSubmit"],
  setup(props) {
    const maxServeQuantity = computed(
      () => props.data.quantity - props.data.served_quantity
    );
    const serveQuantity = ref(maxServeQuantity.value);
    return { ECommon, serveQuantity, maxServeQuantity };
  },
  components: { CButton },
});
</script>

<template>
  <div class="modal title">{{ $t(ECommon.SERVE) }}</div>
  <div class="modal">
    {{ $t(ECommon.MEAL_NAME) }} :
    <span>{{ data?.menu.name || "..." }}</span>
  </div>
  <div class="modal">
    {{ $t(ECommon.SERVED_QUANTITY) }} :
    <span>{{ data?.served_quantity }} / {{ data?.quantity }}</span>
  </div>
  <div class="modal">
    {{ $t(ECommon.SERVING_QUANTITY) }} :
    <div class="stretch"></div>
    <span
      :class="'material-icons ' + (serveQuantity <= 1 ? 'disabled' : '')"
      @click="() => (serveQuantity -= 1)"
    >
      remove
    </span>
    <span>{{ serveQuantity }}</span>
    <span
      :class="
        'material-icons ' +
        (maxServeQuantity <= serveQuantity ? 'disabled' : '')
      "
      @click="() => (serveQuantity += 1)"
    >
      add
    </span>
  </div>
  <CButton
    :name="ECommon.SERVE"
    @click="$emit('serveSubmit', { item: data, serveQuantity: serveQuantity })"
  />
</template>

<style lang="scss" scoped>
.modal {
  gap: var(--s-small);
  justify-content: space-between;
}
.title {
  justify-content: center;
  font-weight: var(--fw-large);
  text-transform: uppercase;
  padding-bottom: var(--s-small);
  font-weight: var(--fw-large);
}
.material-icons {
  border: 1px solid var(--c-text);
  border-radius: var(--br-small);
}
.disabled {
  border: 1px solid var(--c-grey);
}
</style>
