<template>
  <LAuthForm @keyup.enter="signIn">
    <template v-slot:icon>
      <img src="@/assets/icons/login.png" />
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
      <CButton :name="ECommon.SIGNIN" @click="signIn" />
    </template>
    <template v-slot:ext>
      <router-link :to="ERouter.SIGNUP">
        {{ $t(ECommon.SIGNUP) }}
      </router-link>
    </template>
  </LAuthForm>
</template>

<script lang="ts">
import LAuthForm from "@/layouts/LAuthForm.vue";
import { ERouter } from "@/enums/routers";
import { ECommon, EPlaceHolder } from "@/enums/common";
import { defineComponent, ref } from "vue";
import CButton from "@/components/CButton.vue";
import CEnterField from "@/components/CEnterField.vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import { ESAuth } from "@/enums/store";

export default defineComponent({
  setup() {
    const router = useRouter();
    const store = useStore();
    const email = ref("");
    const password = ref("");
    async function signIn() {
      await store.dispatch(ESAuth.A_SIGN_IN, {
        email: email.value,
        password: password.value,
      });
      router.push(ERouter.HOME);
    }
    return { ECommon, EPlaceHolder, ERouter, router, email, password, signIn };
  },
  components: { LAuthForm, CButton, CEnterField },
});
</script>
<style lang="scss" scoped>
.container {
  justify-content: center;
  height: 100%;
  width: 100%;
}
</style>
