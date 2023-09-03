import UnoCSS from 'unocss/vite';
import { defineConfig } from 'vite';
import FullReload from 'vite-plugin-full-reload';

export default defineConfig(({ command, mode, ssrBuild }) => {
  return {
    plugins: [
      UnoCSS(),
      FullReload(['../**/*.html', './src/**/*'], { delay: 0 })
    ],
    root: '/app/' + process.env.STATIC_SRC_DIR + "/src",
    base: '/static/',
    server: {
      host: true,
      port: 3000,
      open: false,
      hmr: {
        host: 'localhost',
        port: 3000,
      },
      watch: {
        disableGlobbing: false,
      },
    },
    build: {
      outDir: process.env.STATIC_DIST_DIR,
      assetsDir: '',
      manifest: true,
      emptyOutDir: true,
      rollupOptions: {
        input: {
          'main': 'src/main.js',
          'uno': `src/uno-${command}.js`,
        },
        output: {
          chunkFileNames: undefined,
        },
      },
    },
  }
})