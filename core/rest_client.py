
#coding=utf-8
import requests,json,os,sys
import json as complexjson
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.logger import log


class RestClient():

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url


    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, **kwargs):
        return self.request(url, "POST", data, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)



    def request(self, url, method, data=None,**kwargs):
        url = self.api_root_url + url
        headers=dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("cookies")

        self.request_log(url, method, data, params, headers, files, cookies)

        if method == "GET":
            return requests.get(url, headers,**kwargs)

        if method == "POST":
            data = json.dumps(data)
            return requests.post(url, data, headers,**kwargs)

        if method == "PUT":
            if data:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(data)
            return requests.put(url, data, **kwargs)
        if method == "DELETE":
            return requests.delete(url, **kwargs)

    def request_log(self, url, method, data=None,  params=None, headers=None, files=None, cookies=None, **kwargs):
        log.info("接口请求地址 ==>> {}".format(url))
        log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        log.info("接口请求头 headers参数 ==>> {}".format(headers,ensure_ascii=False))
        log.info("接口请求 params 参数 ==>> {}".format(params,ensure_ascii=False))
        log.info("接口请求体 data 参数 ==>> {}".format(data,ensure_ascii=False))
        log.info("接口上传附件 files 参数 ==>> {}".format(files,ensure_ascii=False))
        log.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))


