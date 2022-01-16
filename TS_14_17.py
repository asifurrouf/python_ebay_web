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



def deals():
  '''TS_012:checks featured deeals items'''
 
  # cliks on "deals"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.Button[2]').click()
  time.sleep(10)

def deals_item():
  '''TS_014: visit tech item on feature deals item'''
  # cliks on deals
  deals()
  time.sleep(5)
  # clicks on "techs"
  driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Tech. Button. 2 of 5."]/android.widget.TextView').click()
  time.sleep(3)

  # clicks on first item
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout').click()
  time.sleep(5)

def change_theme():
  '''TS_15: changes theme'''
  test_click_menu()
  # scroll to reach settings icon
  scroll = TouchAction(driver)
  scroll.press(x=174, y=1090).wait(2000).move_to(x=174, y=567).release().perform()
  time.sleep(5)

  # clicking on settings icocn
  driver.find_element_by_id('com.ebay.mobile:id/settings').click()
  time.sleep(5)

  # clicks on "theme"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout').click()
  time.sleep(5)

  # clicks on "dark"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RadioButton').click()
  time.sleep(2)

  # # clicks on "light"
  # driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.RadioButton').click()
  # time.sleep(10)

def bids_and_Offers():
  '''TS_016: visits bids and offer section'''
  test_click_menu()
  # clicks on "bids and offer"
  driver.find_element_by_id('com.ebay.mobile:id/myebay_auction_nav_bids_offers').click()
  time.sleep(5)

def filter_search():
  '''TS_017: search items using filter'''
 # clicking on search box
  driver.find_element_by_id('com.ebay.mobile:id/search_box').click()
  time.sleep(3)

  # type any  product name
  driver.find_element_by_id('com.ebay.mobile:id/search_src_text').send_keys('mobile')
  # clicking  on search result  
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.TextView').click()
  time.sleep(10)

  # clicks on blue rectangle popup window
  try:
    driver.find_element_by_id('com.ebay.mobile:id/text_slot_1').click()
    time.sleep(2)
  except:
    pass

  # cliks on "sort"
  driver.find_element_by_id('com.ebay.mobile:id/button_sort').click()
  time.sleep(5)
  # clicks on "lowest price+shipping"
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]').click()
  time.sleep(10)


  


 






# test_click_menu()

# test_categories()
# test_cart()
# test_watching_List()
# search_history()
# search_item()
# filter_item()
# categories()
# check_messages()
# deals()
# check_profile()
# deals_item()
# change_theme()
# bids_and_Offers()
filter_search()

