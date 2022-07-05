
import json

from venv import create

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog
# Create your views here.

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        #name = data['name']
        #email = data['email']
        #age = data['age']
        Owner.objects.create(name = data['name'], email = data['email'], age = data['age'])
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            dogs = list(Dog.objects.values('name', 'age').filter(owner = owner.id))
            results.append(
                {
                    'name': owner.name,
                    'email' : owner.email,
                    'age': owner.age,
                    'dog': dogs
                }
            )
        return JsonResponse({'result':results}, status=200)

class DogView(View):
    def post(self, request):
        dogs = json.loads(request.body)
        name = dogs['name']
        age = dogs['age']
        owner = Owner.objects.get(name = dogs['owner'])
        Dog.objects.create(name = name, age = age, owner = owner)
        return JsonResponse({'messasge':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
            {
                "name" : dog.name,
                "age" : dog.age,
                "owner" : dog.owner.name,
            }
        )
        return JsonResponse({'result':results}, status=200)

            








