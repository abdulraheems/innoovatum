
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from dashboard import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign-up/', views.CreateAuthor.as_view(), name='create_user'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', TemplateView.as_view(template_name='search/homepage.html')),
    path('search/', include('haystack.urls')),
    path('search/autocomplete/', views.AutocompleteView, name='autocomplete'),
    # app url configs
    path('posts/',include('blog.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

