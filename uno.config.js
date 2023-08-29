import presetWind from '@unocss/preset-wind';

export default {
    presets: [
        presetWind(),
    ],
    content: {
        filesystem: [
            "./**/templates/**/*.html"
        ]
    },
}