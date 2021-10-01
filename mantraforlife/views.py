from django.shortcuts import render


def initial(request,):

    return render(request,'404error.html', context=None,)