from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'responsable', ResponsableViewSet)
router.register(r'responsable/all', ResponsableListView.as_view(), name='responsables')




router.register(r'student', StudentViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'students/responsables', StudentResponsableViewSet)
router.register(r'aviable_services' , ServiceSignatureViewSet)
router.register(r'services', ServiceClassViewSet)



urlpatterns = router.urls