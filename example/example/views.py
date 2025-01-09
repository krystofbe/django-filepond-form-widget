from django.shortcuts import render
from .forms import ExampleForm


def upload_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = []
            for field_name in form.fields:
                if field_name in request.FILES:
                    field_files = request.FILES.getlist(field_name)
                    if isinstance(field_files, list):
                        uploaded_files.extend(field_files)
                    else:
                        uploaded_files.append(field_files)

            return render(
                request, "example_app/success.html", {"files": uploaded_files}
            )
    else:
        form = ExampleForm()
    return render(request, "example_app/upload.html", {"form": form})
