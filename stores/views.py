from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .forms import StoreItemForm, StoreItem

from stores import models


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def create_store_item(request):
    form = StoreItemForm()
    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")

    context = {"form": form, }
    return render(request, 'create_store_item.html', context)


def update_store_item(request, item_id):
    print("HI")
    store_item = StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    if request.method == "POST":
        form = StoreItemForm(request.POST, instance=store_item)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")

    context = {
        "form": form,
        "store_item": {
            "id": store_item.id
        }
    }
    return render(request, 'update_store_item.html', context)


def delete_store_item(request, item_id):
    store_item = StoreItem.objects.get(id=item_id)
    store_item.delete()
    return redirect("store-item-list")
