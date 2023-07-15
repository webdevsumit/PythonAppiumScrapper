import os

def get_des_cap():
 des_cap = {
  "appium:app": os.path.dirname(__file__)+"/Instagram.apk",
  "appium:automationName": "UiAutomator2",
  "platformName": "android",
  "appium:udid": "emulator-5554",
  "appium:noReset": "true",
  "appium:appWaitForLaunch": "false",
  "appium:newCommandTimeout": "120",
  "appium:autoAcceptAlerts": "true"
}
return des_cap



import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from des_cap import get_des_cap

class sample(unittest.TestCase):

    #driver initialization
    driver = webdriver.Remote("http://localhost:4723/wd/hub", get_des_cap())
    
def test_hello000(self):
    self.driver.implicitly_wait(20)
    self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"English\")").click()
    self.driver.find_element(By.ID, "com.flipkart.android:id/select_btn").click()
    self.driver.find_element(By.ID, "com.flipkart.android:id/phone_input").send_keys('9876543210')
    self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView").click()
if __name__ == '__main__':
    unittest.main()