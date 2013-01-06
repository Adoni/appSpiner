# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

class AppspinerPipeline(object):
    def process_item(self, item, spider):
		f=open(item.appName,w)
		f.write(item.appName+"\n")
		f.write(item.appComment+"\n")
		f.close()
        return item
