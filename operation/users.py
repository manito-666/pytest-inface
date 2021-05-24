#coding=utf-8
import os,sys,json,requests
from core.result_base import ResultBase
from api.user import user
from common.logger import logger

from core .rest_client import RestClient as R


def login_user():
    """
    登录用户
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()

    headers = {'Authorization': 'dd624d6c-25a9-49e4-914a-92063f096192',
               'Content-Type': 'application/json;charset=UTF-8'}
    res = user.login(headers=headers)
    result.success = False
    if res.json()["error"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["error"], res.json()["info"]["uid"])
    result.msg = res.json()["info"]["uid"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.json()))
    return result


def refuse_user(article_id, value, game_id, language):
    """
    禁止评论帖子
    :param article_id: 帖子id
    :param value: 类型
    :param game_id: 游戏id
    :param language: 语言
    """
    headers={'Authorization': 'dd624d6c-25a9-49e4-914a-92063f096192','Content-Type': 'application/json;charset=UTF-8'}

    data={"article_id": article_id, "value": value, "game_id": game_id, "language": language}

    result = ResultBase()
    rep =user.refuse(data=data, headers=headers)
    result.success = False
    print(rep.json())
    if rep.json()['error_code'] ==0:
        result.success = True
    else:
        result.success = " 禁止评论帖子==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(rep.json()["error_code"], rep.json()["error_msg"])
    result.msg = rep.json()["error_msg"]
    result.response = rep
    logger.info("禁止评论帖子 ==>> 返回结果 ==>> {}".format(result.response.json()))
    return result



def allow_user(article_id, value, game_id, language):
    headers={'Authorization': 'dd624d6c-25a9-49e4-914a-92063f096192','Content-Type': 'application/json;charset=UTF-8'}
    data ={
        "article_id": article_id,
        "value": value,
        "game_id": game_id,
        "language": language
    }
    result = ResultBase()
    res=user.allow(data=data, headers=headers)
    result.success = False
    if res.json()['error_code'] == 0:
        result.success = True
    else:
        result.success = " 允许评论帖子==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["error_code"], res.json()["error_msg"])
    result.msg = res.json()["error_msg"]
    result.response = res
    logger.info("允许评论帖子 ==>> 返回结果 ==>> {}".format(result.response.json()))


def home_page(article_id, game_id, language):

    headers = {'Content-Type': 'application/json', 'Authorization': 'dd624d6c-25a9-49e4-914a-92063f096192'}
    data={'article_id': article_id, 'game_id': game_id, 'language': language}
    result = ResultBase()
    rep= user.home_page(data=data, headers=headers)
    print(rep.json())
    result.success = False
    if rep.json()['error_code'] == 0:
        result.success = True
    else:
        result.success = " 帖子设置为首页==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(rep.json()["error_code"], rep.json()["error_msg"])
    result.msg = rep.json()["error_msg"]
    result.response = rep
    logger.info("帖子设置为首页 ==>> 返回结果 ==>> {}".format(result.response.json()))
    return result

# if __name__ == '__main__'
    # login_user()
    # refuse_user(36102083149830, 1, 1001, 1)
    # home_page(36103975796738, 1001, 1)
    allow_user(36102083149830, 0, 1001, 1)
