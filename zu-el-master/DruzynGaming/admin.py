from django.contrib import admin
from .models import Post #add this to import the Post model
admin.site.register(Post) #add this to register the Post model

from .models import Player #add this to import the Post model
admin.site.register(Player)

from .models import Event #add this to import the Post model
admin.site.register(Event)

from .models import Kalendar
admin.site.register(Kalendar)