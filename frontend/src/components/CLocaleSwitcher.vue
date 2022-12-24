<template>
  <select v-model="$i18n.locale" @click="handleSelection($i18n.locale)">
    <option v-for="(locale, i) in ELanguageCodes" :key="i" :value="locale">
      {{ locale }}
    </option>
  </select>
</template>

<script lang="ts">
import { ELanguageCodes } from "@/enums/languages";
import { ECommon } from "@/enums/common";
import { useI18n } from "vue-i18n";

export default {
  setup() {
    const { locale } = useI18n({ useScope: "global" });
    const initLocale = localStorage.getItem(ECommon.LOCALE);
    locale.value = initLocale ? initLocale : ELanguageCodes.VIETNAMESE;
    const handleSelection = (selectedLocale: string) => {
      localStorage.setItem(ECommon.LOCALE, selectedLocale);
    };
    return { ELanguageCodes, handleSelection };
  },
};
</script>

<style lang="scss" scoped>
select {
  z-index: 100;
  position: fixed;
  top: 20px;
  right: 20px;
  padding: var(--s-small);
}
</style>
