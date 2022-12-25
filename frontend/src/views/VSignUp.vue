<template>
  <LAuthForm>
    <template v-slot:icon>
      <img src="@/assets/icons/sign-up.png" />
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
      <CButton
        :name="ECommon.SIGNUP"
        @click="() => router.push(ERouter.SIGNIN)"
      />
    </template>
  </LAuthForm>
</template>

<script lang="ts">
import LAuthForm from "@/layouts/LAuthForm.vue";
import { ECommon, EPlaceHolder } from "@/enums/common";
import { defineComponent } from "vue";
import CButton from "@/components/CButton.vue";
import CEnterField from "@/components/CEnterField.vue";
import { useRouter } from "vue-router";
import { ERouter } from "@/enums/routers";

export default defineComponent({
  setup() {
    const router = useRouter();
    return { ECommon, EPlaceHolder, router, ERouter };
  },
  components: { LAuthForm, CButton, CEnterField },
});
</script>
<style lang="scss" scoped></style>
