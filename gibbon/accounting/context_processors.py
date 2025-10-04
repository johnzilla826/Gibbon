from .models import Company

def site_settings(request):
    settings = Company.objects.first()  # get the first record
    return {
        'site_settings': settings
    }