#coding=utf-8
import os
from core.rest_client import RestClient
from common.read_data import ReadFileData as R

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = R().load_ini(data_file_path)["host"]["api_root_url"]

class Check(RestClient):   #以下类均继承init方法获取url和发送请求

    def __init__(self, api_root_url, **kwargs):
        super(Check, self).__init__(api_root_url)
    #审核帖子通过
    def check_pass(self,kwargs):
        return self.post("", **kwargs)

    #审核帖子拒绝
    def check_refuse(self,kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_forum_top_set", **kwargs)



check = Check(api_root_url)

