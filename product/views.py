from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Item, Cart


class AddItemsForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
            queryset=Item.objects.all()
            )
    class Meta:
        model = Cart
        exclude = ["customer", "completed", "delivery"]


@login_required
def index(request):
    items = Item.objects.all()
    return render(request, 'product/index.html', {"items": items})


@login_required
def order(request):
    form = AddItemsForm(request.POST or None)
    items = Item.objects.all()
    if not form.is_valid():
        return render(request, 'product/order.html', {"form": form, "items": items})
    cart = request.user.cart_set.create()
    for item_id in request.POST.getlist("items"):
        item = Item.objects.get(id=item_id)
        cart.items.add(item)
    return redirect("product:cart")


class CartForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
            queryset=Item.objects.all()
            )
    class Meta:
        model = Cart
        exclude = ["customer", "completed"]


@login_required
def cart(request):
    cart = request.user.cart_set.filter(completed=False).last()
    form = CartForm(request.POST or None, instance=cart)
    if not form.is_valid():
        return render(request, "product/cart.html", {"form": form})
    for item in cart.items.all():
        cart.items.remove(item)
    for item_id in request.POST.getlist("items"):
        item = Item.objects.get(id=item_id)
        cart.items.add(item)
    instance = form.save(commit=False)
    instance.completed = True
    instance.save()
    return render(request, 'product/order_complete.html', {"total": cart.sum_amount,})
