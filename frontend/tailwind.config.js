/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,ts}'],
  theme: {
    fontFamily: {
      inter: ['Inter', 'sans-serif'],
      'architects-daughter': ['"Architects Daughter"', 'sans-serif'],
    },
    fontSmoothing: {
      antialiased: true
    },
    extend: {},
  },
  plugins: [],
}

