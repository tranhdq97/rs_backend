<template>
  <CLocaleSwitcher />
  <router-view class="router-view" />
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CLocaleSwitcher from "./components/CLocaleSwitcher.vue";

export default defineComponent({
  components: { CLocaleSwitcher },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  justify-content: center;
  color: var(--c-text);
  display: flex;
  flex-direction: column;
  height: 100vh;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
.router-view {
  flex-grow: 1;
}
</style>
