# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AppspinerItem(Item):
	appLink=Field()
	appName=Field()
	appDeveloper=Field()
	appComment=Field()
	appIcon=Field()
	appIconUrl=Field()
class ImageItem(Item):
	image_urls=Field()
	images=Field()
	image_name=Field()
