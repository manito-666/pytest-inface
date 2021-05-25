import pytest,allure,os,sys
from operation.users import refuse_user
from testcases.conftest import api_data
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.logger import log

@allure.step("步骤1 ==>> 选择帖子id")
def step_1(article_id,value,game_id,language):
    log.info("步骤1 ==>> 选择帖子 ==>> {}, {}, {}, {}".format(article_id,value,game_id,language))

#用例等级
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("评论模块")
class Test_Allow():
    """帖子评论"""
    @allure.story("用例--帖子允许评论")
    @allure.description("该用例是针对获取帖子评论接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {article_id}, {value}, {game_id}, {language}, {except_result}, {except_code}, {except_msg}】")
    @pytest.mark.single
    #传参数
    @pytest.mark.parametrize("article_id,value,game_id,language, except_result, except_code, except_msg",
                          api_data["test_refuse_user"])

    def test_refuse_user(self, article_id, value, game_id, language, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        result = refuse_user(article_id, value, game_id, language)
        step_1(article_id,value,game_id,language)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("error_msg")))
        assert result.response.json().get("error_code") == except_code
        assert except_msg in result.msg
        log.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_allow.py"])