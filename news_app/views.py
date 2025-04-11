import random
from django.shortcuts import render, get_object_or_404
from .models import VisualContent
from .models import Article, Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .forms import ArticleForm
import csv
from django.http import JsonResponse

import os
import csv
from django.conf import settings
from django.http import JsonResponse

def articles_api(request):
    file_path = os.path.join(settings.BASE_DIR, 'data', 'articles.csv')
    articles = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            articles.append(row)

    return JsonResponse({'articles': articles})



def submit_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home") 
    else:
        form = ArticleForm()

    return render(request, "submit_article.html", {"form": form})


@csrf_exempt
def like_article(request, article_id):
    article = get_object_or_404(Article, article_id=article_id)
    article.likes += 1
    article.save()
    return JsonResponse({'likes': article.likes})

@csrf_exempt
def add_comment(request, article_id):
    if request.method == "POST":
        article = get_object_or_404(Article, article_id=article_id)
        name = request.POST.get("name", "Anonymous")  # Default to Anonymous if no name given
        comment_text = request.POST.get("text", "")

        if comment_text:
            comment = Comment.objects.create(article=article, name=name, text=comment_text)
            return JsonResponse({
                "message": "Comment added!",
                "name": comment.name,
                "text": comment.text,
                "created_at": comment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # Format date
            })

    return JsonResponse({"error": "Invalid request"}, status=400)

def base(request):
    articles = Article.objects.all()  
    featured_article = random.choice(articles) if articles else None  

    return render(request, "home.html", {"featured_article": featured_article})


def search(request):
    query = request.GET.get("query", "").strip()  
    articles = Article.objects.filter(headline__icontains=query) if query else []  

    return render(request, "search_results.html", {"query": query, "articles": articles})


#def article_detail(request, id):
#    article = get_object_or_404(Article, article_id=id)  # Ensure `article_id` is correct
#    return render(request, "article.html", {"article": article})  # Use "article.html"

def article_detail(request, id):
    article = get_object_or_404(Article, article_id=id)
    related_articles = Article.objects.exclude(article_id=id)[:3]  

    return render(request, "article.html", {
        "article": article,
        "articles": related_articles,  
    })



def home(request):
    articles = Article.objects.all()
    
    global_visuals = VisualContent.objects.filter(article__isnull=True)

    article_visuals = VisualContent.objects.filter(article__isnull=False)
    

    return render(request, "home.html", {
        "articles": articles,
        "global_visuals": global_visuals,
        "article_visuals": article_visuals,
    })


