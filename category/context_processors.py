'''
context_processor is a python fucntion which takes request as an argument and returns a dictionary with data.
We need to add this i.e(category.context_processors.menu_link) in our seetings.py under TEMPLATES--->context_processors
so that we can use this function menu_link in any templates we want

'''
from .models import Category

# we are fetching all the categories from the database(models)
def menu_link(request):
    links = Category.objects.all()
    return dict(links=links)
