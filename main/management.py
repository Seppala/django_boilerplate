from django.conf import settings
from django.utils.translation import ugettext_noop as _
'''
if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification

    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("new_reply", _("New reply"), _("you have received an reply to your submission"))

    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
'''