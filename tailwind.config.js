/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        darkslategray: { "100": "#424242", "200": "#303030" },
        white: "#fff",
        forestgreen: "#4caf50",
        deepskyblue: "#03acf2",
        gray: {
          "100": "rgba(33, 33, 33, 0.8)",
          "200": "rgba(255, 255, 255, 0.12)",
          "300": "rgba(255, 255, 255, 0.7)",
          "400": "rgba(0, 0, 0, 0.87)",
        },
        lightblue: "#b3e5fc",
        beige: "#c8e6c9",
        black: "#000",
        cornflowerblue: "#2196f3",
        azure: "#eef9f9",
        darkslateblue: "#0d47a1",
        steelblue: "#00579b",
      },
      fontFamily: {
        lato: "Lato",
        "open-sans": "'Open Sans'",
        roboto: "Roboto",
      },
      borderRadius: { "base-5": "15.5px", mini: "15px" },
    },
    fontSize: {
      "17xl": "36px",
      base: "16px",
      lg: "18px",
      "5xl": "24px",
      sm: "14px",
      "33xl": "52px",
      "9xl": "28px",
    },
  },
  corePlugins: { preflight: false },
};
