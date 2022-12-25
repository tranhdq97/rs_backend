<template>
  <div class="container">
    <CLocaleSwitcher />
  </div>
</template>

<script lang="ts">
import CLocaleSwitcher from "@/components/CLocaleSwitcher.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: { CLocaleSwitcher },
});
</script>

<style lang="scss" scoped></style>
