<template>
  <div class="container">
    <CTableOverview />
  </div>
</template>

<script lang="ts">
import CTableOverview from "@/components/CTableOverview.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: { CTableOverview },
});
</script>

<style lang="scss" scoped></style>
