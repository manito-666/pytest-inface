import pytest,os,sys
import allure
from operation.users import login_user
from testcases.conftest import api_data
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.logger import log

@allure.step("步骤1 ==>> 登录用户")
def step_1(token):
    log.info("步骤1 ==>> 登录用户：{}".format(token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class Test_Login():

    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("except_result, except_code, except_msg", api_data["test_login_user"])

    def test_login_user(self, except_result, except_code, except_msg):
        log.info("*************** 开始执行用例 ***************")
        result = login_user()
        step_1("获取token")
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        log.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("error")))
        assert result.response.json().get("error") == except_code
        assert except_msg in result.msg
        log.info("*************** 结束执行用例 ***************")

