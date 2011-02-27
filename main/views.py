import os
from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from annoying.decorators import render_to, ajax_request
from annoying.functions import get_object_or_None, get_config

from main.forms import *
from main.models import *

@render_to('main/index.html')
def index(request):
    ''' 
    Index page
    '''
    
    return {
    }
