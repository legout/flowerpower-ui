// tailwind.config.js
module.exports = {
  content: [
    "./templates/**/*.htmy"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui')
  ],
}