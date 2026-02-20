/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        infiniti: ['"Infiniti Brand Light"', 'sans-serif'],
      },
    },
  },
  plugins: [],
};