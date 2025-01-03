from django.shortcuts import render
from .forms import ExampleForm


def upload_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve files from each field
            image_single = request.FILES.get("image_single")
            image_multiple = request.FILES.getlist("image_multiple")
            file_single = request.FILES.get("file_single")
            file_multiple = request.FILES.getlist("file_multiple")

            # Combine all uploaded files into a single list
            uploaded_files = []
            if image_single:
                uploaded_files.append(image_single)
            uploaded_files.extend(image_multiple)
            if file_single:
                uploaded_files.append(file_single)
            uploaded_files.extend(file_multiple)

            return render(
                request, "example_app/success.html", {"files": uploaded_files}
            )
    else:
        form = ExampleForm()
    return render(request, "example_app/upload.html", {"form": form})
