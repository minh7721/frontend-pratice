tailwind.config = {
  theme: {
    extend: {
      colors: {
        xanhLaDam: '#007882',
        mauChu: '#3B4144',
        mauDo: '#D93C23',
      },
    },
    borderRadius: {
        '36px' : '36px',
        'none': '0',
        'sm': '0.125rem',
        DEFAULT: '0.25rem',
        DEFAULT: '4px',
        'md': '0.375rem',
        'lg': '0.5rem',
        'full': '9999px',
        'large': '12px',
      },
      screens: {
        'sm': '375px',
        // => @media (min-width: 640px) { ... }
  
        'md': '768px',
        // => @media (min-width: 768px) { ... }
  
        'lg': '1024px',
        // => @media (min-width: 1024px) { ... }
  
        'xl': '1280px',
        // => @media (min-width: 1280px) { ... }
  
        '2xl': '1536px',
        // => @media (min-width: 1536px) { ... }
      }
  },
};


const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");
const btnCloseHeader = document.getElementById('btnCloseHeader');
const text__reviewNha = document.getElementById('text__reviewNha');
btn.addEventListener("click", () => {
if (btn.style.display === "none") {
btn.style.display = "block";
btnCloseHeader.style.display = "none";
text__reviewNha.style.display = "block";
menu.classList.toggle("hidden");
} else {
btn.style.display = "none";
btnCloseHeader.style.display = "block";
text__reviewNha.style.display = "none";
menu.classList.toggle("hidden");
}
});

btnCloseHeader.addEventListener("click", () => {
if (btnCloseHeader.style.display === "none") {
btn.style.display = "none";
btnCloseHeader.style.display = "block";
text__reviewNha.style.display = "none";
menu.classList.toggle("hidden");
} else {
btn.style.display = "block";
btnCloseHeader.style.display = "none";
text__reviewNha.style.display = "block";
menu.classList.toggle("hidden");
}
});