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

def test_categories():
  '''TS_003: Save item from Categories'''
  # click on nav menu
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  driver.implicitly_wait(30)
  # click on categories
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]').click()
  driver.implicitly_wait(30)

  # clicking on baby category
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView').click()
  driver.implicitly_wait(20)

  # cliking  carsafety seats
  driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Collapsed Car Safety Seats"]/android.widget.TextView').click()
  driver.implicitly_wait(10)

  # clicking infant head support
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]/android.widget.TextView').click()
  driver.implicitly_wait(20)
  # scrolling for selecting the first item
  scroll= TouchAction(driver)
  scroll.press(x=380, y=1128).move_to(x=394, y=475).release().perform()
  driver.implicitly_wait(30)

  # selecting the first item
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[1]').click()
  driver.implicitly_wait(30)

  #adding to watchlist
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Add to Watchlist"]').click()



def test_cart():
  '''Addd item on Cart'''
  # click on nav menu
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  driver.implicitly_wait(30)
  # click on categories
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[9]').click()
  driver.implicitly_wait(30)

  # click books and magazines
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.ImageView').click()
  driver.implicitly_wait(30)

  # clicking on audio books
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.widget.TextView').click()
  driver.implicitly_wait(30)

  # clicking on the first item 
  driver.find_element_by_id('com.ebay.mobile:id/textview_header_0').click()
  time.sleep(3)

  # scrolling to reach "add to cart butoon"
  scroll= TouchAction(driver)
  scroll.press(x=344, y=1158).wait(2000).move_to(x=344, y=611).release().perform()
 
  time.sleep(3)

  # clicking on "add to cart"
  driver.find_element_by_xpath('//android.widget.Button[@content-desc="Add to cart"]').click()
  time.sleep(3)
  driver.close()


def test_watching_List():
  '''TS_005: Check out Watching List'''
  # clicking on menu
  driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Main navigation, open"]').click()
  time.sleep(5)
  driver.find_element_by_id('com.ebay.mobile:id/nav_watching').click()
