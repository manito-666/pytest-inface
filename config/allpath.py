import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

#yaml文件路径
yml_path=os.path.join(configPath,'data')

#配置文件路径
ini_path=os.path.join(configPath,'config','setting.ini')


#测试报告路径
reprort_path=os.path.join(configPath,'testcases','api_test','report')