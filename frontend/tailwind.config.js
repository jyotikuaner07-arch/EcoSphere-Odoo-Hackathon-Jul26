/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bgBase: '#0F1410',
        bgSurface: '#161D18',
        accentGrowth: '#4CBB6C',
        accentSignal: '#E8B84B',
        accentTrust: '#5C8AE6',
        accentXp: '#C97CE0',
        textPrimary: '#EDEFEC',
        textMuted: '#8A938C',
        danger: '#E4573D',
      },
    },
  },
  plugins: [],
}