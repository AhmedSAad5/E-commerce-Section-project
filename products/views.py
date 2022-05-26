from django.shortcuts import redirect, render
from.models import Category, Order,Product
# from django.contrib.auth.models import User ,Order
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    allcategory = Category.objects.all()
    allproducts = Product.objects.all()
    return render(request, 'pages/home.html', {'allcategory':allcategory,'allproducts':allproducts})



def category(request, categoryid):
    allcategory = Category.objects.all()
    E_category = Category.objects.get(id=categoryid)
    allproducts = Product.objects.all().filter(category_id = categoryid)
    return render(request, 'pages/category.html', {'allcategory':allcategory,'allproducts':allproducts,'E_category':E_category})



def Product(request, productid):
    allcategory = Category.objects.all()
    E_product = Product.objects.get(id=productid)
    return render(request, 'pages/product.html', {'allcategory':allcategory,'E_product':E_product})


def newproducts(request):
    allcategory = category.objects.all()
    # allproducts = Product.objects.all().order_by("-id")
    return render(request,'pages/newproducts.html',{"allcategory":allcategory})

# Add to cart
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

# Delete from cart
@login_required(login_url='/login/')
def deleteitem(request,proid):
    item=Order.objects.get(id=proid)
    item.delete()
    return redirect("/cartitem/")

# Show the cart
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





    





