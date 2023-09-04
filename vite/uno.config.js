import presetWind from '@unocss/preset-wind';
import transformerVariantGroup from '@unocss/transformer-variant-group';
import { defineConfig } from 'unocss';

export default defineConfig({
    presets: [
        presetWind(),
    ],
    shortcuts: [
        {
            'label': 'block mb-2 text-sm font-medium text-gray-900 error:text-red-700',
            'input': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:outline-blue-500 focus:border-blue-500 block w-full p-2.5 error:bg-red-50 error:border-red-500 error:text-red-900 error:placeholder-red-700 error:focus:outline-red-500 error:focus:border-red-500',
            'text': 'input',
        },
        [/^btn-(.+)$/, function ([, color]) {
            return `focus:ring-4 focus:outline-none font-medium mb-2 mr-2 px-5 py-2.5 rounded-lg text-sm text-white bg-${color}-700 focus:ring-${color}-300 hover:bg-${color}-800`
        }]
    ],
    content: {
        filesystem: [
            "../**/templates/**/*.html"
        ]
    },
    variants: [
        (matcher) => {
            if (!matcher.startsWith('error:'))
                return matcher
            
            return {
                // slice `hover:` prefix and passed to the next variants and rules
                matcher: matcher.slice(6),
                selector: s => `*:has(> input[unicorn\\:error\\:required]) ${s}, *:has(> input[unicorn\\:error\\:invalid]) ${s}`,
            }
        },
        (matcher) => {
            let match = matcher.match(/^\[([^\]]+)\]:(.+)$/)

            if (match == null)
                return matcher

            let anyselector = match[1].replace('_', ' ')
            let after = match[2]
            
            return {
                // slice `hover:` prefix and passed to the next variants and rules
                matcher: after,
                selector: s => `${anyselector} ${s}`,
            }
        }
    ],
    transformers: [
        transformerVariantGroup(),
    ],
})