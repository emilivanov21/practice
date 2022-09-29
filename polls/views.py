from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import deepform 

from .models import Choice, Question, Deepthought



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# class DeepthoughtView_input(generic.DeepthoughtView_input):
#     model = Deepthought
#     template_name = 'polls/deepthought.html'
#     fields = ["thought_title", "thought_view"]

   
# class DeepthoughtView_all(generic.DeepthoughtView_all):
#     template_name = 'polls/list.html'
#     context_object_name = 'latest_thought_list'

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Deepthought.objects.all()
# def deep_view(request):
#     form = deepform(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form':form
#     }
#     return render(request, "polls/base.html", context)

def deep_view(request):
    if request.method == 'POST':
        form = deepform(request.POST)
        if form.is_valid():
            form.save()
            # list_view = Deepthought.objects.all()
            # print (list_view)

            
    else:
        form = deepform()
    return render(request, "polls/base.html", {'form': form})

def list_view(request):
    list_view = Deepthought.objects.all
    context = {'list_view' : list_view}
    return render(request, 'polls/list.html', context)