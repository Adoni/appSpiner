# Scrapy settings for appspiner project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'appspiner'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['appspiner.spiders']
NEWSPIDER_MODULE = 'appspiner.spiders'
DEFAULT_ITEM_CLASS = 'appspiner.items.AppspinerItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
#####Myself
#ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
ITEM_PIPELINES=['appspiner.ImageMiddleware.ImagesPipeline']
IMAGES_STORE = '/home/yiyufafa/ImageStore'
