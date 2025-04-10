from django.urls import path
from .views import leader_standard_work_view

urlpatterns = [
    # This URL pattern routes the form page.
    path('', leader_standard_work_view, name='leader_standard_work_form'),
]