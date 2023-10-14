from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .models import Quote, Author, Tag
from .forms import QuoteForm, AuthorForm, TagForm

from django.contrib.auth.decorators import login_required


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={"quotes": quotes_on_page})


def show_author(request, author_id):
    author = Author.objects.get(pk=author_id)

    return render(request, 'quotes/show_author.html', context={"author": author})


def viewing_tag(request, tag_name, page=1):
    print(tag_name)
    tag_obj = Tag.objects.get(name=tag_name)
    print(tag_obj, type(tag_obj))
    quotes = Quote.objects.filter(tags=tag_obj)
    return render(request, 'quotes/viewing_tag.html', context={"quotes": quotes})


@login_required
def add_quote(request):
    print(" start add quote   ")
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():

            print("  form valid ")

            form.save()
            print("  save new quote ")
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_quote.html', {'form': form})

    return render(request, 'quotes/add_quote.html', {'form': QuoteForm()})



@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_tag.html', {'form': form})

    return render(request, 'quotes/add_tag.html', {'form': TagForm()})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/add_author.html', {'form': form})

    return render(request, 'quotes/add_author.html', {'form': AuthorForm()})
