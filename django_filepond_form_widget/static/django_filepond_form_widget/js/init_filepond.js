function initializeFilePond() {
  document.querySelectorAll(".filepond-input").forEach(function (input) {
    // Avoid initializing FilePond multiple times on the same input
    if (input._filePondInitialized) return;

    const configElement = document.getElementById(
      input.dataset.filepondConfigId
    );
    if (configElement) {
      try {
        const pondConfig = JSON.parse(configElement.textContent);

        if (pondConfig.allowImagePreview) {
          FilePond.registerPlugin(FilePondPluginImagePreview);
        }

        FilePond.create(input, pondConfig);

        // Mark as initialized
        input._filePondInitialized = true;
      } catch (error) {
        console.error(
          `Invalid JSON configuration for FilePond input with ID: ${input.id}`,
          error
        );
      }
    } else {
      console.warn(
        `Configuration element not found for FilePond input with ID: ${input.id}`
      );
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
