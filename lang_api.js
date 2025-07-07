
let lang = "en";

function loadLanguage(langCode) {
  fetch("lang_data.json")
    .then(response => response.json())
    .then(data => {
      for (const key in data) {
        const el = document.querySelector(`[data-key="${key}"]`);
        if (el) el.textContent = data[key][langCode] || data[key]["en"];
      }
    });
}

function setLang(code) {
  lang = code;
  loadLanguage(lang);
}
