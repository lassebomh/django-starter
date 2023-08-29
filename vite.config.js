import UnoCSS from 'unocss/vite';
import FullReload from 'vite-plugin-full-reload';

export default {
  plugins: [
    FullReload(['./**/*.html', './static/src/**/*'], { delay: 0 }),
    UnoCSS(),
  ],
  root: './static/src',
  base: '/static/',
  server: {
    host: true,
    port: 3000,
    open: false,
    // hmr: false,
    hmr: {
      host: 'localhost',
      port: 3000,
    },
    watch: {
      // usePolling: true,
      disableGlobbing: false,
    },
  },
  build: {
    outDir: './static/dist',
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: 'main.js',
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};