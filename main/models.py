from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from annoying.functions import get_object_or_None


class UserProfile(models.Model):
    # Map to user
    user = models.ForeignKey(User, unique=True)
    
    # Fields
    # TODO: Add user's fields
    
    def __unicode__(self):
        return '%s' % self.user
    
    def get_absolute_url(self):
        #return reverse('main_blog', args=[self.user.username])
        pass
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])