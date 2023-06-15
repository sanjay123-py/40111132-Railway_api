from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_company(request):
    # Your code here
    url = 'http://104.211.219.98/train/register'
    data = {
        'companyName': 'Train 123',
        'ownerName': 'Sanjay',
        'rollNo': '40111132-CSE',
        'ownerEmail': 'sanjayreddy1270@gmail.com',
        'accessCode': 'siuzyt'
    }

    try:
        response = requests.post(url, json=data)
        response_data = response.json()
        return JsonResponse(response_data)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return JsonResponse({'error': error_message})
@csrf_exempt
def get_auth_token(request):
    url="http://104.211.219.98/train/auth"
    data={"companyName": "Train 123", 
          "clientID": "64f7e7f3-87a7-4a7e-94c0-033db2e7dff8",
          "clientSecret": "WmRncQZpTAzceEsI", 
          "ownerName": "Sanjay",
          "ownerEmail": "sanjayreddy1270@gmail.com", 
          "rollNo": "40111132-CSE"
          }
    try:
        response=requests.post(url,json=data)
        response_data = response.json()
        AUTH=response_data
        return JsonResponse(response_data)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return JsonResponse({'error': error_message})

@csrf_exempt
def get_trains(request):
    url = "http://104.211.219.98/train/trains"
    try:
        access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODY4NDE2NjYsImNvbXBhbnlOYW1lIjoiVHJhaW4gMTIzIiwiY2xpZW50SUQiOiI2NGY3ZTdmMy04N2E3LTRhN2UtOTRjMC0wMzNkYjJlN2RmZjgiLCJvd25lck5hbWUiOiIiLCJvd25lckVtYWlsIjoiIiwicm9sbE5vIjoiNDAxMTExMzItQ1NFIn0.PzTFElz3Fz1ADpAV6s-JqZ4z4kJO0h57cDSlM7yWce0"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return JsonResponse(response.json(),safe=False)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return JsonResponse({'error': error_message})

@csrf_exempt
def get_trains_ind(request):
    url = "http://104.211.219.98/train/trains/2344"
    try:
        access_token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODY4NDI4NDcsImNvbXBhbnlOYW1lIjoiVHJhaW4gMTIzIiwiY2xpZW50SUQiOiI2NGY3ZTdmMy04N2E3LTRhN2UtOTRjMC0wMzNkYjJlN2RmZjgiLCJvd25lck5hbWUiOiIiLCJvd25lckVtYWlsIjoiIiwicm9sbE5vIjoiNDAxMTExMzItQ1NFIn0.LEF7Ijkf_6TNBaw3bVP0R4sYuhHTu5gIzw37k5Y-qrU"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers)
        return JsonResponse(response.json(),safe=False)
    except Exception as e:
        error_message = f"An error occurred: {e}"
        return JsonResponse({'error': error_message})
