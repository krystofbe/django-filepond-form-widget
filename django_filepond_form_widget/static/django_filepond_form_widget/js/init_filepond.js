async function initializeFilePond() {
  const localeFiles = {
    "am-ET": "am-et.js",
    "ar-AR": "ar-ar.js",
    "az-AZ": "az-az.js",
    "ca-CA": "ca-ca.js",
    "cs-CZ": "cs-cz.js",
    "da-DK": "da-dk.js",
    "de-DE": "de-de.js",
    "el-EL": "el-el.js",
    "en-EN": "en-en.js",
    "en-US": "en-en.js", // Map en-US to en-en.js
    "es-ES": "es-es.js",
    "fa-IR": "fa_ir.js", // Note the underscore
    "fi-FI": "fi-fi.js",
    "fr-FR": "fr-fr.js",
    "he-HE": "he-he.js",
    "hr-HR": "hr-hr.js",
    "hu-HU": "hu-hu.js",
    "id-ID": "id-id.js",
    "it-IT": "it-it.js",
    "ja-JA": "ja-ja.js",
    "km-KM": "km-km.js",
    "ko-KR": "ko-kr.js",
    "lt-LT": "lt-lt.js",
    "lv-LV": "lv-lv.js",
    "no-NB": "no_nb.js", // Note the underscore
    "nl-NL": "nl-nl.js",
    "pl-PL": "pl-pl.js",
    "pt-BR": "pt-br.js",
    "pt-PT": "pt-pt.js",
    "ro-RO": "ro-ro.js",
    "sk-SK": "sk-sk.js",
    "sv-SE": "sv_se.js", // Note the underscore
    "tr-TR": "tr-tr.js",
    "uk-UA": "uk-ua.js",
    "vi-VI": "vi-vi.js",
    "zh-CN": "zh-cn.js",
    "zh-TW": "zh-tw.js",
  };

  document.querySelectorAll(".filepond-input").forEach(async function (input) {
    if (input._filePondInitialized) return;

    const configElement = document.getElementById(
      input.dataset.filepondConfigId
    );
    const langCode = input.dataset.locale || "en-us";
    const normalizedLangCode = langCode.toUpperCase();
    const localeFile =
      localeFiles[normalizedLangCode] ||
      localeFiles[
        Object.keys(localeFiles).find((key) =>
          key.startsWith(normalizedLangCode.split("-")[0])
        )
      ] ||
      "en-en.js";

    try {
      const module = await import(`../locale/${localeFile}`);
      window.FilePondLocale = module.default;
    } catch (error) {
      console.error(`Failed to load locale file: ${localeFile}`, error);
    }

    if (configElement) {
      try {
        const pondConfig = JSON.parse(configElement.textContent);

        if (window.FilePondLocale) {
          FilePond.setOptions(window.FilePondLocale);
        }

        if (pondConfig.allowImagePreview) {
          FilePond.registerPlugin(FilePondPluginImagePreview);
        }

        FilePond.create(input, pondConfig);
        input._filePondInitialized = true;
      } catch (error) {
        console.error(
          `Invalid JSON configuration for FilePond input with ID: ${input.id}`,
          error
        );
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", initializeFilePond);

// Listen to htmx events to re-initialize FilePond on dynamically loaded content
document.addEventListener("htmx:afterSwap", function (event) {
  // Only proceed if the swapped content is part of a target that may contain FilePond inputs
  // Adjust the selector or conditions as needed based on your htmx usage
  initializeFilePond();
});
