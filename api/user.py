#coding=utf-8
import os
from core.rest_client import RestClient
from common.read_data import ReadFileData as R

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = R().load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):   #以下类均继承init方法获取url和发送请求

    def __init__(self, api_root_url,**kwargs):
        super(User, self).__init__(api_root_url)

    def login(self,**kwargs):
        return self.get("/forum_b_online_cn/gateway_open_api/web/user/pms?game_id=1001&language=1",**kwargs)


    #禁止评论帖子
    def refuse(self,**kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_comment_refuse", **kwargs)

    #允许评论帖子
    def allow(self,**kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_comment_allow",**kwargs)

    #帖子设置为首页
    def home_page(self,**kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_recommended_set", **kwargs)



    #帖子设置为首页置顶
    def home_top(self,**kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_top_set", **kwargs)



    #帖子设置为动态置顶
    def move_top(self,**kwargs):
        return self.post("/forum_b_api_cn_v1/content/article/attr_forum_top_set", **kwargs)







user = User(api_root_url)
