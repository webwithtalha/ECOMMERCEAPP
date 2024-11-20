# myapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import products , users

# Render the home page
def hello(request):
    return render(request, 'home.html')

# Render the login page
def login_view(request):
    return render(request, 'loginSignup.html')

#<------- CRUD operations for user --------->
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = users.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            password=data.get('password')
        )
        return JsonResponse({'id': user.id, 'name': user.name})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    

def get_users(request):
    if request.method == 'GET':
        user_list = list(users.objects.values())
        return JsonResponse(user_list, safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)
    

@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = users.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except users.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)
    
@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            user = users.objects.get(id=user_id)
            data = json.loads(request.body)
            user.name = data.get('name', user.name)
            user.email = data.get('email' , user.email)
            user.password = data.get('password' , user.password)
            user.save()
            return JsonResponse({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password
            })
        except users.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)    


#<------- CRUD operations for products --------->
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = products.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )
        return JsonResponse({'id': product.id, 'name': product.name})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt    
def get_products(request):
    if request.method == 'GET':
        product_list = list(products.objects.values())
        return JsonResponse(product_list, safe=False)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)

@csrf_exempt    
def delete_product(request, product_id):
    if request.method == 'DELETE':
        try:
            product = products.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'})
        except products.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)
    
@csrf_exempt
def update_product(request, product_id):
    if request.method == 'PUT':
        try:
            product = products.objects.get(id=product_id)
            data = json.loads(request.body)
            product.name = data.get('name', product.name)
            product.description = data.get('description' , product.description)
            product.price = data.get('price' , product.price)
            product.save()
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': str(product.price)
            })
        except products.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'}, status=404)
        
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)    
            