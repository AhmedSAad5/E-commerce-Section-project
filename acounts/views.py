from itertools import product
from django.shortcuts import  render, redirect

from products.models import Product
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.models import User ,Order
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="pages/signup.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="pages/login.html", context={"login_form":form})

@login_required(login_url='/Login/')
def addcart(request,proid):
    quantity=int(Order.objects.filter(productid=proid).count())
    if quantity >= 1:
        De=Order.objects.get(productid=proid)
        Order.objects.filter(productid=proid).update(num=int(De.num)+1)
    else:
        id = request.user.id
        carts=Order(productid=proid,user_id=id,num=1)
        carts.save()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def deleteitem(request,proid):
    item=Order.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

@login_required(login_url='/login/')
def cartitem(request):
    quantity = 0
    price =0
    products = Product.objects.all()
    orders = Order.objects.filter(user_id=request.user.id)
    for i in orders:
        quantity=quantity+int(i.num)
        for j in Product.objects.all():
            if i.productid ==j.id:
                price =price +(int(j.price)*int(i.num))
    return render(request, 'pages/cartitem.html',{"products":products,'quantity':quantity,"price":price,"orders":orders})


