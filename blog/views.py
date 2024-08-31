from django.shortcuts import render

from .models import Stories
from .forms import SubscriptionForm


def starting_page(request):
    stories = Stories.objects.all()
    subscription_form = SubscriptionForm()
    if request.method == "POST":
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            subscription_form.save()
    context = {
        "stories": stories,
        "subscription_form": subscription_form,
    }
    return render(request, "blog/index.html", context)


def all_stories(request):
    all_story = Stories.objects.all()
    context = {
        "stories": all_story
    }
    return render(request, "blog/all_stories.html", context)


def single_stories(request, pk):
    stories = Stories.objects.get(pk=pk)

    context = {
        "story": stories
    }
    return render(request, 'blog/single_stories.html', context)
