<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <button @click="click">AAA</button>
  </div>
</template>

<script lang="ts">
import authAxios from "@/axios";
import { EAMaster } from "@/enums/api";
import { EMasterModel, ERouterParams } from "@/enums/common";
import { formRouter } from "@/utils/route";
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    async function click() {
      const url = formRouter(EAMaster.LIST, [
        { key: ERouterParams.MASTER_NAME, value: EMasterModel.COUNTRY },
      ]);
      await authAxios.get(url);
    }
    return { click };
  },
});
</script>
