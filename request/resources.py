from import_export import resources
from .models import PricingRequest


class PricingRequestResource(resources.ModelResource):
    class Meta:
        model = PricingRequest
