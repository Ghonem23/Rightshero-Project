from django.shortcuts import render
from django.http import JsonResponse, Http404
from .models import Category

# View to display the main category selection page
def category_selection_view(request):
    categories = Category.objects.filter(parent__isnull=True)  # Fetch only top-level categories
    return render(request, 'categories/category_selection.html', {'categories': categories})

# View to load subcategories based on selected category via Ajax
def load_subcategories(request):
    try:
        category_id = int(request.GET.get('category_id'))  # Ensure the category ID is a valid integer
    except (ValueError, TypeError):
        raise Http404("Invalid category ID")
    
    subcategories = Category.objects.filter(parent_id=category_id)
    if not subcategories.exists():
        return JsonResponse({'error': 'No subcategories found'}, status=404)

    return render(request, 'categories/subcategories.html', {'subcategories': subcategories})