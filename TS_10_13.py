from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_cap= {
  "appium:deviceName": "0123456789ABCDEF",
  "platformName": "Android",
  "appium:app": "C:\\Users\\FoysalAhmed\\Downloads\\com-ebay-mobile-6025003-59007535-e7eb97e507b7f0e960662171a8b5e725.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)
driver.implicitly_wait(50)
time.sleep(10)



def test_click_menu():
  '''TS_002: Display Menu bar'''
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  time.sleep(5)




def cart_page():
  '''TS__10:checks cart page'''
  # clicks on "cart" icon
  driver.find_element_by_id('com.ebay.mobile:id/action_view_icon').click()
  time.sleep(3)

def check_messages():
  '''TS__011: checks maessage inbox'''
  test_click_menu()
  # clicks on "massages"
  driver.find_element_by_id('com.ebay.mobile:id/nav_messages').click()

def deals():
  '''TS_012:checks featured deeals items'''
 
  # cliks on "deals"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.Button[2]').click()
  time.sleep(10)

def check_profile():
  '''TS_013: visits profile'''
  test_click_menu()
  # cliks user name
  driver.find_element_by_id('com.ebay.mobile:id/textview_sign_in_status').click()
  time.sleep(3)
  # clicks on profile
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]').click()
