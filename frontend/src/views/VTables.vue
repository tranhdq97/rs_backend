<template>
  <div class="container">
    <CTableRep v-for="i in 10" :key="i" :name="i.toString()" :data="dummy" />
  </div>
</template>

<script lang="ts">
import CTableRep from "@/components/CTableRep.vue";
import { IFTableRep } from "@/interfaces/tables";
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    const dummy: IFTableRep = {
      isHavePhoneNumber: true,
      lastServedAt: new Date(Date.now()),
      oldestOrderAt: new Date(Date.now()),
      numServed: 2,
      numOrders: 5,
    };
    return { dummy };
  },
  components: { CTableRep },
});
</script>

<style lang="scss" scoped>
.container {
  flex-direction: row;
  padding: var(--s-large);
  align-content: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  row-gap: var(--s-medium);
  column-gap: var(--s-small);
  flex: 1 0 0;
  background: var(--c-tables);
}
</style>
