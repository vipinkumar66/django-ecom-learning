from .models import Category

def get_categories(request):
    """
    This one is used in the context in the settings
    """
    return {"categories": Category.objects.all()}