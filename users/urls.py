from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterView


urlpatterns = [
                  path('', RegisterView.as_view(template_name="users/register.html"), name='user'),
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
