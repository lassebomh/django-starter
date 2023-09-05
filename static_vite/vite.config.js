import UnoCSS from 'unocss/vite';
import { defineConfig } from 'vite';

export default defineConfig(({ command, mode, ssrBuild }) => {
  return {
    plugins: [
      UnoCSS(),
    ],
    root: 'src',
    base: '/static/',
    server: {
      host: true,
      port: 3000,
      open: false,
      hmr: {
        host: 'localhost',
        port: 3000,
      },
    },
    build: {
      outDir: '../static/dist',
      assetsDir: '',
      manifest: true,
      emptyOutDir: true,
      rollupOptions: {
        input: {
          'main': 'src/main.js',
        },
      },
    },
  }
})