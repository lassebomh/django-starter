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
            'input': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 focus:(outline-neutral-700 border-neutral-700) error:(bg-red-50 border-red-500 text-red-900 placeholder-red-700 focus:outline-red-500 focus:border-red-500)',
            // form inputs
            'text': 'input',
            'textarea': "input",
            'number': "input",
            'email': "input",
            'url': "input",
            'password': "input",
            'date': "input",
            'time': "input",
            'datetime-local': "input",
            'select': 'input',
            'time': 'input',
            'date': 'input',
            'splitdatetime': 'input w-auto inline',
            'file': 'block p-2 w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none',
            'clearable_file_input': 'file',
            'checkbox': 'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:outline-3 focus:outline-neutral-500',
            'radio_option': 'w-4 h-4 border-gray-300 focus:(outline-2 outline-neutral-500)',
            'radio': 'flex flex-col gap-1 children:children:(text-sm flex items-center gap-1.5 children:checkbox)',
            'checkbox_select': 'flex flex-col gap-1 children:children:(text-sm flex items-center gap-1.5 children:checkbox)',
            // form extra
            'helptext': 'mt-2 text-sm text-gray-500 error:text-red-400',
            'errorlist': 'children:(mt-2 text-sm text-red-600)',
        },
        [/^btn-(.+)$/, function ([, color]) {
            return `focus:outline-4 focus:outline-none font-medium mb-2 mr-2 px-5 py-2.5 rounded-lg text-sm text-white bg-${color}-700 focus:outline-${color}-300 hover:bg-${color}-800`
        }],
    ],
    safelist: 'password'.split(' '),
    content: {
        filesystem: [
            "../**/templates/**/*.html"
        ],
    },
    variants: [
        (matcher) => {
            if (!matcher.startsWith('error:'))
                return matcher
            
            return {
                // slice `hover:` prefix and passed to the next variants and rules
                matcher: matcher.slice(6),
                // selector: s => `*:has(~ .errorlist)${s}, *:has(> input[unicorn\\:error\\:required]) ${s}, *:has(> input[unicorn\\:error\\:invalid]) ${s}`,
                selector: s => `.has-errors ${s}`,
            }
        },
        (matcher) => {
            let match = matcher.match(/^\[([^\]]+)\]:(.+)$/)
            if (match == null)
                return matcher

            let anyselector = match[1].replace('_', ' ')
            let after = match[2]
            return {
                matcher: after,
                selector: s => `${anyselector} ${s}`,
            }
        }
    ],
    transformers: [
        transformerVariantGroup(),
    ],
})