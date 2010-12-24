# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:
#!/usr/bin/env python
import sys 
import urllib
import urllib2
try:
  from hashlib import md5
except ImportError:
  import md5


class Zhaoia:
    def __init__(self,url,app_key,secret_code):
        self.url = url
        self.app_key = app_key
        self.secret_code = secret_code

    def get_sign(self,params):
        src = '&'.join(["%s=%s" % (k, v) for k, v in sorted(params.iteritems())]) + "&secretcode="+self.secret_code  
        return md5(src).hexdigest().upper()

    def get_results(self,name,params):
        request_url = self.url+name
        params['sign'] = self.get_sign(params)
        form_data = urllib.urlencode(params)
        return urllib2.urlopen(request_url,form_data).read()

    def get_product_lists(self,keyword,page=1,per_page=16,sort=''):
        params = {
            'appkey':self.app_key,
            'keyword':keyword,
            'page':page,
            'per_page':per_page,
            'sort':sort
            }
        return self.get_results(sys._getframe().f_code.co_name,params)

    def get_product_info(self,id):
        params = {
            'appkey':self.app_key,
            'id':id
            }
        return self.get_results(sys._getframe().f_code.co_name,params)

    def get_related_product_lists(self,id,lsize=8):
        params = {
            'appkey':self.app_key,
            'id':id,
            'lsize':lsize
            }
        return self.get_results(sys._getframe().f_code.co_name,params)
        
    def get_context_product_lists(self,keyword,url,lsize=8):
        params = {
            'appkey':self.app_key,
            'keyword':keyword,
            'url':url,
            'lsize':lsize
            }
        return self.get_results(sys._getframe().f_code.co_name,params)
     
if __name__ == '__main__':

    ZHAOIA_ROOT = 'http://www.zhaoia.com/service/'
    z = Zhaoia(url=ZHAOIA_ROOT, app_key='29286397', secret_code='78cf14f220bdffa07e')
    print z.get_product_lists('dell',page=6)
    print z.get_product_info('85f286c812340d61c727a427bd527566')
    print z.get_related_product_lists('85f286c812340d61c727a427bd527566',lsize=6)
    print z.get_context_product_lists('Canon 佳能 EOS 500D 单反相机 套机 含18-55IS头 - 新蛋中国','http://www.newegg.com.cn/Product/90-c13-193.htm')


