import os
import pytest
from common.logger import logger
case_path = os.path.join(os.getcwd())
PATH = os.path.split(os.path.realpath(__file__))[0]
failureException = AssertionError
if __name__ == '__main__':
    logger.info("%s --alluredir=./report" % case_path)
    pytest.main(["-s", "-q", "--alluredir=./report"])
    os.popen("allure generate report/ -o result/ --clean")
