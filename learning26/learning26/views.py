from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def Movies(request):
    return render(request,"Movies.html")

def shows(request):
    return render(request,"shows.html")

def news(request):
    return render(request,"news.html")

def recape(request):
    return render(request,"recape.html")

def recipe(request):
    ingredient = ["Salt","Sugar","Spices","Vegetables"]
    data = { "name": "Pasta", "time": 20, "ingredient": ingredient}
    return render(request,"recipe.html",data)

def team(request):
    
    data = { "teamName": "India", "cap": "Rohit Sharma", "playerList": ["Virat", "Gill", "Jadeja", "Bumrah"], "trophy": 3}
    return render(request,"team.html",data)
