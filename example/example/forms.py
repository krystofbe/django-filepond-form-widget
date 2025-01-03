from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class ExampleForm(forms.Form):
    image_single = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": False}
        )
    )
    image_multiple = forms.FileField(
        widget=FilePondWidget(config={"allowImagePreview": True, "allowMultiple": True})
    )
    file_single = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": False, "allowMultiple": False}
        )
    )
    file_multiple = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": False, "allowMultiple": True}
        )
    )
