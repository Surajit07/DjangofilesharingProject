from django.shortcuts import render
from .models import Photo

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        new_url=str('https://xeroxfin.herokuapp.com'+new_photo.file.url)
        return render(request, 'index.html', {'new_url': new_url})
    else:
        return render(request, 'index.html')
