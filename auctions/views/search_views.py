from django.shortcuts import render
from auctions.models import Comment
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages


def search_results(request):
    if 'q' in request.GET:
        query = request.GET['q']
        print("Query: ", query)  # Debugging
        results = Comment.objects.filter(content__icontains=query)
        print("Results: ", results)  # Debugging

        if not results:
            messages.error(request, 'Nothing matches your search!')
        return render(request, "auctions/search_results.html", {"results": results, "query": query})
    else:
        messages.error(request, 'No search query provided!')
        return render(request, "auctions/search_results.html")
