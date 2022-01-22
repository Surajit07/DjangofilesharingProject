from django.shortcuts import render
from .models import Photo
from twilio.rest import Client

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_photo = Photo(
            file = request.FILES['img']
        )
        new_photo.save()
        new_url=str('https://xeroxfin.herokuapp.com'+new_photo.file.url)
        sid='ACad20495dd3bf324541f3c9a60657ddf9'
        authToken='79dd15fb319bc03f63c7d81f4f8a662c'

        client=Client(sid,authToken)

        from_whatsapp_number='whatsapp:+14155238886'
        to_whatsapp_number='whatsapp:+919863103113'

        message=client.messages.create(body=new_url,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
        return render(request, 'index.html', {'new_url': new_url})
    else:
        return render(request, 'index.html')
