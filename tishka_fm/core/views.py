from django.shortcuts import render


def main(request):
    template = 'core/index.html'
    return render(request, template)
