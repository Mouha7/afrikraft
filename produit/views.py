from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from produit.models import Category

User = get_user_model()

def list_and_manage_categories(request):
    all_categories = Category.objects.all()

    if request.method == 'POST':
        if 'delete_category' in request.POST:
            category_id = request.POST.get('delete_category')
            category = get_object_or_404(Category, pk=category_id)
            category.delete()
            return redirect('list_and_manage_categories')
        
        if 'id_category' in request.POST:
            category_id = request.POST.get('id_category')
            category = get_object_or_404(Category, pk=category_id)
            name_category = request.POST.get('name_category')
            if name_category:
                category.name_category = name_category
                category.save()
            return redirect('list_and_manage_categories')
        
        name_category = request.POST.get('name_category')
        if name_category:
            category = Category(name_category=name_category)
            category.save()
            return redirect('list_and_manage_categories')
    
    return render(request, 'produit/list_category.html', context={'all_categories': all_categories})
