import logging

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic import TemplateView

from . import plots

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "index.html"


class Plot1DView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d()
        return context


class Plot2DView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot2DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot2d()
        return context


class Plot3DView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot3DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot3d()
        return context


class Plot1DMultipleView(TemplateView):
    template_name = "plot_multiple.html"

    def get_context_data(self, **kwargs):
        n = int(kwargs['n'])
        # Call the base implementation first to get a context
        context = super(Plot1DMultipleView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d_multiple(n)
        return context


def plot1d_multiple_ajax(request, n):
    """
    Only handles AJAX queries
    """
    logger.debug("Plotting {} plots.".format(n))
    return HttpResponse(plots.plot1d_multiple(int(n)))


class PlotIqView(TemplateView):
    template_name = "plot_fit.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlotIqView, self).get_context_data(**kwargs)
        context['plot'] = plots.plotIq()
        return context


class PlotLiveView(TemplateView):
    template_name = "plot_live.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlotLiveView, self).get_context_data(**kwargs)
        context['plot'] = plots.plotLive()
        return context


def plot_live_update(request):
    '''
    Handle ajax call to update the live plot
    '''
    if request.is_ajax():
        logger.debug("Live plot updated...")
        data = plots.live_plot_get_data_serialized()
        # In order to allow non-dict objects to be serialized set the safe
        # parameter to False
        return JsonResponse([data], safe=False)
    else:
        return HttpResponseBadRequest()


class Plot3DScatterView(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot3DScatterView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot3D_scatter
        return context


class PlotPie(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(PlotPie, self).get_context_data(**kwargs)
        context = {
            'plot': plots.piechart,
        }

        return context

class PlotDonut(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(PlotDonut, self).get_context_data(**kwargs)
        context = {
            'plot': plots.donutchart,
        }

        return context

class PlotVolume(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(PlotVolume, self).get_context_data(**kwargs)
        context = {
            'plot': plots.volumedonutchart,
        }

        return context

class PlotMarketChange(TemplateView):
    template_name = "plot.html"

    def get_context_data(self, **kwargs):
        context = super(PlotMarketChange, self).get_context_data(**kwargs)
        context = {
            'plot': plots.MarketChangedonutchart,
        }

        return context