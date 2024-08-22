from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

fp = webdriver.FirefoxProfile(r"C:\Users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\somestrinng.default")

firefox = webdriver.Firefox(firefox_profile=fp)
firefox.get('https://www.youtube.com/playlist?list=your_playlist_here')

max_scrolls = 22
scroll_count = 0
f = open("links.txt", "a", encoding="utf-8")

while scroll_count < max_scrolls:
	actions = ActionChains(firefox)
	actions.send_keys(Keys.END)
	actions.perform()
	time.sleep(5)
	scroll_count += 1
	print(scroll_count)

arr = firefox.find_elements(By.TAG_NAME, "a")

for x in arr:
	if x is not None:
		if x.text is not None:
			print(x.text)
			f.write(x.text + "\n")
		if x.get_attribute("href") is not None:
			print(x.get_attribute("href"))
			f.write(x.get_attribute("href") + "\n")
f.close()