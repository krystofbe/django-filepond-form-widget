
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
