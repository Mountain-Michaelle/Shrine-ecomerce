from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreationForm
from cart.cart import Cart

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=['quantity'])
            #Clear the cart
            cart.clear()
            return render(request, 'order_create.html', {'order':order})
    else:
        form = OrderCreationForm()
        return render(request, 'order_create.html', {'cart':cart, 'form':form})