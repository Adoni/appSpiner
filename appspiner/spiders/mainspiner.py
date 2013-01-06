# -*- coding: utf-8 -*- 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from appspiner.items import AppspinerItem, ImageItem
from scrapy.http import Request
from scrapy.utils.response import get_base_url 
from scrapy.utils.url import urljoin_rfc 
import sys, os, time
reload(sys) 
sys.setdefaultencoding('utf-8')

class appSpiner(BaseSpider):
	name="itunes"
	allowed_domains=["itunes.apple.com"]
	start_urls=["https://itunes.apple.com/cn/genre/ios/id36?mt=8",
	]
#### Main parse function, to enter into every category ####
	def parse(self, response):
		items=[]
		hxs=HtmlXPathSelector(response)
		links=hxs.select("//div[@class='grid3-column']//li//@href").extract()
		for link in links:
			yield Request(link, callback=self.parseCategory)

#### Parse function to parse every category ####
	def parseCategory(self, response):
		hxs=HtmlXPathSelector(response)
		appurls=hxs.select("//div[@id='selectedcontent']//li//@href").extract()
		i=0
		for appurl in appurls:
			i=i+1
			if(i>5):
				break
			yield(Request(appurl, callback=self.parseApp))

#### Parse function to parse a certain app ####
	def parseApp(self, response):
		hxs=HtmlXPathSelector(response)
		#title=hxs.select("//div[@id='title']//div[1]//h1/text()").extract()
		#appname=title[0]
		#developer=title[1]
		#item=AppspinerItem()
		#item['appName']=appname
		#item['appDeveloper']=developer
		#comment=hxs.select("//div[@class='center-stack']/div[1]/p/text()")
		#item['appComment']=comment
		#item['appIconUrl']=iconurl
		appname=hxs.select("//div[@id='title']//div[1]//h1/text()").extract()[0]
		developer=hxs.select("//div[@id='title']//div[1]//h2/text()").extract()[0]
		#f=open("Information.txt",'w')
		#f.write(appname+'\n')
		#f.write(developer+'\n')
		#f.write('\n')
		#f.close()
		#print appname
		#print developer
		iconurls=hxs.select("//div[@id='left-stack']//div[1]/a/div/img/@src").extract()
		items=[]
		base_url=get_base_url(response)
		item=ImageItem()
		item['image_urls']=[urljoin_rfc(base_url, iconurls[0])]
		item['image_name']=appname
		items.append(item)
		return items
