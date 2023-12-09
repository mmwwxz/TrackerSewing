# production_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def forbidden_view(request):
    return HttpResponseForbidden("Пошёл нахуй 🖕🏿")


urlpatterns = [
    path('', lambda request: redirect('login'), name='index'),  # Redirect to 'home'
    path('admin/', forbidden_view),
    path('moms_hacker_admin/', admin.site.urls),
    path('home/', lambda request: redirect('home'), name='home'),
    path('records/', include('production_records.urls')),  # Include production_records.urls
    path('expenses/', include('production_records.expenses_urls')),  # Include expenses_urls
]
