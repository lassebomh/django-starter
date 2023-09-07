import UnoCSS from 'unocss/vite';
import { defineConfig } from 'vite';
import webfontDownload from 'vite-plugin-webfont-dl';

export default defineConfig({
    plugins: [
      UnoCSS(),
      webfontDownload([
        'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap',
      ], {
        injectAsStyleTag: false,
      }),
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
      outDir: '../../static/dist',
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
)