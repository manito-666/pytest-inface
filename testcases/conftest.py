import pytest
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from common.logger import log
from common.read_data import data
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data =data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data

api_data = get_data("api_test_data.yml")
#
# @allure.step("前置步骤 ==>> 清理数据")
# def step_first():
#     log.info("******************************")
#     log.info("前置步骤开始 ==>> 清理数据")
#
#
# @allure.step("后置步骤 ==>> 清理数据")
# def step_last():
#     log.info("后置步骤开始 ==>> 清理数据")

