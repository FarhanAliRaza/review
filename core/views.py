from email.mime import image
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
import csv
from app.settings import BASE_DIR, BASE_URL

from django.utils import timezone
from core.models import *


def index(request):
    stores = Store.objects.all()
  
    
    return render(request, 'index.html', {'stores' : stores})



def review(request, id):
    s = get_object_or_404(Store, pk=id)
  
    
    return render(request, 'review.html', {'s' : s})


def review_store(request):
    id = request.POST.get('store_id')
    feel = request.POST.get('review')

    img = request.FILES.get('image')
    print(img, " image")
    c = Customer.objects.create(store_id = id, feel = feel, image = img)
    s = get_object_or_404(Store, pk=id)
    if feel == "happy":
        print(feel)
        s.happy += 1
        s.customer.add(c)
        s.save()
    elif feel == "sad":
        print(feel)
        s.customer.add(c)
        s.sad += 1
        s.save()
    elif feel == "neutral":
        print(feel)
        s.customer.add(c)

        s.neutral += 1
        s.save()
    elif feel == "satisfied":
        print(feel)
        s.customer.add(c)

        s.satisfied += 1
        s.save()
    else:
        return JsonResponse({'success': False})

  
    return JsonResponse({'success': True})



def admin_view(request):

    return render(request, 'admin_view.html', {})

@login_required(login_url='/admin/login/?next=/download_customer_csv/')
def download_customer_csv(request):
    output = []
    query_set = Customer.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="customers.csv"'},
    )
    writer = csv.writer(response)


    # write the header
    writer.writerow(['Customer ID', 'Feeling', 'Store ID', 'Store Name', 'Image URL', 'Created'])
    for c in query_set:
        s = Store.objects.get(id=c.store_id)
        writer.writerow([c.id, c.feel, c.store_id, s.name , BASE_URL + c.image.url, c.created])
    return response




@login_required(login_url='/admin/login/?next=/download_store_csv/')
def download_store_csv(request):
    output = []
    query_set = Store.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="customers.csv"'},
    )
    writer = csv.writer(response)

    # write the header
    writer.writerow(['Store ID', 'Store Name' 'Happy', 'Satisfied', 'Neutral', 'Sad', 'Store Image URL'])
    for c in query_set:
        writer.writerow([c.id, c.name, c.happy, c.satisfied , c.neutral , c.sad , BASE_URL + c.logo.url if c.logo else ''])
    return response