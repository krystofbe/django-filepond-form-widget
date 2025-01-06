async function initializeFilePond() {
  const localeFiles = {
    "am-et": "am-et.js",
    "ar-ar": "ar-ar.js",
    "az-az": "az-az.js",
    "ca-ca": "ca-ca.js",
    "cs-cz": "cs-cz.js",
    "da-dk": "da-dk.js",
    "de-de": "de-de.js",
    "el-el": "el-el.js",
    "en-en": "en-en.js",
    "en-us": "en-en.js", // map en-us to en-en.js
    "es-es": "es-es.js",
    "fa-ir": "fa_ir.js", // note the underscore
    "fi-fi": "fi-fi.js",
    "fr-fr": "fr-fr.js",
    "he-he": "he-he.js",
    "hr-hr": "hr-hr.js",
    "hu-hu": "hu-hu.js",
    "id-id": "id-id.js",
    "it-it": "it-it.js",
    "ja-ja": "ja-ja.js",
    "km-km": "km-km.js",
    "ko-kr": "ko-kr.js",
    "lt-lt": "lt-lt.js",
    "lv-lv": "lv-lv.js",
    "no-nb": "no_nb.js", // note the underscore
    "nl-nl": "nl-nl.js",
    "pl-pl": "pl-pl.js",
    "pt-br": "pt-br.js",
    "pt-pt": "pt-pt.js",
    "ro-ro": "ro-ro.js",
    "sk-sk": "sk-sk.js",
    "sv-se": "sv_se.js", // note the underscore
    "tr-tr": "tr-tr.js",
    "uk-ua": "uk-ua.js",
    "vi-vi": "vi-vi.js",
    "zh-cn": "zh-cn.js",
    "zh-tw": "zh-tw.js",
  };

  document.querySelectorAll(".filepond-input").forEach(async function (input) {
    if (input._filePondInitialized) return;

    const configElement = document.getElementById(
      input.dataset.filepondConfigId
    );
    const langCode = input.dataset.locale || "en-us";
    const normalizedLangCode = langCode.toLowerCase();
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
