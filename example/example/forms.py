from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ExampleForm(forms.Form):
    image_single = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": False}
        ),
        required=False,
    )
    image_multiple = MultipleFileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": True}
        ),
        required=False,
    )
    file_single = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": False, "allowMultiple": False}
        ),
        required=False,
    )
    file_multiple = MultipleFileField(
        widget=FilePondWidget(
            config={"allowImagePreview": False, "allowMultiple": True}
        ),
        required=False,
    )
    file_with_validation = forms.FileField(
        widget=FilePondWidget(
            config={
                "allowImagePreview": False,
                "allowMultiple": False,
                "allowFileSizeValidation": True,
                "maxFileSize": "5MB",
                "maxTotalFileSize": "10MB",
            }
        ),
        required=False,
    )
    image_with_resize_and_validation = forms.FileField(
        widget=FilePondWidget(
            config={
                "allowImagePreview": True,
                "allowMultiple": False,
                "allowFileSizeValidation": True,
                "maxFileSize": "2MB",
                "allowImageResize": True,
                "imageResizeTargetWidth": 200,
                "imageResizeTargetHeight": 200,
                "imageResizeMode": "cover",
                "imageResizeUpscale": False,
            }
        ),
        required=False,
    )
    file_with_type_validation = forms.FileField(
        widget=FilePondWidget(
            config={
                "allowFileTypeValidation": True,
                "acceptedFileTypes": ["image/png", "image/jpeg", "application/pdf"],
                "labelFileTypeNotAllowed": "Invalid file type. Please upload a PNG, JPEG, or PDF.",
                "fileValidateTypeLabelExpectedTypes": "Expects {allButLastType} or {lastType}",
                "fileValidateTypeLabelExpectedTypesMap": {
                    "image/jpeg": ".jpg",
                    "image/png": ".png",
                    "application/pdf": ".pdf",
                },
            }
        ),
        required=False,
    )
