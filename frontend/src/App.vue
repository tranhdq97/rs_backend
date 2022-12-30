<template>
  <CSideBar />
  <div class="container router-view">
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CSideBar from "./components/CSideBar.vue";

export default defineComponent({
  components: { CSideBar },
});
</script>

<style>
#app {
  font-family: "Roboto", sans-serif;
  font-weight: 400;
  background: var(--c-background);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--c-text);
  display: flex;
  height: 100vh;
}
</style>
