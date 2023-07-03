from django.shortcuts import render

# Create your views here.
from save.models import AnyData


def save_date(request):

    save_data = AnyData(data=125)
    save_data.save()

    return render(request, 'save.html')