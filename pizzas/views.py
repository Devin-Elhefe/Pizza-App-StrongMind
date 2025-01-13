from django.shortcuts import render, redirect
from .models import Topping, Pizza

def home(request):
    total_toppings = Topping.objects.count()
    total_pizzas = Pizza.objects.count()
    return render(request, 'home.html', {
        'total_toppings': total_toppings,
        'total_pizzas': total_pizzas
    })
                  

def pizza_list(request):
    pizzas = Pizza.objects.prefetch_related('toppings').all()
    return render(request, 'pizza_list.html', {'pizzas': pizzas})

def add_pizza(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        topping_ids = request.POST.getlist('toppings')
        
        if Pizza.objects.filter(name=name).exists():
            return render(request, 'add_pizza.html', {'error': 'Pizza name already exists', 'toppings': Topping.objects.all()})
        
        pizza = Pizza.objects.create(name=name)
        pizza.toppings.set(topping_ids)
        return redirect('pizza_list')
    
    return render(request, 'add_pizza.html', {'toppings': Topping.objects.all()})

def delete_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    pizza.delete()
    return redirect('pizza_list')

def update_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        topping_ids = request.POST.getlist('toppings')
        
        if Pizza.objects.filter(name=name).exclude(id=pizza_id).exists():
            return render(request, 'update_pizza.html', {
                'error': 'Pizza name already exists',
                'pizza': pizza,
                'toppings': Topping.objects.all()
            })
            
        pizza.name = name
        pizza.toppings.set(topping_ids)
        pizza.save()
        return redirect('pizza_list')
    
    return render(request, 'update_pizza.html', {'pizza': pizza, 'toppings': Topping.objects.all()})
0
def topping_list(request):
    toppings = Topping.objects.all()
    return render(request, 'topping_list.html', {'toppings': toppings})

def add_topping(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if not Topping.objects.filter(name=name).exists():
            Topping.objects.create(name=name)
        return redirect('topping_list')
    return render(request, 'add_topping.html')

def delete_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    topping.delete()
    return redirect('topping_list')

def update_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if not Topping.objects.filter(name=name).exclude(id=topping_id).exists():
            topping.name = name
            topping.save()
        return redirect('topping_list')
    return render(request, 'update_topping.html', {'topping': topping})





