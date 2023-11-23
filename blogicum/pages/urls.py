"""Calls the function corresponding to the query.

For example, if we have a request for the path <domain>/pages/rules
The urlpatterns variable will start the 'rules' function,
which is located in the 'views' file, assign name=rules to it.
"""

from django.urls import path
from django.views.generic import TemplateView

app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
    path('rules/', TemplateView.as_view(template_name='pages/rules.html'),
         name='rules')
]
