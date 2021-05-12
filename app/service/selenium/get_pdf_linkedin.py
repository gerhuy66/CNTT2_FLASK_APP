from os import scandir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdfkit
# import requests
from pdfkit.api import configuration
wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("incognito")

driver = webdriver.Chrome(executable_path="D:\study\DUANCNTT2\Scapy\selenium\chromedriver.exe",chrome_options=chrome_options)
driver.maximize_window()


driver.get("https://www.linkedin.com/")
driver.find_element_by_id("session_key").send_keys("duchuy1096@gmail.com")
driver.find_element_by_id("session_password").send_keys("megamind0122")
driver.find_element_by_class_name("sign-in-form__submit-button").click()

# element = WebDriverWait(driver,200).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[3]/div/div/div/div/footer/div/div/p"))
# )

def getpdf_from_url(url,folder_name):
    #boilpipe
    driver.get(url)
    file_name = url.split("/")[len(url.split("/"))-1]
    #open file with *.html* extension to write html

    file= open("linkedin_profile.html","+w")
    #write then close file
    file.write(driver.page_source)
    file.close()
    extractor = extractors.ArticleExtractor()
    # From a file
    doc = extractor.get_doc_from_file("linkedin_profile.html")
    print("############################################################")
    print("############################################################")
    print("############################################################")
    print(doc.content)
    return True

    script = "window.scrollBy(0,999999999999);window.scrollBy(0,-400);"
    driver.execute_script(script)
    try:
        element = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "ember85")))
    except:
        return False
    click_success = False
    scroll_count = 0
    while not click_success:
        try:
            driver.execute_script('''
                document.querySelector('[data-control-name="skill_details"]').click();
            ''')
            click_success = True
        except:
            if scroll_count == 20:
                break
            print("script error: can't find element [data-control-name='skill_details'], try to scroll up...")
            script = '''window.scrollBy(0,-100);'''
            scroll_count += 1
            driver.execute_script(script)
        
    options = {
        'page-size': 'A4',
        'orientation': 'Landscape',
        'quiet': '',
        'dpi': 96,
        'margin-top': '0.2in',
        'margin-bottom': '0.2in',
        'margin-right': '0.72in',
        'margin-left': '0.72in',
        'encoding': "UTF-8"
    }
    try:
        wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf= wkhtmltopdf_path)
        file_name = file_name+".pdf"
        path = os.path.join(folder_name,file_name)
        # pdfkit.from_string(driver.page_source,path,configuration=config,options=options)
        
       
    except:
        return False
    return True

# getpdf_from_url("https://www.linkedin.com/in/tr%C3%BAc-anh-nguy%E1%BB%85n-tr%E1%BA%A7n-71397352")
import os
from boilerpy3 import extractors
file_path = "D:\study\DUANCNTT2\scapy\selenium\data"
save_path = "D:\study\DUANCNTT2\scapy\selenium\linkedin"
count = 0
for filename in os.listdir(file_path):
    file = open(file_path+"\\"+filename,"r")
    links = file.readlines()
    
    # Parent Directory path
    parent_dir = save_path

    # Path
    path = os.path.join(parent_dir, filename.replace(".txt",""))
    # os.mkdir(path)
    for l in links:
        l = l.split('?')[0]
        rs = getpdf_from_url(l.replace('\n',''),path)
        break
        if rs:
            print("Crawl success: "+l)
            count+=1
        else:
            print("Crawl fail: "+l)
        
print("totals: "+str(count))