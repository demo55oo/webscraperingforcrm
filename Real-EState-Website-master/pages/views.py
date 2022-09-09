from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor 
from listings.choices import price_choices, bedroom_choices, state_choices
from autoscraper.auto_scraper import AutoScraper
import requests
from bs4 import BeautifulSoup
import json


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_data').filter(is_published=True)[:3]

    url ='https://mobile.fmcsa.dot.gov/qc/services/carriers/name/greyhound?webKey=f9d9a84990f7f4a5b72ebba8ccdb7bb861a44eff'
    url1 ='https://mobile.fmcsa.dot.gov/qc/services//carriers/docket-number/117719?webKey=f9d9a84990f7f4a5b72ebba8ccdb7bb861a44eff'
    # We can add one or multiple candidates here.
    # You can also put urls here to retrieve urls.
    res = requests.get(url)
    response_dict = json.loads(res.text)

    result = response_dict
    print(res.content)
    context ={
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'result':result
    }
    return render(request, 'pages/index.html', context)

def index1(request):
    response=requests.get('https://api.covid19api.com/countries').json()
    return render(request,'pages/index.html',{'response':response})

def about(request):
    realtors=Realtor.objects.order_by('-hire_date')

    mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

    context= {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }


    return render(request, 'pages/about.html', context)
