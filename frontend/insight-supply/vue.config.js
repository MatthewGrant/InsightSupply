module.exports = {
    css: {
        loaderOptions: {
            sass: {
                data: `@import "@/scss/utilities/_variables.scss";`
            }
        }
    },
    devServer: {
      host: "localhost",
      proxy: {
         '/api': {
           target: 'http://localhost:8000',
           ws: true,
           changeOrigin: true,
         },
      }
    }
}