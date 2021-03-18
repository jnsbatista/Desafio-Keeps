"""
kontent URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import RedirectView
from config.docs import schema_view

from course.views.course_viewset import CourseViewSet
from course.views.course_category_viewset import CourseCategoryViewSet
from student.views.student_viewset import StudentViewSet
from enrollment.views.enrollment_viewset import EnrollmentViewSet

_read_only = {'get': 'list'}

_read_only_detail = {'get': 'retrieve'}

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'patch': 'partial_update',
           'delete': 'destroy'}


urlpatterns = [
    re_path('^$', RedirectView.as_view(url='docs/', permanent=True), name='schema-swagger-ui'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('courses', CourseViewSet.as_view(_list), name='course-list'),
    path('courses/<uuid:pk>', CourseViewSet.as_view(_detail), name='course-detail'),

    path('course-categories', CourseCategoryViewSet.as_view(_list), name='course-categories-list'),
    path('course-categories/<uuid:pk>', CourseCategoryViewSet.as_view(_detail), name='course-categories-detail'),

    path('students', StudentViewSet.as_view(_list), name='students-list'),
    path('students/<uuid:pk>', StudentViewSet.as_view(_detail), name='students-detail'),

    path('enrollments', EnrollmentViewSet.as_view(_list), name='students-list'),
    path('enrollments/<uuid:pk>', EnrollmentViewSet.as_view(_detail), name='students-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
