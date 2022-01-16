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



def search_history():
  '''TS_006: Clears search history'''
  # clicking on menu
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  time.sleep(5)
  # scroll to reach settings icon
  scroll = TouchAction(driver)
  scroll.press(x=174, y=1090).wait(2000).move_to(x=174, y=567).release().perform()
  time.sleep(5)

  # clicking on settings icocn
  driver.find_element_by_id('com.ebay.mobile:id/settings').click()
  time.sleep(5)

  # clicking on clear search history
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout').click()
  time.sleep(5)

  # clicking on "OK" button
  driver.find_element_by_id('android:id/button1').click()
  time.sleep(5)

def search_item():
  '''TS_07:Searching any item from search box'''
  # clicking on search box
  driver.find_element_by_id('com.ebay.mobile:id/search_box').click()
  time.sleep(3)

  # type any  product name
  driver.find_element_by_id('com.ebay.mobile:id/search_src_text').send_keys('mobile')
  time.sleep(3)
  # clicking  on search result  
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
  time.sleep(10)

  # clicks on blue rectangle popup window
  try:
    driver.find_element_by_id('com.ebay.mobile:id/text_slot_1').click()
    time.sleep(2)
  except:
    pass

  # clicking on "save this search" button
  driver.find_element_by_id('com.ebay.mobile:id/button_follow').click()
  time.sleep(5)



  ###########---------------------####################

def filter_item():
  '''TS_08: Search item and filter item'''
  # clicking on search box
  driver.find_element_by_id('com.ebay.mobile:id/search_box').click()
  time.sleep(3)
  # type any  product name
  driver.find_element_by_id('com.ebay.mobile:id/search_src_text').send_keys('mobile')
  time.sleep(3)
  # clicking  on search result  
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
  time.sleep(10)
  # clicks on blue rectangle popup window
  try:
    driver.find_element_by_id('com.ebay.mobile:id/text_slot_1').click()
    time.sleep(2)
  except:
    pass
  # clicks on "filter"
  driver.find_element_by_id('com.ebay.mobile:id/button_filter').click()
  # clicks on "sort"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.ViewGroup').click()
  time.sleep(5)
  # selecting "newly listed"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]').click()
  time.sleep(10)
  # clicking 'back barrow'
  driver.find_element_by_id('com.ebay.mobile:id/search_button_back_all_filters').click()
  time.sleep(5)
  # clicks on "condition " button
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]').click()
  time.sleep(10)
  # cliks on "show result" button
  driver.find_element_by_id('com.ebay.mobile:id/call_to_action_button').click()
  time.sleep(10)


def categories():
  '''TS_09:search "stamps"'''
    # click on nav menu
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  driver.implicitly_wait(30)
  # click on categories
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]').click()
  time.sleep(10)
  # scrolling to reach "stamps"
  scroll= TouchAction(driver)
  for i in range(5):
    scroll.press(x=314, y=1255).wait(2000).move_to(x=314, y=290).release().perform()
    time.sleep(3)
  
  # clicking on stamps
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.TextView').click()
  time.sleep(10)

  # clicking on "Asia"
  driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Collapsed Asia"]/android.widget.TextView').click()
  time.sleep(5)
  # clicking on bangladesh
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.TextView').clik()
  time.sleep(3)
