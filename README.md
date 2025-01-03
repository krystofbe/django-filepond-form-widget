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
