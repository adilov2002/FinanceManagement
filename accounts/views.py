from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Purchases, Categories, Items, Income


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
        elif "deleteTransaction" in request.POST:
            purchase_id = request.POST['purchase_id']
            item_id1 = request.POST['item_id']
            Items.objects.filter(id=item_id1).delete()
            Purchases.objects.filter(id=purchase_id).delete()
            return redirect('/accounts/purchases')
        elif "addIncome" in request.POST:
            user = request.user
            price = request.POST['price']
            date = request.POST['date']
            Income.objects.create(user=user, price=price, date=date)
            return redirect('/accounts/purchases')
        elif "updateIncome" in request.POST:
            user = request.user
            price = request.POST['price']
            date = request.POST['date']
            income_id = request.POST['income_id']
            Income.objects.filter(id=income_id).update(user=user, price=price, date=date)
            return redirect('/accounts/purchases')
        elif "deleteIncome" in request.POST:
            income_id = request.POST['income_id']
            Income.objects.filter(id=income_id).delete()
            return redirect('/accounts/purchases')

    category_list = list(Categories.objects.values_list('name', flat=True))
    purchase_data = Purchases.objects.filter(user__username=request.user.username)
    cat = list(Purchases.objects.values_list('item__category__name', flat=True).distinct())
    date1 = list(Purchases.objects.values_list('date', flat=True).distinct())

    # expense
    datas = []
    for d in sorted(date1):
        datas.append(d.__str__())

    # income
    incomes = Income.objects.filter(user__username=request.user.username)
    income_data = sorted(incomes.values_list('date', flat=True).distinct())
    income_days = []
    for d in income_data:
        income_days.append(d.__str__())

    income_sum = []
    for day in income_days:
        income_sum.append(sum(incomes.filter(date=day).values_list('price', flat=True)))

    merged_datas = sorted(set(datas + income_days))
    correct_income = []
    expense = []
    sum_income = 0
    sum_expense = 0
    for d in merged_datas:
        if d not in income_days:
            correct_income.append(0)
        else:
            correct_income.append(sum(incomes.filter(date=d).values_list('price', flat=True)))
            sum_income += sum(incomes.filter(date=d).values_list('price', flat=True))
        if d not in datas:
            expense.append(0)
        else:
            expense.append(sum(list(purchase_data.filter(date=d).values_list('item__price', flat=True))))
            sum_expense += sum(list(purchase_data.filter(date=d).values_list('item__price', flat=True)))

    merged_tables = list(list(purchase_data) + list(incomes))
    merged_tables.sort(key=lambda d: d.date)

    diff = []
    prev_income = 0
    for d1, d2 in zip(correct_income, expense):
        diff.append(d1 - d2)

    data = {
        'purchases': merged_tables,
        'income_days': income_days,
        'expense': expense,
        'income': correct_income,
        'cat': cat,
        'diff': diff,
        'category_list': category_list,
        'date': merged_datas,
        'sum_income': sum_income,
        'sum_expense': sum_expense
    }
    return render(request, 'purchases.html', data)
