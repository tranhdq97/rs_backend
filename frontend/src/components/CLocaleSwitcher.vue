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

export default {
  setup() {
    const handleSelection = (selectedLocale: string) => {
      localStorage.setItem(ECommon.LOCALE, selectedLocale);
    };
    return { ELanguageCodes, handleSelection };
  },
};
</script>

<style lang="scss" scoped>
select {
  padding: var(--s-small);
  border: 1px solid transparent;
  &:hover {
    border: 1px solid var(--c-primary);
  }
}
</style>
