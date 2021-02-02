from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
	path('', include('djoser.urls')),
	path('', include('djoser.urls.authtoken')),
]