import pytest,allure,os
from operation.users import home_page
from testcases.conftest import api_data
from common.logger import logger

@allure.step("步骤1 ==>> 选择帖子id")
def step_1(article_id, game_id, language):
    logger.info("步骤1 ==>> 传入参数 ==>> {}, {},  {}".format(article_id, game_id, language))

#用例等级
@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("设置首页模块")
class Test_Home():
    """帖子设置为首页"""
    @allure.story("用例--帖子设置为首页")
    @allure.description("该用例是针对设置帖子为首页接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {article_id}, {game_id}, {language}, {except_result}, {except_code}, {except_msg}】")
    @pytest.mark.single
    #传参数
    @pytest.mark.parametrize("article_id, game_id, language, except_result, except_code, except_msg",
                          api_data["test_home_page"])

    def test_home_page(self, article_id, game_id, language, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = home_page(article_id, game_id, language)
        step_1(article_id, game_id, language)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("error_msg")))
        assert result.response.json().get("error_code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_home.py"])