from django.shortcuts import render
from musicApp.models.albums import *
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import pdb

def album_list(request):
	all_albums = Albums.list_albums()
	return render(request, 'music/index.html', {'all_albums':all_albums})

def album_detail(request,pk):
	album_detail = Albums.show_album(pk)
	return render(request, 'music/detail.html', {'album':album_detail[0]})

class AlbumCreate(CreateView):
	template_name = "music/album_form.html"
	model = Albums
	fields = ['title', 'number_of_song', 'created_date', 'published_date', 'singer','album_logo']
