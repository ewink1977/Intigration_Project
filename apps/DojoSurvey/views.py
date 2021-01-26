from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print('INDEX PAGE REQUESTED')
    return render(request, 'dojo/index.html')

def redir(request):
    if request.method == "POST":
        print("POST REQUEST MADE FROM SURVEY")
        request.session["your_name"] = request.POST["your_name"]
        request.session["location"] = request.POST["location"]
        request.session["language"] = request.POST["language"]
        request.session["end"] = request.POST["end"]
        request.session["frameworks"] = request.POST.getlist("frameworks")
        request.session["comments"] = request.POST["comments"]
        return redirect('/result')
    if request.method == "GET":
        print("GET REQUEST MADE TO RESULT. INVALID AND REDIRECTING.")
        redirect("/")

def result(request):
    print("REDIRECTION TO RESULT PAGE")
    return render(request, 'dojo/results.html')
    

