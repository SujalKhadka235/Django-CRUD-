from django.shortcuts import render
from django.http import HttpResponse
import requests
import csv


def productsHome(request):
    url = "https://dummyjson.com/products"
    r = requests.get(url, stream=True)
    f = (line.decode("utf-8") for line in r.iter_lines())
    reader = csv.reader(f)
    print(reader)

    return HttpResponse("this is products page")


# Create your views here.
