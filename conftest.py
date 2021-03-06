import os
import pytest
from selenium.webdriver import DesiredCapabilities
from pack.pack_log import logger
from time import sleep
from selenium import webdriver
from page.login_page import loginPage
from data.configyaml import getdata, getThirddata
from config import config

log = logger()
# pytest配置对象
# 注意此对象只能在顶层目录的conftest.py文件中完成
# action：store 存储参数
# default 参数默认值，此处为“device”
# help 参数帮助信息，此处为无



def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="device", help="None")

# 解析命令行
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture
def common_browser(cmdopt):
    os.system('chcp 65001')
    print(cmdopt)
    if cmdopt == "localhost:5555":
        # 注意这里5001是selenium grid设置的端口号
        browser = webdriver.Remote(
            command_executor='http://localhost:5555/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    elif cmdopt == "192.168.6.218:6666":
        browser = webdriver.Remote(
            command_executor='http://192.168.6.174:6666/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    else:
        raise Exception
    browser.implicitly_wait(10)
    browser.get("http://ft1.sh.zhaoonline.com")
    yield browser
    browser.quit()
    sleep(2)

@pytest.fixture
def login_browser(cmdopt):
    # os.system('chcp 65001')
    # print(cmdopt)
    if cmdopt == "localhost:5555":
        # 注意这里5001是selenium grid设置的端口号
        browser = webdriver.Remote(
            command_executor='http://localhost:5555/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    elif cmdopt == "192.168.6.218:6666":
        browser = webdriver.Remote(
            command_executor='http://192.168.6.174:6666/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
    else:
        raise Exception
    browser.implicitly_wait(10)
    browser.get("http://ft1.home.zhaoonline.com/login.shtml?back=")
    browser.find_element_by_id("loginId").send_keys(getdata("setup_account","username"))
    browser.find_element_by_id("password").send_keys(getdata("setup_account","password"))
    browser.find_element_by_id("loginBtn").click()
    yield browser
    browser.quit()
    sleep(2)

@pytest.fixture
def multi_browser(cmdopt):
    # os.system('chcp 65001')
    # print(cmdopt)
    if cmdopt == "localhost:5555":
        # 注意这里5001是selenium grid设置的端口号
        browser = webdriver.Remote(
            command_executor='http://localhost:5555/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        temp = 1
    elif cmdopt == "192.168.6.89:6666":
        browser = webdriver.Remote(
            command_executor='http://192.168.6.89:6666/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        temp = 2
    else:
        raise Exception
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("http://ft1.home.zhaoonline.com/login.shtml?back=")
    browser.find_element_by_id("loginId").send_keys(getThirddata("multi_account", temp, "username"))
    browser.find_element_by_id("password").send_keys(getThirddata("multi_account", temp, "password"))
    browser.find_element_by_id("loginBtn").click()
    yield browser
    browser.quit()
    sleep(2)

