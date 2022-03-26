from django.shortcuts import render
from youtube import auth, search, get_video_details
from yandex import YandexApi
from django.urls import reverse_lazy
from .models import Video


def index(request):
    videos = []
    context = {}
    if request.method == 'POST':
        yt = auth()
        response = search(query=request.POST['search'])['items']
        videos_data = [vid['id']['videoId'] for vid in response]
        response = get_video_details(ids=','.join(videos_data))
        for result in response['items']:
            video_data = {
                'id': result['id'],
                'title': result["snippet"]["title"],
                'publishedAt': result["snippet"]["publishedAt"],
                'description': result["snippet"]["description"],
                'channelTitle': result["snippet"]["channelTitle"],
                'thumbnail': result["snippet"]["thumbnails"]["high"]["url"],
                'views': result["statistics"]["viewCount"],
                'url': reverse_lazy('video_page', kwargs={'id': result['id']})
            }
            try:
                Video.objects.get(videoId=video_data['id'])  # Проверка, не было ли такое видео уже сохранено в БД
            except:
                new_video = Video(
                    videoId=video_data['id'],
                    title=video_data['title'],
                    description=video_data['description'],
                    publishedAt=video_data['publishedAt'],
                    channelTitle=video_data['channelTitle'],
                    thumbnail=video_data['thumbnail'],
                    views=video_data['views']
                )
                new_video.save()
            videos.append(video_data)
            context['search_query'] = request.POST['search']
    context['videos'] = videos
    return render(request, 'videosearch/index.html', context)


def video_page(request, id):
    video = Video.objects.get(videoId=id)
    if request.method == 'POST':
        if request.POST['language'] == '':
            context = {'video': video}
            return render(request, 'videosearch/video_page.html', context=context)
        dict_video = {'title': video.__dict__['title'], 'description': video.__dict__['description']}
        translator = YandexApi()
        if dict_video['description'] == '':  # Переводчик не принимает пустые строки
            dict_video.pop('description', None)
            translated = translator.translate(request.POST['language'], dict_video, schema=['title'])
        else:
            translated = translator.translate(request.POST['language'], dict_video)
        video.title = translated['title']
        if len(dict_video) != 1:  # проверка на отсутствие описания
            video.description = translated['description']
    context = {'video': video}
    return render(request, 'videosearch/video_page.html', context=context)
