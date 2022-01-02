from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pandas as pd
from PIL import ImageOps
from PIL import Image
import os
import pickle

#https://chromedriver.chromium.org/downloads
#https://sites.google.com/a/chromium.org/chromedriver/home

##when you update chrome on the PC, it changes settings. If you get this error msh


project_dir = r'C:\PythonProjects\py_newSiteScrape'
driver_dir = "chrome_driver96"


driver_location = r"{}\{}\chromedriver.exe".format(project_dir, driver_dir)
pickle_cookies = r"{}\{}\cookies.pkl".format(project_dir, driver_dir)


saveDIR_out = project_dir + '\\img_save\\'
saveDIR_out2 = project_dir + '\\news_photos\\'  ### just another folder. Can remove #TODO
saveDIR_out3 = project_dir + '\\news_photos\\' ## saves with timestamp

EXCEL_FILE = project_dir + "\\new_sites1.xlsx"
CSV_FILE = project_dir + "\\new_sites1.csv"


chrome_data_path = project_dir + '\chrome-data'

chrome_options = webdriver.ChromeOptions()
prefs = {
    "translate_whitelists": {"pt": "en", "de":"en", "es":"en", "ja":"en",
    "sv":"en", "ko":"en", "zh-CN":"en","ru":"en","fr":"en", "no":"en",
    "id":"en","tr":"en","it":"en","zh-TW":"en"},
    "translate": {"enabled": "true"}
}
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.binary_location = driver_location


from selenium_chrome import Chrome

chrome = Chrome()
chrome.get('https://www.google.com')

webdriver.Chrome(executable_path=driver_location, options= chrome_options)
##https://ctrlq.org/code/19899-google-translate-languages
browser = webdriver.Chrome(driver_location ) #r"C:\path\to\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
prefs = {
    "translate_whitelists": {"pt": "en", "de":"en", "es":"en", "ja":"en", 
    "sv":"en", "ko":"en", "zh-CN":"en","ru":"en","fr":"en", "no":"en",
    "id":"en","tr":"en","it":"en","zh-TW":"en"},
    "translate": {"enabled": "true"}
}
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.binary_location(driver_location)
# chrome_options.add_argument('window-size=375x875')  #hights x width
chrome_options.add_argument(
    'whitelisted-ips')  # not surw what this does
#chrome_options.add_argument("user-data-dir=C:\\Users\\paperspace\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


chrome_options.add_argument("user-data-dir=" + chrome_data_path)

#chrome_options.addArguments("--disable-notifications");
##copy over chrome folder
#chrome_options.add_argument("--user-data-dir=chrome-data")  ##to add cookies? https://stackoverflow.com/questions/15058462/how-to-save-and-load-cookies-using-python-selenium-webdriver


#chrome_options.add_argument('headless')  ## if you do headless it wont translate

#https://selenium.dev/selenium/docs/api/javascript/module/selenium-webdriver/index_exports_Key.html
def saveImageSite(url, window_size = [1024, 1366],
                  saveFile1 = 'screenshot_noHeadless_sized_10.png',
                  saveFile2 = 'screenshot_noHeadless_sized_10.png',
                  chrome_driver = driver_location,
                  chrome_options = chrome_options):
    #chrome_driver = driver_location

    timeout = 2 * 60  # [seconds]
    timeout_start = time.time()
    driver = webdriver.Chrome(chrome_driver,
                              options=chrome_options)  # Optional argument, if not specified will se
    cookies = pickle.load(open(pickle_cookies, "rb"))
    # for cookie in cookies:
    #     driver.add_cookie(cookie)

    driver.set_window_size(window_size[0], window_size[1])
    #url = 'www.cnbc.com'
    driver.get(url)
    #driver.execute_script("window.scrollTo(0, 1000);")
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_UP)
    driver.save_screenshot(saveFile1)
    #body.send_keys(Keys.PAGE_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #driver.save_screenshot(saveFile2)
    driver.quit()
    if time.time() > timeout_start + timeout:
        driver.quit()
        #continue

def saveImageSite_globo(url, window_size = [1500, 600],
                saveFile1 = 'screenshot_noHeadless_sized_10.png',
                saveFile2 = 'screenshot_noHeadless_sized_10.png',
                chrome_driver = driver_location,
                chrome_options = chrome_options):


    driver = webdriver.Chrome(chrome_driver,
                              options=chrome_options)  # Optional argument, if not specified will se

    driver.set_window_size(window_size[0], window_size[1])
    driver.get(url)
    #driver.execute_script("window.scrollTo(0, 1000);")
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.PAGE_UP)
    driver.save_screenshot(saveFile1)
    body.send_keys(Keys.PAGE_DOWN)
    body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    driver.save_screenshot(saveFile2)
    driver.quit()


def saveImageSite_scrollDown(url, window_size = [1500, 600],
                  saveFile1 = 'screenshot_noHeadless_sized_10.png',
                  scroll_down_xtimes = 10,
                  chrome_driver = driver_location,
                  chrome_options = chrome_options):

    timeout = 2 * 60  # [seconds]
    timeout_start = time.time()
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)  # Optional argument, if not specified will se
    cookies = pickle.load(open(pickle_cookies, "rb"))
    #for cookie in cookies:
    #    driver.add_cookie(cookie)
    driver.set_window_size(window_size[0], window_size[1])
    driver.get(url)

    body = driver.find_element_by_css_selector('body')

    for item in range(0, scroll_down_xtimes):
        body.send_keys(Keys.ARROW_DOWN)

    driver.save_screenshot(saveFile1)
    #body.send_keys(Keys.PAGE_DOWN)
    #body.send_keys(Keys.PAGE_UP)
    #body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #body.send_keys(Keys.ARROW_DOWN)
    #driver.save_screenshot(saveFile2)
    #driver.execute_script("window.scrollTo(0, 1000);")
    driver.quit()
    if time.time() > timeout_start + timeout:
        driver.quit()
        #continue

def crop_image(img_file, crop_area = (0,100,0,100)):
    img = Image.open(img_file)
    #border = (0, 30, 0, 30) # left, up, right, bottom
    cropped = ImageOps.crop(img, crop_area)
    split_name = img_file.split(".")
    cropped.save(split_name[0] + "_crop" + ".png", 'PNG')

def crop_image_resize(img_file, outfile, crop_area=(0, 100, 0, 100),
                      resize_pixels = (800,800)):
    img = Image.open(img_file)
    # border = (0, 30, 0, 30) # left, up, right, bottom
    cropped = ImageOps.crop(img, crop_area)
    cropped.resize(resize_pixels)
    split_name = img_file.split(".")
    cropped.save(split_name[0] + "_crop_resized" + ".png", 'PNG')
    cropped.save(outfile, 'PNG')

def resize_img(img_file, newsize = (800, 800)):
    img = Image.open(img_file)
    im1 = img.resize(newsize)
    split_name = img_file.split(".")
    im1.save(split_name[0] + "_resized" + ".png", 'PNG')


site_list = pd.read_excel(EXCEL_FILE, sheet_name="Sheet1")
#site_list = pd.read_csv(CSV_FILE)
#CSV_FILE =
#site_list = pd.read_csv()

website_urls = site_list['websiteURL'].values
savefiles_out = site_list['fileName'].values


os.chdir(saveDIR_out)
print(datetime.datetime.now())

site_list = site_list.sort_values(by=['websiteNUM'])
list(site_list)
#ind= 1
for ind in site_list.index:
    #print(site_list['websiteURL'][ind])
    #ind = 1
    scroll_down_ind = site_list['scroll_down_times'][ind]
    saveFile1 = saveDIR_out + savefiles_out[ind] + ".png"
    saveFile2 = saveDIR_out2 + savefiles_out[ind] + ".png"
    saveFile3 = saveDIR_out3 + savefiles_out[ind] +"_" +  datetime.datetime.now().strftime("%Y%m%d") + ".png"
    url_ind = website_urls[ind]
    print(url_ind)
    window_size0 = site_list['window_size_0'][ind]
    window_size1 =site_list['window_size_1'][ind]
    site_name = site_list['site_short_name'][ind]


    # while True:
    if site_name == 'globo_br':
        saveImageSite_globo(url_ind, saveFile1=saveFile1)
        pass

    if (scroll_down_ind > 0):
        saveImageSite_scrollDown(url_ind, window_size=[window_size0, window_size1], saveFile1=saveFile1,
                                 scroll_down_xtimes=scroll_down_ind, chrome_options=chrome_options)
    else:
        saveImageSite(url_ind, window_size=[window_size0, window_size1], saveFile1=saveFile1,
                      chrome_options=chrome_options)

    crop_ind = (site_list['crop_left'][ind], site_list['crop_up'][ind],
                site_list['crop_right'][ind], site_list['crop_bottom'][ind])
    crop_image_resize(saveFile1, saveFile2, crop_area=crop_ind)
    crop_image_resize(saveFile1, saveFile3, crop_area=crop_ind)




    #print(website_urls[ind], site_list['window_size_0'][ind])
    #add cropping


print(datetime.datetime.now())
