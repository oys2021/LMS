from django.urls import path
from .import views


urlpatterns=[
path("",views.home,name="index"),
path("testa",views.test,name="index"),
path("courses",views.courses,name="courses"),
path("teachers",views.teacher_view,name="teacher"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact"),
path("login",views.login,name="login"),
path("signup",views.signup,name="signup"),
path("logout",views.logout,name="logout"),
path("recover",views.recover_password,name="recover"),
path("update",views.enroll_update,name="update"),
path("create",views.create,name="create"),
path("profile/<str:username>",views.profile,name="profile"),
path("enroll/<int:id>",views.course_detail,name="enrolled"),
path("classes",views.classes,name="class"),
path("lesson/<int:id>",views.lessons,name="lesson"),
path("aboutcourse",views.about_course,name="acourse"),
path("page/<int:pk>",views.coursepage,name="page")
] 