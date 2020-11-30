"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from project import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create_project/', views.create_project, name="create_project"),
    path('project/<int:project_id>', views.project_detail, name="project_detail"),
    path('project/report/', views.project_report, name='project_report'),
    path('comment_report/<int:comment_id>', views.comment_report, name='project_report_comment'),
    path('project/<int:project_id>/post_comment', views.post_comment, name="post_comment"),
    path('project/<int:project_id>/fund', views.fund_project, name="project_fund"),

    path('create_project/', views.create_project, name="create_project"),
    path('project/<int:project_id>', views.project_detail, name="project_detail"),
    path('project_rate/<int:project_id>/<int:rating_val>', views.rating_project, name="rating_project")

]


