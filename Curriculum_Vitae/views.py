from django.shortcuts import render#, get_object_or_404
#from Curriculum_Vitae.models import Resume

#def readlinkresume(request, name):
#    article = get_object_or_404(Resume, path=name)
#    return render(request, 'blog/lire.html', {'article':article})

def rfaure_view(request):

    return render(request, 'Curriculum_Vitae/rfaure.html')