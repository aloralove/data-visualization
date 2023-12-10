from django.contrib.auth import login  
from django.db import IntegrityError  
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.models import User

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(
                request, "auctions/register.html", {"message": "Passwords must match."}
            )

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)  # Log in the user
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(
                request,
                "auctions/register.html",
                {"message": "Username already taken."}
            )
    else:
        return render(request, "auctions/register.html")
