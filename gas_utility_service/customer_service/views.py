from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm, SignUpForm  # Ensure SignUpForm is imported
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def services(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'customer_service/services.html', {'requests': requests})

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate the service request with the logged-in user
            service_request.save()
            return redirect('track_requests')  # Redirect to the track requests page after saving
    else:
        form = ServiceRequestForm()  # Create an empty form instance for GET requests
    return render(request, 'customer_service/submit_request.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignUpForm()  # Create an empty form instance for GET requests
    return render(request, 'customer_service/signup.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(user=request.user)  # Filter requests for the logged-in user
    return render(request, 'customer_service/track_requests.html', {'requests': requests})

@login_required
def support_dashboard(request):
    requests = ServiceRequest.objects.all()  # Get all service requests for support representatives
    return render(request, 'customer_service/support_dashboard.html', {'requests': requests})

@login_required
def profile(request):
    return render(request, 'customer_service/profile.html')  # Create a template for the profile

@login_required
def view_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id, user=request.user)  # Ensure only the logged-in user can view their requests
    return render(request, 'customer_service/view_request.html', {'request': service_request})


def home(request):
    
    return render(request, 'customer_service/home.html')
