"""sekretariat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from school_office.views import base, SignUp, Login, logoutView, recruitment1, RecruitmentView, pdf_view, documents, \
    my_data, ResetPasswordView, application_list, application_detail, ApplicationFormView, change_status, RecruitDetailView, \
    serach, SerachStudents, SerachApplication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('signup/', SignUp.as_view(), name="signup"),
    path('', Login.as_view(), name="signin"),
    path('logout/', logoutView, name="logout"),
    path('recruitment1/', recruitment1, name="recruitment1"),
    path('serach/', serach, name="serach"),
    path('serach/student/', SerachStudents.as_view(), name="serach-student"),
    path('serach/application/', SerachApplication.as_view(), name="serach-application"),
    path('recruitment/<int:school_class>', RecruitmentView.as_view(), name="RecruitmentView"),
    path('document/', documents, name='documents'),
    path('my-data/', my_data, name='my_data'),
    path('change-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('pdf/<str:klasa>', pdf_view, name='pdf'),
    path('application/', application_list, name='app-list'),
    path('new-application', ApplicationFormView.as_view(), name='new_app'),
    path('RecruitDetailView/<int:pk>', RecruitDetailView.as_view(), name='recruit'),
    path('application/<int:id>', application_detail, name='application-detail'),
    path('application/<int:id>/<int:status>', change_status, name='change-status'),

]
