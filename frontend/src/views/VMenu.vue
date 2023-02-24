<script lang="ts">
import CAddButton from "@/components/CAddButton.vue";
import { ESMenu, ESTable } from "@/enums/store";
import { defineComponent, computed } from "vue";
import { useStore } from "vuex";

export default defineComponent({
  setup() {
    const store = useStore();
    store.dispatch(ESTable.A_GET_TABLES);
    store.dispatch(ESMenu.A_GET_MENU);
    const tables = computed(() => store.getters[ESTable.G_TABLES]);
    async function addTable() {
      await store.dispatch(ESTable.A_ADD_TABLE);
    }
    return { tables, addTable };
  },
  components: { CAddButton },
});
</script>

<template>
  <div class="container">
    <CAddButton @click="addTable" />
  </div>
</template>

<style lang="scss" scoped>
.container {
  flex-direction: row;
  align-content: flex-start;
  justify-content: space-between;
  flex-wrap: wrap;
  row-gap: var(--s-medium);
  column-gap: var(--s-small);
  flex: 1 0 0;
}
</style>
