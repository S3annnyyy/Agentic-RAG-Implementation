import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {      
      colors: {
        primary: {
          DEFAULT: '#68E2FA',
          purple:'#9757D7',
          pink: '#EF466F',          
          backdrop: '#000000e1',
          grey: '#F1F5F9',
          blue: '#3266D3',
          dark: '#323e4d',
          green: '#60c039',
          darkgreen: '#577f5d',
        },
        secondary:{
          DEFAULT:'#3772FF',
          pink: '#E4D7CF',
          yellow: '#FFD166',
          purple:'#CDB4DB',
        },        
      },      
    },
    fontFamily: {
      charlieSans: ["Charlie-sans", "sans-serif"],      
    },  
  },  
  plugins: [],
}
export default config