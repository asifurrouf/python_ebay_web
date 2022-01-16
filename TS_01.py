from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
class User:

    desired_cap= {
    "appium:deviceName": "0123456789ABCDEF",
    "platformName": "Android",
    "appium:app": "C:\\Users\\FoysalAhmed\\Downloads\\com-ebay-mobile-6025003-59007535-e7eb97e507b7f0e960662171a8b5e725.apk"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
    driver.implicitly_wait(50)
    time.sleep(10)
    # driver.find_element_by_id('com.ebay.mobile:id/button_sign_in').click()
    # driver.find_element_by_id("com.ebay.mobile:id/button_register").click()
    # driver.implicitly_wait(30)
    # driver.find_element_by_id('com.ebay.mobile:id/button_google').click()

    # #click gmail account 
    # driver.implicitly_wait(30)
    # driver.find_element_by_xpath('	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout').click()
