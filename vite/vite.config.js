import UnoCSS from 'unocss/vite';
import FullReload from 'vite-plugin-full-reload';

const MODE = process.env.MODE

var plugins = []
var input = {
  main: 'src/main.js',
}

if (MODE == 'development'){
  plugins.push(FullReload(['../**/*.html', './src/**/*'], { delay: 0 }))
  input['unoruntime'] = 'src/uno-runtime.js'
} else {
  plugins.push(UnoCSS())
  input['unobuild'] = 'src/uno-build.js'
}

export default {
  plugins: plugins,
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
      input: input,
      output: {
        chunkFileNames: undefined,
      },
    },
  },
};