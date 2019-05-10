import xadmin
from .models import User

class UserAdmin(object):
    list_display=['username','sex','userid','grade','identity','mobile','nickname']
    search_fields=['username','userid','grade','identity']
    list_filter=['grade','identity','sex']

xadmin.site.unregister(User)
xadmin.site.register(User,UserAdmin)