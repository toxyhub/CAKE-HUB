from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import CakePro
from django.urls import reverse

class cakeupdate(Feed):     #inheritance
    title='cakehub'
    link='/drcomments/'
    description='A gorgeous selection of our favorites for a client as a gift.'

    def items(self):
        return CakePro.objects.all()[:4]

    def item_title(self,item):
        return item.name

    def item_description(self,item):
        return truncatewords (item.descript,20)     # for cutting words.

    def item_link(self,item):
        return reverse ('home')                                                                                                                                                                                 