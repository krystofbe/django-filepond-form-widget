# django-filepond-form-widget

A Django form widget using FilePond with image preview support.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Easy Integration**: Seamlessly integrates FilePond with Django forms.
- **Image Preview**: Provides image preview functionality out of the box.
- **Customization**: Configurable options to tailor the widget to your needs.
- **Responsive Design**: Ensures a responsive and user-friendly interface.
- **Simple Form Submission**: Focuses on regular file field submissions with forms, without handling server API endpoints.
- **Language Selection**: Automatically sets the locale based on the current language, ensuring the FilePond interface matches the user's language preferences.
- **Extensible**: Support for additional FilePond plugins planned for future releases.

Note: This widget is designed to work with standard form submissions. While FilePond's server property can be configured for API endpoints, this is beyond the scope of this project which aims to provide a simple form widget implementation.

## Installation
Install the package using pip:

```
pip install django-filepond-form-widget
```

Alternatively, you can install it from the repository:

```
pip install git+https://github.com/krystofbe/django-filepond-form-widget.git
```



## Usage
### Add to Installed Apps

Add `django_filepond_form_widget` to your `INSTALLED_APPS` in `settings.py`:

```
INSTALLED_APPS = [
    # ...
    'django_filepond_form_widget',
    # ...
]
```

### Include Static Files

Ensure that your templates include the necessary static files. Typically, this is handled automatically by the widget's media.

### Use the Widget in Forms

```
from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class ExampleForm(forms.Form):
    image = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": False}
        )
    )
```

### Create Views and Templates

```
from django.shortcuts import render
from .forms import ExampleForm


def upload_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle uploaded file
            return render(request, "example_app/success.html")
    else:
        form = ExampleForm()
    return render(request, "example_app/upload.html", {"form": form})
```
### File Size Validation

To enable file size validation, set the `allowFileSizeValidation` option to `True` in the widget's `config`. You can also configure the following options:

-   `minFileSize`: The minimum size of a file (e.g., "1KB", "2MB").
-   `maxFileSize`: The maximum size of a file (e.g., "5MB", "10MB").
-   `maxTotalFileSize`: The maximum total size of all files (e.g., "10MB", "20MB").
-   `labelMaxFileSizeExceeded`: Custom message when a file exceeds `maxFileSize`.
-   `labelMaxFileSize`: Custom message showing the max file size.
-   `labelMaxTotalFileSizeExceeded`: Custom message when total size exceeds `maxTotalFileSize`.
-   `labelMaxTotalFileSize`: Custom message showing the max total file size.

### Image Resize

To enable image resizing, set the `allowImageResize` option to `True` in the widget's `config`. You can also configure the following options:

- `imageResizeTargetWidth`: The target width of the resized image in pixels.
- `imageResizeTargetHeight`: The target height of the resized image in pixels.
- `imageResizeMode`: The resizing mode ('cover', 'contain', or 'force').
- `imageResizeUpscale`: Whether to upscale images smaller than the target size (true or false).
- 
Example:

```
from django import forms
from django_filepond_form_widget.widgets import FilePondWidget

class ExampleForm(forms.Form):
    image = forms.FileField(
        widget=FilePondWidget(
            config={
                "allowImagePreview": True,
                "allowMultiple": False,
                "allowFileSizeValidation": True,
                "maxFileSize": "5MB",
                "maxTotalFileSize": "10MB",
            }
        )
    )
```

## Example
An example project is provided to demonstrate how to integrate and run the widget.

### Run the Development Server

Navigate to the example directory and run the server using Uvicorn:

```
uv run python example/manage.py runserver
```

### Access the Application

Open your browser and navigate to `http://localhost:8000/upload/` to see the file upload form in action.

## Testing
This project uses pytest for testing. To run the tests:

### Install Development Dependencies

```
uv pip install -e ".[test]"   
```

### Run Tests

```
pytest
```

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear messages.
4. Submit a pull request detailing your changes.

## License
This project is licensed under the MIT License.
