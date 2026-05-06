const translations = {
    en: {
        title: "Mahoba Organic Market",
        shops: "Shops",
        cart: "Cart",
        search: "Search",
        search_placeholder: "Search products...",
        products: "Products",
        add_to_cart: "Add to Cart",
        featured: "Featured",
        organic: "100% Organic",
        payment: "Payment",
        total: "Total",
        proceed: "Proceed to Payment"
    },
    hi: {
        title: "महोबा जैविक बाजार",
        shops: "दुकानें",
        cart: "कार्ट",
        search: "खोजें",
        search_placeholder: "उत्पाद खोजें...",
        products: "उत्पाद",
        add_to_cart: "कार्ट में डालें",
        featured: "विशेष",
        organic: "100% जैविक",
        payment: "भुगतान",
        total: "कुल",
        proceed: "भुगतान करें"
    }
};

function setLanguage(lang) {
    localStorage.setItem("lang", lang);
    applyLanguage();
}

function applyLanguage() {
    const lang = localStorage.getItem("lang") || "en";

    document.querySelectorAll("[data-key]").forEach(el => {
        const key = el.getAttribute("data-key");

        if (translations[lang][key]) {
            if (el.tagName === "INPUT") {
                el.placeholder = translations[lang][key];
            } else {
                el.innerText = translations[lang][key];
            }
        }
    });
}

window.setLanguage = setLanguage;
document.addEventListener("DOMContentLoaded", applyLanguage);