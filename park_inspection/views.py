from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

from django.shortcuts import render
from .models import Inspection, Park

def inspection_detail(request):
    # Retrieve the Inspection object from the database
    # inspection = Inspection.objects.get()

    # Prepare context data to be passed to the template
    # context = {
    #     'inspection': inspection,
    # }

    # Render the template with the provided context
    return render(request, 'park_inspection/inspection_detail.html')

# In your views.py file

from django.shortcuts import render, redirect
from .forms import InspectionForm

def create_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inspection_list')
    else:
        form = InspectionForm()

    return render(request, 'park_inspection/create_inspection.html', {'form': form})
# In your views.py file

from django.shortcuts import render, get_object_or_404
from .models import Inspection

def park_detail(request):
    # Retrieve the Park object from the database
    park = get_object_or_404(Inspection)

    # Prepare context data to be passed to the template
    context = {
        'park': park,
    }

    # Render the template with the provided context
    return render(request, 'park_inspection/park_detail.html'
    )

def home_page(request):
    inspections = Inspection.objects.all()
    parks = Park.objects.all()

    context = {
        'inspections': inspections,
        'parks': parks,
    }

    return render(request, 'park_inspection/home_page.html', context)

