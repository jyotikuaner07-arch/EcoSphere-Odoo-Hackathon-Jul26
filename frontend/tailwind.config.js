/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bgBase: '#E8F0E9',
        bgBaseDeep: '#D9E8DD',
        bgSurface: '#FFFFFF',
        bgSurfaceAlt: '#EEF5EE',
        primaryGreen: '#2F7D4F',
        primaryGreenDark: '#1F5C3A',
        accentBlue: '#4C7EA8',
        accentAmber: '#D9A441',
        accentViolet: '#8B6FC9',
        textPrimary: '#16241C',
        textMuted: '#5C6B62',
        border: '#DCE5DE',
        danger: '#C1503A',
      },
      fontFamily: {
        display: ['Manrope', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
      },
      boxShadow: {
        card: '0 4px 20px rgba(47, 125, 79, 0.08)',
        cardHover: '0 12px 40px rgba(47, 125, 79, 0.18)',
        glass: '0 8px 32px rgba(31, 92, 58, 0.14)',
      },
      backdropBlur: {
        xs: '2px',
      },
    },
  },
  plugins: [],
}