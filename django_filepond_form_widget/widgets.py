from django import forms


class FilePondWidget(forms.ClearableFileInput):
    template_name = "django_filepond_form_widget/filepond_widget.html"

    def __init__(self, attrs=None, config=None):
        # app .filepond-input to the widget attrs class
        if attrs is None:
            attrs = {}
        attrs["class"] = "filepond-input"

        super().__init__(attrs)
        self.config = config or {}
        self.config["storeAsFile"] = True

    @property
    def media(self):
        css = {"all": ["django_filepond_form_widget/css/filepond.min.css"]}
        js = ["django_filepond_form_widget/js/filepond.min.js"]

        if self.config.get("allowImagePreview"):
            css["all"].append(
                "django_filepond_form_widget/css/filepond-plugin-image-preview.min.css"
            )
            js.append(
                "django_filepond_form_widget/js/filepond-plugin-image-preview.min.js"
            )

        js.append("django_filepond_form_widget/js/init_filepond.js")

        return forms.Media(css=css, js=js)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["filepond_config"] = self.config
        context["widget"]["filepond_config_id"] = (
            f"filepond_config_{context['widget']['attrs']['id']}"
        )
        return context
