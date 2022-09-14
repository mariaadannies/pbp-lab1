from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

def show_wishlist(request):
    return render(request, "wishlist.html",context)

def show_wishlist_xml(request):
    data = BarangWishlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_wishlist_json_id(request):
    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Maria'
}

