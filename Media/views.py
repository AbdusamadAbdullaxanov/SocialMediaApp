from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts, Users
from .forms import UsersForm, PostsForm, YouTubeForm
from django.http import HttpResponseRedirect
from youtube_search import YoutubeSearch


# Create your views here.
def index(request):
    return render(request, "check.html", {})


def return_to_home(request):
    return render(request, "homepage.html", {})


def user_information(request, pk):
    username = Posts.objects.get(id=pk)
    user = Users.objects.filter(username=username).values()
    return render(request, "user_info.html", {"user": user})


def search_videos(request):
    query = YouTubeForm(request.POST)
    video = query.cleaned_data["search_field"] if query.is_valid() else print(False)
    print(video)
    print("\n\n\n")
    video = "Python" if video is None else print(False)
    response = YoutubeSearch(str(video), max_results=1).to_dict()
    print(response)
    return render(request, "YouTube_videos.html",
                  {"query": query, "video": "https://www.youtube.com/embed/" + response[0].get("id"),
                   "title": response[0].get("title"),
                   "views": response[0].get("views")})


class PostsView(ListView):
    template_name = "posts.html"
    model = Posts


def create_user(request):
    form = UsersForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username, fullname, email, password = form.cleaned_data["username"], form.cleaned_data["fullname"], \
                                                  form.cleaned_data["email"], form.cleaned_data["password"]
            new_user = Users(username=username, fullname=fullname, email=email, password=password)
            new_user.save()
            return HttpResponseRedirect("https://socialmedia0007.herokuapp.com")
    return render(request, "create_user.html", {"form": form})


def create_post(request):
    create_posts = PostsForm(request.POST)

    if request.method == "POST" and create_posts.is_valid():
        username, text = create_posts.cleaned_data["user"], create_posts.cleaned_data["text"]
        user_name = Users.objects.filter(username=username).values()
        if user_name:
            post_model = Posts(user=username, text=text)
            post_model.save()
        else:
            # ________________________________________________________________________________________________
            print(create_posts.Meta.widgets.get("user").attrs.get("placeholder"))
            # ________________________________________________________________________________________________
            return render(request, "error_auth.html", {})
        return HttpResponseRedirect("https://socialmedia0007.herokuapp.com/posts")
    return render(request, "create_posts.html", {"create_posts": create_posts})
