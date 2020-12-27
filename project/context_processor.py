from project.models import Category


def extra(request):
    categories = Category.objects.all()
    return {"categories": categories}
