from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from financeiro.views import TransationViewSet

router = DefaultRouter()
router.register(r'transacoes',TransationViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('admin/', admin.site.urls),
  path('api/', include('financeiro.urls')), # API do app financeiro

]