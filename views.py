from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder


from django.contrib import messages
from django.contrib.auth import login, authenticate


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm




# filters.py
from django import template


register = template.Library()

@register.filter
def convert_to_inr(price_in_usd, exchange_rate=75.0):
    try:
        price_in_usd = float(price_in_usd)
        return "₹{:,.2f}".format(price_in_usd * exchange_rate)
    except (ValueError, TypeError):
        return price_in_usd







def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    # Ensure cartItems is in the context
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    
    return render(request, 'store/cart.html', context)



def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Define the exchange rate (1 USD to INR)
    exchangeRate = 75.0

    # Update the price_inr for each product in the cart
    for item in items:
        item.product.price_inr = item.product.price * exchangeRate
        item.price_inr = item.product.price_inr  # Set the price_inr for the item

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'exchangeRate': exchangeRate,
    }
    return render(request, 'store/cart.html', context)









def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Define the exchange rate (1 USD to INR)
    exchangeRate = 75.0

    # Update the price_inr for each product in the cart
    for item in items:
        item.product.price_inr = item.product.price * exchangeRate

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)



def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Define the exchange rate (1 USD to INR)
    exchangeRate = 75.0

    # Update the price_inr for each product in the cart
    for item in items:
        item.product.price_inr = item.product.price * exchangeRate

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'exchangeRate': exchangeRate,  # Pass the exchange rate to the template
    }
    return render(request, 'store/cart.html', context)




def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # Update price_inr for each item
    for item in items:
        item.product.price_inr = item.product.price * Decimal('75.0')
        item.get_total_inr = item.product.price_inr * item.quantity

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)



from .models import Product  # Import your Product model

def product_list(request):
    # Define the exchange rate
    exchange_rate = 75.0  # Replace with the actual exchange rate (1 USD to INR)

    # Fetch the list of products
    products = Product.objects.all()

    # Update product prices in INR
    for product in products:
        product.price_inr = product.price * exchange_rate

    # Pass the updated product list to the template
    return render(request, 'your_template.html', {'products': products})

from django.shortcuts import render
from .models import Product

def cart(request):
    # Fetch the products from the database
    products = Product.objects.all()

    # Define the exchange rate (1 USD to INR)
    exchangeRate = 75.0

    # Set the price_inr attribute for each product
    for product in products:
        product.price_inr = product.price * exchangeRate

    # Pass the products to the template context
    context = {
        'products': products,
    }

    return render(request, 'store/cart.html', context)








from decimal import Decimal  



def cart(request):
    # Your code for handling the cart
    # Make sure that each product in the cart has the 'price_inr' attribute set

 def checkout(request):
    # Your code for handling the checkout
    # When rendering the checkout page, make sure the products in the cart have 'price_inr' set
    # Example:
    cart_items = cart.get_cart_items()
    for item in cart_items:
        item.product.price_inr = item.product.price * Decimal('75.0')
    # Render the checkout page



















from decimal import Decimal  # Import Decimal for precise float calculations

def add_to_cart(request, product_id):
    # Retrieve the product
    product = YourProductModel.objects.get(id=product_id)
    
    # Set the price_inr attribute based on your conversion rate
    exchangeRate = Decimal('75.0')  # Use Decimal for precise float calculations
    product.price_inr = product.price * exchangeRate
    
    # Add the product to the cart
    cart.add(product)
    
    # Redirect or respond as needed



















def add_to_cart(request, product_id):
    # Retrieve the product
    product = YourProductModel.objects.get(id=product_id)
    
    # Set the price_inr attribute based on your conversion rate
    exchangeRate = 75.0  # Replace with your actual exchange rate
    product.price_inr = product.price * exchangeRate
    
    # Add the product to the cart
    cart.add(product)
    
    # Redirect or respond as needed
















def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('main')  # Redirect to the main page
            else:
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'Invalid form data. Please check your input.')
    else:
        form = LoginForm()

    return render(request, 'store/access.html', {'form': form})







































def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('main')  # Redirect to the main page
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'store/access.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if the user exists and the credentials are valid
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('main')  # Redirect to the main page
        else:
            messages.error(request, 'Invalid login credentials.')
    
    return render(request, 'store/access.html')
















def join_view(request):
    # Your view logic goes here
    if request.method == 'POST':
        # Your signup logic here
        # Assuming the signup was successful:
        messages.success(request, 'Signed up successfully!')

    return render(request, 'store/join.html')

def access_view(request):
    # Your view logic goes here
    if request.method == 'POST':
        # Your login logic here
        # Assuming the login was successful:
        messages.success(request, 'Logged in successfully!')

    return render(request, 'store/access.html')

















































def join_view(request):
    if request.method == 'POST':
        # Your signup logic here
        # Ensure the username and password are unique
        # After successful signup, you can use Django's built-in login method to log the user in.
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Signed up successfully as {user.username}!")
        else:
            messages.error(request, "Signup failed. Please check your credentials.")
    return render(request, 'store/join.html')

def access_view(request):
    if request.method == 'POST':
        # Your login logic here
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Logged in successfully as {user.username}!")
        else:
            messages.error(request, "Login failed. Please check your credentials.")
    return render(request, 'store/access.html')


























def join_view(request):
    # Your view logic goes here
    return render(request, 'store/join.html')

def access_view(request):
    # Your view logic goes here
    return render(request, 'store/access.html')






def register(request):
    return render(request, 'store/register.html')


def login(request):
    return render(request, 'store/login.html')













































































































def login(request):
    return render(request, 'store/login.html')


def signup(request):
    return render(request, 'store/signup.html')
































def login(request):
    return render(request, 'D:\IZ\django_ecommerce_mod5\store\templates\store\login.html')


def signup(request):
    return render(request, 'D:\IZ\django_ecommerce_mod5\store\templates\store\signup.html')


def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')







def login_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/login.html')  # Corrected template path

# View function for signup
def signup_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/signup.html')  











def signup_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/signup.html')  # Corrected template path

def login_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/login.html')  # Corrected template path



















def login(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/login.html')

def signup(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'store/signup.html')



def login(request):
    return render(request, 'store/login.html')











def login_view(request):
    return render(request, 'store/login.html')

def signup_view(request):
    return render(request, 'store/signup.html')



def home(request):
    return render(request, 'store/home.html')

def about(request):
    
    return render(request, 'store/about.html')





def contact(request):
       return render(request, 'store/contact.html')
   



def signup_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        # Implement logic for handling the form data
        pass
    return render(request, 'login.html')

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

# Additional view functions for your project can be added here

# Example view function for product detail page
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# Example view function for updating cart items
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('Item was added', safe=False)

# Example view function for processing orders
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)
    
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    
    if total == order.get_cart_total:
        order.complete = True
    order.save()
    
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
    
    return JsonResponse('Payment submitted..', safe=False)
