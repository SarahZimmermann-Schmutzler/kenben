"""kenben URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workspace.views import BoardsView, TicketsView, SubtasksView, LoginView, RegisterView, UsersView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/boards/', BoardsView.as_view()),
    path('api/boards/<boardId>/', BoardsView.as_view()),
    path('api/tickets/', TicketsView.as_view()),
    path('api/tickets/<ticketId>/', TicketsView.as_view()),
    path('api/subtasks/', SubtasksView.as_view()),
    path('api/subtasks/<subtaskId>/', SubtasksView.as_view()),
    path('api/allUsers/', UsersView.as_view()),
    path('', LoginView.as_view()),
    path('api/login/', LoginView.as_view()),  # API-Login for nginx
    path('api/signup/', RegisterView.as_view()),  # API-Register for nginx
    path('signup/', RegisterView.as_view()),
] + staticfiles_urlpatterns()
