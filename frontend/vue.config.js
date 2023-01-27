const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === "local" ? "/" : "/",
  pluginOptions: {
    i18n: {
      locale: "en",
      fallbackLocale: "en",
      localeDir: "locales",
      enableLegacy: false,
      runtimeOnly: false,
      compositionOnly: false,
      fullInstall: true,
    },
  },
  devServer: {
    proxy: {
      "^/staff": {
        target: "http://localhost:8020",
        changeOrigin: true,
        // secure: false,
        pathRewrite: { "^/staff": "/api" },
      },
      "^/storage": {
        target: "http://localhost:8010",
        changeOrigin: true,
        pathRewrite: { "^/storage": "/api" },
      },
    },
  },
});
