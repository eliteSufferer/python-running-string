import tempfile
from django.http import HttpResponse
from .video_generator import generate_video


from .models import Request

def generate_video_view(request):
    text = request.GET.get('text', '')

    if text:
        Request.objects.create(text=text)

        duration = 3
        font_size = 48
        background_color = (128, 0, 128)

        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
            generate_video(text, duration, font_size, background_color, temp_file.name)
            with open(temp_file.name, 'rb') as video_file:
                response = HttpResponse(video_file.read(), content_type='video/mp4')
                response['Content-Disposition'] = 'attachment; filename="output.mp4"'
                return response

    return HttpResponse("Укажите нужный текст в параметре 'text' в адресной строке через '?text='")
