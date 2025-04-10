from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import auth
from .models import FirebaseUser

def home(request):
    return render(request, 'home.html')  # This serves your HTML

@csrf_exempt
def verify_token(request):
    if request.method == 'POST':
        try:
            auth_header = request.headers.get('Authorization', '')
            token = auth_header.split(' ')[1]
            decoded = auth.verify_id_token(token)

            uid = decoded.get('uid')
            name = decoded.get('name', '')
            email = decoded.get('email', '')
            picture = decoded.get('picture', '')

            user, created = FirebaseUser.objects.update_or_create(
                uid=uid,
                defaults={'name': name, 'email': email, 'picture': picture}
            )

            return JsonResponse({
                'message': 'User authenticated and saved',
                'uid': uid,
                'created': created
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)
    return JsonResponse({'error': 'Invalid request'}, status=400)
