from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("event", EventViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("group", GroupViewSet)
router.register("course", CourseViewSet)
router.register("module", ModuleViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("recording", RecordingViewSet)
router.register("lesson", LessonViewSet)
router.register("category", CategoryViewSet)
router.register("enrollment", EnrollmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
