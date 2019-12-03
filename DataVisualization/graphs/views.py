# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# # Create your views here.
from django.views.generic import TemplateView
from . import plots

class SimpleCandlestickWithPandas(TemplateView):
    template_name = 'plot.html'
    def get_context_data(self, **kwargs):
        context = super(SimpleCandlestickWithPandas, self).get_context_data(**kwargs)
        context['simplecandlestick'] = plots.get_simple_candlestick()
        context['3dplot'] = plots.get_topographical_3D_surface_plot()
        context['piechart'] = plots.pie_chart()
        return context