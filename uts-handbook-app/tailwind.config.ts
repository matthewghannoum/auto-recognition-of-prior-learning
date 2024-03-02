import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        gray: {
          DEFAULT: "#EBEBEB",
          light: "#EBEBEB",
          dark: "#323232",
        },
        white: "#FFFFFF",
        black: "#000000",
        blue: {
          DEFAULT: "#0d41d1",
          light: "#0f4beb",
          dark: "#0d41d1",
        },
      },
    },
    fontFamily: {
      sans: ["DM Sans", "sans-serif"],
    },
  },
  plugins: [],
};
export default config;
