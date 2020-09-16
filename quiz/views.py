from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Poll

# Create your views here.

def index(request):
    content = {}

    poll_id = request.GET.get("poll_id")
    if poll_id:
        content["success"] = True
        content["poll_id"] = poll_id
        try:
            poll_id = int(poll_id)
        except:
            content["success"] = False
            return render(request, 'quiz/quiz_result.html', content)

        poll = Poll.objects.filter(pk=poll_id).first()

        if not poll:
            content["success"] = False
            return render(request, 'quiz/quiz_result.html', content)

        content["poll_name"] = poll.poll_name
        content["poll_description"] = poll.poll_description

        poll_options = eval(poll.poll_options)
        poll_result = {}

        for option in poll_options:
            print(option)
            poll_result[option["id"]] = [option["option"],]
            
        poll_options = eval(poll.poll_result)

        for result in poll_options:
            poll_result[result[0]].append(len(result[1]))

        print(poll_result)
        content["poll_result"] = poll_result

        return render(request, 'quiz/quiz_result.html', content)

    return render(request, 'quiz/index.html', content)


def filterInput(text):

    if text == None:
        return None

    try:
        str(text)
        return text.strip()
    except:
        return text


def createPoll(request):
    
    if request.method == "POST":

        context = {"success": True}

        poll_name = request.POST.get("poll_name")
        poll_description = request.POST.get("poll_description")
        poll_options = request.POST.get("poll_options")

        poll_options = json.loads(poll_options)
        poll_result = []
        for option in poll_options:
            poll_result.append([option["id"], []])

        poll = Poll.objects.create(poll_name=poll_name, poll_description=poll_description, poll_options=poll_options, poll_result=poll_result)
        poll.save()

        context["pollId"] = poll.pk

        return JsonResponse(context)


