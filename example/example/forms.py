from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class ExampleForm(forms.Form):
    image_single = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": False}
        ),
        required=False,
    )
    image_multiple = forms.FileField(
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
    file_multiple = forms.FileField(
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
