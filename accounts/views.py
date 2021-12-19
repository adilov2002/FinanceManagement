from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Purchases, Categories, Items


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='login')
def categories(request):
    group = None

    if request.user.groups.exists():
        group = request.user.groups.all()[0].name

    if group in 'user':
        return redirect('profile')
    if group in 'admin':
        return render(request, '')


@login_required(login_url='login')
def purchases(request):
    if request.method == 'POST':
        if "addTransaction" in request.POST:
            user = request.user
            category = request.POST['category']
            cat = Categories.objects.get(name=category)
            name = request.POST['name']
            price = request.POST['price']
            date = request.POST['date']
            item = Items.objects.create(name=name, price=price, category_id=cat.id)
            purchase = Purchases.objects.create(user=user, item_id=item.id, date=date)
            return redirect('/accounts/purchases')
        elif "updateTransaction" in request.POST:
            user = request.user
            purchase_id = request.POST['purchase_id']
            item_id1 = request.POST['item_id']
            category = request.POST['category']
            cat = Categories.objects.get(name=category)
            name = request.POST['name']
            price = request.POST['price']
            date = request.POST['date']
            Items.objects.filter(id=item_id1).update(name=name, price=price, category_id=cat.id)
            item = Items.objects.get(id=item_id1)
            purchase = Purchases.objects.filter(id=purchase_id).update(user=user, item_id=item.id, date=date)
            return redirect('/accounts/purchases')

    category_list = list(Categories.objects.values_list('name', flat=True))
    purchase_data = Purchases.objects.filter(user__username=request.user.username)
    cat = list(Purchases.objects.values_list('item__category__name', flat=True).distinct())
    # cats = list(Purchases.objects.values_list('item__category__name', flat=True))
    date = list(Purchases.objects.values_list('date', flat=True).distinct())


    datas = []
    for d in sorted(date):
        datas.append(d.__str__())

    # datas = list(set(datas))
    chart_data = []
    for c in datas:
        # chart_data.append(sum(list(purchase_data.filter(item__category__name=c).values_list('item__price', flat=True))))
        chart_data.append(sum(list(purchase_data.filter(date=c).values_list('item__price', flat=True))))

    data = {
        'purchases': purchase_data,
        'chart_data': chart_data,
        'cat': cat,
        'category_list': category_list,
        'date': datas,
    }
    return render(request, 'purchases.html', data)
