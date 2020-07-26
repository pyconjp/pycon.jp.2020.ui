/*
 ** TailwindCSS Configuration File
 **
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */
const defaultTheme = require('tailwindcss/defaultTheme')
const plugin = require('tailwindcss/plugin')

module.exports = {
  purge: {
    enabled: process.env.NODE_ENV === 'production',
    content: [
      'components/**/*.vue',
      'layouts/**/*.vue',
      'pages/**/*.vue',
      'plugins/**/*.js',
      'nuxt.config.ts',
    ],
    options: {
      whitelist: [
        'hidden',
        'border-blue-400',
        'bg-blue-400',
        'bg-blue-100',
        'border-orange-400',
        'bg-orange-400',
        'bg-orange-100',
      ],
    },
  },
  theme: {
    fontFamily: {
      sans: ["'Rounded Mplus 1c'", ...defaultTheme.fontFamily.sans],
      serif: [...defaultTheme.fontFamily.serif],
      mono: [...defaultTheme.fontFamily.mono],
    },
    screens: {
      sm: '480px',
      md: '768px',
      tb: '848px',
      lg: '992px',
      xl: '1280px',
    },
    extend: {
      colors: {
        'py-black': '#404a6b',
        'py-blue-light': '#d4d4ff',
        'py-orange-light': '#ffd8a1',
        'py-blue-dark': '#3D40CB',
        'py-orange-dark': '#EE9D2C',
      },
      spacing: {
        72: '18rem',
        80: '20rem',
        96: '24rem',
        120: '30rem',
      },
      width: {
        '35vw': '35vw',
        '50vw': '50vw',
        '70vw': '70vw',
      },
      margin: {
        screen: '0 calc(50% - 50vw)',
      },
      borderRadius: {
        xl: '4rem',
        '2xl': '8rem',
        py: '98px',
        'card-head': '2.35rem',
        '50%': '50%',
      },
      boxShadow: {
        right:
          '10px 10px 15px -3px rgba(0, 0, 0, 0.1), 4px 4px 6px -2px rgba(0, 0, 0, 0.05)',
        left:
          '-10px 10px 15px -3px rgba(0, 0, 0, 0.1), -4px 4px 6px -2px rgba(0, 0, 0, 0.05)',
      },
      inset: {
        '1/2': '50%',
        '3/4': '75%',
        '1/4': '25%',
      },
    },
  },
  variants: {
    backgroundColor: ['hover', 'group-hover'],
    textColor: ['hover', 'group-hover'],
    margin: ['responsive', 'first'],
    padding: ['responsive', 'odd', 'even'],
    borderWidth: ['responsive', 'hover'],
  },
  plugins: [
    plugin(function ({ addComponents }) {
      addComponents({
        '.aspect': {
          position: 'relative',
          width: '100%',
          height: '0',
          '> *': {
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: '100%',
          },
        },
        '.ratio-16-9': {
          paddingBottom: '56.25%',
        },
      })
    }),
  ],
}
