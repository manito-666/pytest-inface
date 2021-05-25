import os,sys
import pytest
Path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(Path)[0]
sys.path.append(rootPath)
from common.logger import log
case_path = os.path.join(os.getcwd())
PATH = os.path.split(os.path.realpath(__file__))[0]
failureException = AssertionError
if __name__ == '__main__':
    log.info("%s --alluredir=./report" % case_path)
    pytest.main(["-s", "-q", "--alluredir=./report"])
    os.popen("allure generate report/ -o result/ --clean")
