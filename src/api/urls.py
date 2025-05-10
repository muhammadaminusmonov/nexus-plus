from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('category/', include('api.category.urls')),
    path('brand/', include('api.brand.urls')),
    path('region/', include('api.region.urls')),
    path('blog/', include('api.blog.urls')),
]
