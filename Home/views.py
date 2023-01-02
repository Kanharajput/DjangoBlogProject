from django.shortcuts import render
from .Helper.BlogDetailsData import all_blogs     # getting the blogs data
from .Helper.getDate import getDate             # getting the function which is used to sort the post

# Create your views here.

def home (request):
    # sort the list according to the date of dictionaries in accending order
    # https://github.com/Kanharajput/SortListHavingDictionary/blob/main/sortListHavingDict.txt
    # check the example of above link to understand happing behind the scene
    sorted_blogs = sorted(all_blogs,key=getDate)      
    latest_blogs = sorted_blogs[-3:]               # it will return the recent 3 blogs
    return render(request,'Home/home.html',{'latest_blogs':latest_blogs})  