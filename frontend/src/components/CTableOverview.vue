<template>
  <div class="container area">
    <div class="table">{{ $t(ECommon.TABLE) }}: {{ tableIndex }}</div>
    <CSearchField :placeHolder="ECommon.SEARCH" />
  </div>
</template>

<script lang="ts">
import { ECommon } from "@/enums/common";
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import CSearchField from "./CSearchField.vue";

export default defineComponent({
  setup() {
    const router = useRouter();
    const tableIndex = router.currentRoute.value.params.index;
    return { ECommon, tableIndex };
  },
  components: { CSearchField },
});
</script>

<style lang="scss" scoped>
.container {
  overflow-y: auto;
  justify-content: flex-start;
  gap: var(--s-small);
}
.table {
  justify-content: flex-start;
  text-transform: capitalize;
  font-weight: var(--fw-large);
}
</style>
