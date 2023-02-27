<template>
  <select v-model="lang" @click="handleSelection">
    <option v-for="(locale, i) in ELanguageCodes" :key="i" :value="locale">
      {{ locale }}
    </option>
  </select>
</template>

<script lang="ts">
import { ELanguageCodes } from "@/enums/languages";
import { ECommon } from "@/enums/common";
import { useI18n } from "vue3-i18n";
import { ref } from "vue";

export default {
  setup() {
    const i18n = useI18n();
    const lang = ref(i18n.getLocale());
    const handleSelection = () => {
      localStorage.setItem(ECommon.LOCALE, lang.value);
      i18n.setLocale(lang.value);
    };
    return { ELanguageCodes, handleSelection, lang };
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
