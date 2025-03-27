from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import OTP

import json
import os
# Import the regular expression module

import google.generativeai as genai

from .models import ChatMessage, OTP

# Configure the Gemini API with your API key
# It's better to configure this in your settings.py file and access it from there
# For example, in settings.py:
# GEMINI_API_KEY = os.environ.get("AIzaSyAkfG0wiq23BnTP38RFnpxGJqxRU3RLD4o")
#
# Then in your views.py:
# genai.configure(api_key=settings.GEMINI_API_KEY)
genai.configure(api_key=os.environ.get("AIzaSyAkfG0wiq23BnTP38RFnpxGJqxRU3RLD4o"))

# Select the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-01-21')

@csrf_exempt
def chat_with_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            message = data.get('message')
            if not message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            chat = model.start_chat()
            response = chat.send_message(message)  # Send the message directly as a string
            ai_response_text = response.text
            return JsonResponse({'response': ai_response_text})
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            return JsonResponse({'error': 'Failed to get response from Gemini'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
@csrf_exempt
def verify_otp(request):
    """
    Handles POST requests to verify the OTP sent to the user's email.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            otp_received = data.get('otp')

            if not email or not otp_received:
                return JsonResponse({'error': 'Email and OTP are required'}, status=400)

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid email address'}, status=400)

            otp_instance = OTP.objects.filter(user=user, otp=otp_received, expiry_at__gt=timezone.now()).first()

            if otp_instance:
                # Mark the user as verified (consider adding an is_verified field to your UserProfile model)
                otp_instance.delete()  # Delete the used OTP
                return JsonResponse({'message': 'Email verified successfully! You can now log in.'})
            else:
                return JsonResponse({'error': 'Invalid or expired OTP'}, status=400)

        except Exception as e:
            print(f"Error during OTP verification: {e}")
            return JsonResponse({'error': 'OTP verification failed'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def register_user(request):
    """
    Handles POST requests to register a new user.
    Sends an OTP to the user's email for verification.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            if not name or not email or not password:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email address already registered'}, status=400)

            user = User.objects.create_user(username=email, email=email, password=password, first_name=name)

            # Create and save OTP
            otp_instance = OTP.objects.create(user=user)
            otp = otp_instance.otp

            subject = 'Your MarketWise Registration OTP'
            message = f'Thank you for registering with MarketWise! Your OTP is: {otp}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return JsonResponse({'message': 'Registration successful. OTP sent to your email.'})

        except Exception as e:
            print(f"Error during registration: {e}")
            return JsonResponse({'error': 'Registration failed'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def login_otp(request):
    """
    Handles POST requests to generate and send an OTP for login.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            email = data.get('email')

            if not name or not email:
                return JsonResponse({'error': 'Name and email are required'}, status=400)

            try:
                user = User.objects.get(first_name=name, email=email)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid name or email'}, status=404)

            # Create and save OTP
            otp_instance = OTP.objects.create(user=user)
            otp = otp_instance.otp

            subject = 'Your MarketWise Login OTP'
            message = f'Your OTP to log in to MarketWise is: {otp}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return JsonResponse({'message': 'Login OTP sent to your email.'})

        except Exception as e:
            print(f"Error during login OTP generation: {e}")
            return JsonResponse({'error': 'Failed to send login OTP'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def verify_login_otp(request):
    """
    Handles POST requests to verify the login OTP.
    Upon successful verification, you should typically log the user in using Django's authentication system.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            otp_received = data.get('otp')

            if not email or not otp_received:
                return JsonResponse({'error': 'Email and OTP are required'}, status=400)

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid email address'}, status=400)

            otp_instance = OTP.objects.filter(user=user, otp=otp_received, expiry_at__gt=timezone.now()).first()

            if otp_instance:
                otp_instance.delete()
                # **Important:** You should implement Django's authentication system here
                # to log the user in. For example:
                # from django.contrib import auth
                # auth.login(request, user)
                # You might also want to return a session token or redirect the user.
                return JsonResponse({'message': 'Login successful!'})
            else:
                return JsonResponse({'error': 'Invalid or expired OTP'}, status=400)

        except Exception as e:
            print(f"Error during login OTP verification: {e}")
            return JsonResponse({'error': 'Login OTP verification failed'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)