import '@unocss/reset/tailwind-compat.css'
import initUnocssRuntime from '@unocss/runtime'
import unoConfig from '../uno.config'

initUnocssRuntime({
    defaults: unoConfig
})
    