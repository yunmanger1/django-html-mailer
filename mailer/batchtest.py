from django.contrib.auth.models import User
from announcements.models import Announcement

def test_announce():
    from notification import models as notification
    a = Announcement.objects.all()[0]
    data = {'content' :a.content, 'get_absolute_url' : a.get_absolute_url()}
    users = [User.objects.get(username = 'german'), User.objects.get(username = 'admin')]
    notification.send_now(users, "announcement", {'announcement' : data})
