<template>
  <LAuthForm>
    <template v-slot:icon>
      <img src="@/assets/icons/login.png" />
    </template>
    <template v-slot:fields>
      <CEnterField
        :title="ECommon.EMAIL"
        :placeHolder="EPlaceHolder.ENTER_EMAIL"
      />
      <CEnterField
        :title="ECommon.PASSWORD"
        :placeHolder="EPlaceHolder.ENTER_PASSWORD"
        type="password"
      />
    </template>
    <template v-slot:button>
      <CButton :name="ECommon.SIGNIN" @click="() => router.push('/')" />
    </template>
    <template v-slot:ext>
      <router-link :to="'/' + ERouter.SIGNUP">
        {{ $t(ECommon.SIGNUP) }}
      </router-link>
    </template>
  </LAuthForm>
</template>

<script lang="ts">
import LAuthForm from "@/layouts/LAuthForm.vue";
import { ERouter } from "@/enums/routers";
import { ECommon, EPlaceHolder } from "@/enums/common";
import { defineComponent } from "vue";
import CButton from "@/components/CButton.vue";
import CEnterField from "@/components/CEnterField.vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const router = useRouter();
    return { ECommon, EPlaceHolder, ERouter, router };
  },
  components: { LAuthForm, CButton, CEnterField },
});
</script>
<style lang="scss" scoped></style>
