<template>
  <select v-model="$i18n.locale">
    <option
      v-for="(locale, i) in locales"
      :key="i"
      :value="locale"
      @click="handleSelect(locale)"
    >
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
    const currentLocale = localStorage.getItem(ECommon.LOCALE);
    const { locale } = useI18n({ useScope: "global" });
    locale.value = currentLocale ? currentLocale : ELanguageCodes.ENGLISH;
    const locales = ELanguageCodes;
    const handleSelect = (selectedLocale: string) => {
      locale.value = selectedLocale;
    };
    return { locales, handleSelect };
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
