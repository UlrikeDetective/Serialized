from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_distill import distill_path
from . import views
from .models import Story, Chapter


# These functions tell django-distill which pages to export for the static site.
def get_stories():
    for story in Story.objects.all():
        yield {'story_slug': story.slug}


def get_published_chapters():
    for chapter in Chapter.objects.published().select_related('story'):
        yield {'story_slug': chapter.story.slug, 'chapter_number': chapter.number}


# Define the app's specific patterns
story_urlpatterns = [
    distill_path('', views.story_list, name='story_list'),
    distill_path('<slug:story_slug>/', views.story_detail, name='story_detail',
                 distill_func=get_stories),
    distill_path('<slug:story_slug>/<int:chapter_number>/', views.chapter_detail, name='chapter_detail',
                 distill_func=get_published_chapters),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the story patterns under the 'stories' namespace
    path(settings.SITE_PREFIX, include((story_urlpatterns, 'stories'), namespace='stories')),
]
