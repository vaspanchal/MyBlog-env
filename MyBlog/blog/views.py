from django.shortcuts import HttpResponse, render
from .models import BlogPost, Comment
from django.http import Http404


# Create your views here.

def blog_home(request):
    # display recent entries
    recent_blogs_list = BlogPost.objects.order_by("-created_at")[:7]  # making query for latest 7 entries from database ; put '-' in order by argument if wants it in descending order

    context = {"recent_blogs_list": recent_blogs_list} # it gives context to html file that where this key is, use this value
    return render(request, "blog/home.html", context)

def blog_details(request, blog_id): # declared a blog_id variable that stores the int value from url
    # permalink for a particula r blog
    try:
        blog = BlogPost.objects.get(id = blog_id) # ugives given blog object
        title = blog.title
        content = blog.content
        created = blog.created_at.strftime("%d-%m-%y") # string formatting of this field as date(%d)-month(%m)-year
    except:
         raise Http404("Does not exist")
    return HttpResponse(f"TITLE : {title}, CONTENT : {content}, CREATED ON : {created}") # a type of string formatting, see helloworld.py in core python

def yearly_archive(request, year):
    # yearly list of blogs
    yearly_blogs_list = BlogPost.objects.all().filter(created_at__year = year) # The double underscore (__) is used in Django's ORM to create field lookups.
    output = ", ".join([blog.content for blog in yearly_blogs_list])
    return HttpResponse(output)

def monthly_archive(request, month):
    # monthly list of blogs
        monthly_blogs_list = BlogPost.objects.all().filter(created_at__month = month)
        output = ", ".join([blog.content for blog in monthly_blogs_list])
        return HttpResponse(output)


def comment(request, blog_id):
    # handles post comments for a given blog
    comment = Comment.objects.all().filter(post_id = blog_id)[:]

    comments =  ", ".join([f"\"{this.content}\" commented by - {this.author}" for this in comment]) # using fstring with join, demilitor = ,
    return HttpResponse(comments)