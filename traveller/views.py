from django.shortcuts import render
from django.http import HttpResponse
from .models import FeaturedPost

# Create your views here.
def index(request):

    # fp1 = FeaturedPost()
    # fp1.desc = "A Practical Guide to a Minimalist Lifestyle."
    # fp1.id = 1
    # fp1.img = "featured-1.jpg"
    # fp1.name = "Naruto Uzumaki"
    # fp1.date = "September 06, 2020"
    # fp1.condition = True

    # fp2 = FeaturedPost()
    # fp2.desc = "Enhancing Your Designs with Negative Space."
    # fp2.id = 2
    # fp2.img = "featured-2.jpg"
    # fp2.name = "Pablo Picasso Jr"
    # fp2.date = "September 19, 2020"
    # fp2.condition = False

    # fp3 = FeaturedPost()
    # fp3.desc = "Music Album Cover Designs for Inspiration."
    # fp3.id = 3
    # fp3.img = "featured-3.jpg"
    # fp3.name = "Rolling Stoners"
    # fp3.date = "October 06, 2020"
    # fp3.condition = True
    # fp = [fp1,fp2,fp3]
    """We will try to fetch the data from database now
    """
    fp = FeaturedPost.objects.all()
    
    return render(request,'index.html',{"fp":fp})