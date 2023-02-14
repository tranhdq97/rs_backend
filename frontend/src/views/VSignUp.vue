<template>
  <LAuthForm @keyup.enter="signUp">
    <template v-slot:icon>
      <img src="@/assets/icons/sign-up.png" />
    </template>
    <template v-slot:fields>
      <CEnterField
        :title="ECommon.EMAIL"
        :placeHolder="EPlaceHolder.ENTER_EMAIL"
        @content="(value) => (email = value)"
      />
      <CEnterField
        :title="ECommon.PASSWORD"
        :placeHolder="EPlaceHolder.ENTER_PASSWORD"
        type="password"
        @content="(value) => (password = value)"
      />
    </template>
    <template v-slot:button>
      <CButton :name="ECommon.SIGNUP" @click="signUp" />
    </template>
    <template v-slot:ext>
      <router-link :to="ERouter.SIGNIN">
        {{ $t(ECommon.SIGNIN) }}
      </router-link>
    </template>
  </LAuthForm>
</template>

<script lang="ts">
import LAuthForm from "@/layouts/LAuthForm.vue";
import { ECommon, EPlaceHolder } from "@/enums/common";
import { defineComponent, ref } from "vue";
import CButton from "@/components/CButton.vue";
import CEnterField from "@/components/CEnterField.vue";
import { useRouter } from "vue-router";
import { ERouter } from "@/enums/routers";
import { useStore } from "vuex";
import { ESAuth } from "@/enums/store";

export default defineComponent({
  setup() {
    const router = useRouter();
    const store = useStore();
    const email = ref("");
    const password = ref("");
    async function signUp() {
      await store.dispatch(ESAuth.A_SIGN_UP, {
        email: email.value,
        password: password.value,
      });
      router.push(ERouter.SIGNIN);
    }
    return { ECommon, EPlaceHolder, router, ERouter, signUp, email, password };
  },
  components: { LAuthForm, CButton, CEnterField },
});
</script>
<style lang="scss" scoped>
.container {
  height: 100%;
  width: 100%;
  justify-content: center;
}
</style>
