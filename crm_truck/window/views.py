from logging import getLogger

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponseRedirect

from utils import reverse_query

from fleet.models import Vehicle, FilterLabel

from .forms import IndexForm

logger = getLogger(__name__)


class Index(FormView):
    form_class = IndexForm
    template_name = "window/index.html"
    success_url = reverse_lazy("home-index")

    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, *kwargs)

    def form_valid(self, form):
        request = self.request
        if "filter-vehicle" in request.POST:
            cd = form.cleaned_data
            return HttpResponseRedirect(reverse_query("vehicle-list", query_kwargs=cd))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vehicle_list"] = [Vehicle.objects.first() for _ in range(8)]
        context["range_i"] = list(range(3))
        return context
