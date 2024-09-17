from .models import category,asettings,footer
def global_data_send(request):
    data={
        'category':category.objects.all(),
        'asettings':asettings.objects.first(),
        'footer':footer.objects.first(),
       
    }
    return data