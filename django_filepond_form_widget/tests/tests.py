from django.test import TestCase
from django import forms
from django_filepond_form_widget.widgets import FilePondWidget


class FilePondWidgetTest(TestCase):
    def setUp(self):
        # Common setup for tests
        self.widget_id = "id_filepond_field"

    def test_default_media(self):
        """
        Test that the default media includes only the essential FilePond CSS and JS.
        """
        widget = FilePondWidget(attrs={"id": self.widget_id})
        expected_css = ["django_filepond_form_widget/css/filepond.min.css"]
        expected_js = ["django_filepond_form_widget/js/filepond.min.js"]
        self.assertEqual(widget.media._css["all"], expected_css)
        self.assertEqual(widget.media._js, expected_js)

    def test_media_with_image_preview(self):
        """
        Test that media includes image preview assets when allowImagePreview is True.
        """
        config = {"allowImagePreview": True}
        widget = FilePondWidget(attrs={"id": self.widget_id}, config=config)
        expected_css = [
            "django_filepond_form_widget/css/filepond.min.css",
            "django_filepond_form_widget/css/filepond-plugin-image-preview.min.css",
        ]
        expected_js = [
            "django_filepond_form_widget/js/filepond.min.js",
            "django_filepond_form_widget/js/filepond-plugin-image-preview.min.js",
        ]
        self.assertEqual(widget.media._css["all"], expected_css)
        self.assertEqual(widget.media._js, expected_js)

    def test_render_without_image_preview(self):
        """
        Test rendering the widget without image preview enabled.
        """
        widget = FilePondWidget(attrs={"id": self.widget_id})

        # Dynamically create a form class with the widget
        MyForm = type("MyForm", (forms.Form,), {"file": forms.FileField(widget=widget)})
        form = MyForm()
        rendered = form.as_p()

        # Check that FilePond.registerPlugin is not present
        self.assertNotIn("FilePond.registerPlugin", rendered)

        # Check that FilePond.create is present
        self.assertIn("FilePond.create(fileInput, pondConfig);", rendered)

    def test_render_with_image_preview(self):
        """
        Test rendering the widget with image preview enabled.
        """
        config = {"allowImagePreview": True}
        widget = FilePondWidget(attrs={"id": self.widget_id}, config=config)

        # Dynamically create a form class with the widget
        MyForm = type("MyForm", (forms.Form,), {"file": forms.FileField(widget=widget)})
        form = MyForm()
        rendered = form.as_p()

        # Check that FilePond.registerPlugin is present
        self.assertIn("FilePond.registerPlugin(FilePondPluginImagePreview);", rendered)

        # Check that FilePond.create is present
        self.assertIn("FilePond.create(fileInput, pondConfig);", rendered)

    def test_filepond_config_context(self):
        """
        Test that the widget correctly passes the configuration to the template context.
        """
        config = {"allowImagePreview": True, "maxFileSize": "2MB"}
        widget = FilePondWidget(attrs={"id": self.widget_id}, config=config)
        context = widget.get_context("file", None, {"id": self.widget_id})

        self.assertEqual(context["widget"]["filepond_config"], config)
        self.assertEqual(
            context["widget"]["filepond_config_id"], f"filepond_{self.widget_id}"
        )

    def test_filepond_config_id_generation(self):
        """
        Test that the filepond_config_id is generated correctly based on the widget's id.
        """
        custom_id = "custom_filepond_id"
        widget = FilePondWidget(attrs={"id": custom_id})
        context = widget.get_context("file", None, {"id": custom_id})

        self.assertEqual(
            context["widget"]["filepond_config_id"], f"filepond_{custom_id}"
        )

    def test_partial_media_inclusion(self):
        """
        Ensure that only specific media files are included based on partial config.
        """
        config = {"allowImagePreview": False}
        widget = FilePondWidget(attrs={"id": self.widget_id}, config=config)
        expected_css = ["django_filepond_form_widget/css/filepond.min.css"]
        expected_js = ["django_filepond_form_widget/js/filepond.min.js"]
        self.assertEqual(widget.media._css["all"], expected_css)
        self.assertEqual(widget.media._js, expected_js)

    def test_empty_config(self):
        """
        Test that an empty config does not cause any issues and defaults are used.
        """
        widget = FilePondWidget(attrs={"id": self.widget_id}, config={})
        expected_css = ["django_filepond_form_widget/css/filepond.min.css"]
        expected_js = ["django_filepond_form_widget/js/filepond.min.js"]
        self.assertEqual(widget.media._css["all"], expected_css)
        self.assertEqual(widget.media._js, expected_js)

    def test_multiple_config_options(self):
        """
        Test that multiple configuration options are handled correctly.
        """
        config = {"allowImagePreview": True, "allowMultiple": True, "maxFiles": 5}
        widget = FilePondWidget(attrs={"id": self.widget_id}, config=config)
        # Media should include image preview assets
        expected_css = [
            "django_filepond_form_widget/css/filepond.min.css",
            "django_filepond_form_widget/css/filepond-plugin-image-preview.min.css",
        ]
        expected_js = [
            "django_filepond_form_widget/js/filepond.min.js",
            "django_filepond_form_widget/js/filepond-plugin-image-preview.min.js",
        ]
        self.assertEqual(widget.media._css["all"], expected_css)
        self.assertEqual(widget.media._js, expected_js)

        # Dynamically create a form class with the widget
        MyForm = type("MyForm", (forms.Form,), {"file": forms.FileField(widget=widget)})
        form = MyForm()
        rendered = form.as_p()

        # Check that FilePond.registerPlugin is present
        self.assertIn("FilePond.registerPlugin(FilePondPluginImagePreview);", rendered)

        # Check that all configuration options are present in the rendered JavaScript
        self.assertIn('"allowImagePreview": true', rendered)
        self.assertIn('"allowMultiple": true', rendered)
        self.assertIn('"maxFiles": 5', rendered)
