import datetime
import json
from django.core import serializers
from django.shortcuts import render
from django.db.models.functions import TruncMonth, TruncDay, TruncWeek, TruncHour
from django.db.models import Count, Avg
from decimal import Decimal
from django.utils.dateformat import format
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import os
import requests
from django.template.loader import render_to_string

def home(request):

    return render(request, 'app/log.html')
