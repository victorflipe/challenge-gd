/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {

            fontFamily:{
                newsreader: ["Newsreader", "serif"]
            },

            colors:{
                // background: "hsl(var(--background))",
                // foreground: "hsl(var(--foreground))",
                greenColor1: "#67A22D",
                greenColor2: "#73964F",
                greenLight: "#EDF2E8",
                blackColor: "#141C0D",
                whiteColor1: "#FAFCF7",
                whiteColor2: "#E5E8EB"
            }
        },
    },
    plugins: [],
};