from django.urls import path
from . import views
from employer.views import employer
from products.views import productsHome
from Accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("employee/", views.employee, name="employee"),
    path("employer/", employer, name="employer"),
    path("employee/create/", views.createEmployee, name="create-employee"),
    path("employee/delete/<str:pk>", views.deleteEmployee, name="delete-employee"),
    path("employee/update/<str:pk>", views.updateEmployee, name="update-employee"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
