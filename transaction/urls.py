from rest_framework.routers import DefaultRouter
from .views import TransactionView, AggregateView

router = DefaultRouter()
router.register("transactions", TransactionView, basename="transactions")
router.register("budget", AggregateView, basename="aggregate")

urlpatterns = router.urls