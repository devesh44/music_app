from django.shortcuts import render


def album_list(request):
    return render(request, 'album/album_list.html', {})