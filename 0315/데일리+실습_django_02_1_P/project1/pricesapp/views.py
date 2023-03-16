from django.shortcuts import render

# Create your views here.
def price(request,name,count):
    product_price = {
        "라면":980,
        "홈런볼":1500,
        "칙촉":2300, 
        "식빵":1800
        }
    if name in product_price:
        total = product_price[name] * count
    else:
        total = 0
    context = {
        'name':name,
        'count':count,
        'price':total,
    }
    return render(request, 'pricesapp/price.html',context)
