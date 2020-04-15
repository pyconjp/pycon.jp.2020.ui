/*
 ** TailwindCSS Configuration File
 **
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  theme: {
    fontFamily: {
      sans: ['Noto Sans', ...defaultTheme.fontFamily.sans],
      serif: ['Noto Serif', ...defaultTheme.fontFamily.serif],
      mono: [...defaultTheme.fontFamily.mono]
    },
    extend: {
      spacing: {
        72: '18rem',
        80: '20rem',
        96: '24rem',
        120: '30rem'
      },
      margin: {
        screen: '0 calc(50% - 50vw)'
      }
    }
  },
  variants: {
    margin: ['responsive', 'first']
  },
  plugins: []
}
