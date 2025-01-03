from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class ExampleForm(forms.Form):
    image = forms.FileField(
        widget=FilePondWidget(
            config={"allowImagePreview": True, "allowMultiple": False}
        )
    )
