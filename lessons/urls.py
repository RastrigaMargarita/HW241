from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from config import settings
from lessons.views.kurs import KursViewSet
from lessons.views.lesson import LessonCreateView, LessonDestroyView, LessonRetriveView, LessonUpdateView, LessonListView

urlpatterns = [
    path('', LessonListView.as_view()),
    path('update/<int:pk>', LessonUpdateView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('<int:pk>', LessonRetriveView.as_view()),
    path('destroy/<int:pk>', LessonDestroyView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = routers.SimpleRouter()
router.register('kurs', KursViewSet)
urlpatterns += router.urls


