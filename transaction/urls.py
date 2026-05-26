from rest_framework.routers import DefaultRouter
from .views import TransactionView

router = DefaultRouter()
router.register("transactions", TransactionView, basename="transactions")

urlpatterns = router.urls