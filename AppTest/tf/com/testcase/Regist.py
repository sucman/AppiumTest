# -*- coding:utf-8 -*-
import time
import unittest
import warnings

from AppTest.tf.com.control import config
from AppTest.tf.com.control import getDb
from appium import webdriver


class Login(unittest.TestCase):
    @classmethod
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告

        cal = {
            "platformName": "Android",  # 设备平台
            "deviceName": "b43d2c1",  # 设备名称
            "platformVersion": "6.0.1",  # 设备系统版本
            "appPackage": "com.viausd.pay",  # 包名
            "appActivity": "com.viausd.activity.MainActivity",  # 启动项
            # "app":"C:\\Users\\shuchengxiang\\Desktop\\shoujibaidu_25580288.apk",#apk包路径
            "unicodeKeyboard": True,  # 此两行是为了解决字符输入不正确的问题
            "resetKeyboard": True  # 运行完成后重置软键盘的状态　
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', cal)  # 启动app
        time.sleep(5)

    @classmethod
    def test_calculation(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 忽略警告

        self.driver.find_element_by_id("loginBtn").click()

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView").click()

        iptmail = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")
        iptmail.send_keys(config.REG_MAIL)

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView").click()


        iptsms = self.driver.find_element_by_id("verifyCode")
        smscode = getDb.get_info("MNS","APP_ID","SMSG")
        iptsms.send_keys(smscode)

        iptpwd = self.driver.find_element_by_id("loginPasswd")
        iptpwd.send_keys(config.REG_PWD)

        iptname = self.driver.find_element_by_id("loginName")
        iptname.send_keys(config.REG_NAME)



        self.driver.find_element_by_id("loginBtn").click()

        time.sleep(30)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
