from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from pages.forms import ContactModelForm
from pages.models import ContactModel, NewsModel, PlayerModel, DefendersModel, ManagerModel, MatchModel, GoalModel, \
    AssistModel

app_name = 'pages'


class HomePageView(ListView):
    template_name = 'index.html'
    model = MatchModel
    context_object_name = 'matches_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bombardir_list'] = GoalModel.objects.all()
        context['assisters_list']=AssistModel.objects.all()
        return context


class ContactView(CreateView):
    template_name = 'contacts.html'
    model = ContactModel
    form_class = ContactModelForm
    success_url = '/'


class MatchPageView(ListView):
    template_name = 'matches.html'
    model = MatchModel
    context_object_name = 'matches_list'


class TeamPageView(ListView):
    template_name = 'staff.html'
    model = PlayerModel
    context_object_name = 'staff_list'


class ManagerPageView(ListView):
    template_name = 'staff.html'
    model = ManagerModel
    context_object_name = 'manager_list'


class NewsPageView(ListView):
    template_name = 'news.html'
    model = NewsModel
    context_object_name = 'news_list'


class NewsSinglePageView(DetailView):
    template_name = 'news-single.html'
    model = NewsModel
    context_object_name = 'news'


class StorePageView(TemplateView):
    template_name = 'store.html'
