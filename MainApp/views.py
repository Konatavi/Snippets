from django.http import Http404
from django.shortcuts import render, redirect

from MainApp.models import Snippet


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }


def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = get_base_context(request, 'Добавление нового сниппета')
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    # получение данных из базы
    snippet_list = Snippet.objects.all()
    count = Snippet.objects.all().count()
    context = get_base_context(request, 'Просмотр сниппетов')
    context["snippet_list"] = snippet_list
    context["count"] = count

    return render(request, 'pages/view_snippets.html', context)


def snippet_by_id_page(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
    except Snippet.DoesNotExist:
        raise Http404
    context = get_base_context(request, 'Просмотр сниппета')
    context["snippet"] = snippet
    return render(request, 'pages/snippet.html', context)

