from .models import Company

def site_settings(request):
    settings = Company.objects.first()
    return {
        'site_settings': settings
    }