from os import scandir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="D:\study\DUANCNTT2\CV_SEARCH_FLASK_SOURCECODE\CNTT2_FLASK_APP\\app\service\selenium\chromedriver.exe",chrome_options=chrome_options)

driver.maximize_window()
jobs_title = ['java developer','AI developer','accounting','project manager','director']

def crawl_profile(job_tit):
    file = open("D:\study\DUANCNTT2\CV_SEARCH_FLASK_SOURCECODE\CNTT2_FLASK_APP\\app\service\selenium\\all_link.txt","r")
    link_list = []
    for line in file.readlines():
        link_list.append(line)



    print("LINKEDIN PROFILE FOR: "+job_tit)
    # login google
    driver.get("https://accounts.google.com/")
    driver.find_element_by_id("identifierId").send_keys("duchuy1096@gmail.com")
    driver.find_element_by_id("identifierNext").click()
    password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys("Metrohuy1770")
    password.send_keys(Keys.ENTER)
    driver.get ("https://www.google.com")

    # login linked in
    driver.get("https://www.linkedin.com/")
    driver.find_element_by_id("session_key").send_keys("duchuy1096@gmail.com")
    driver.find_element_by_id("session_password").send_keys("megamind0122")
    driver.find_element_by_class_name("sign-in-form__submit-button").click()

    driver.find_element_by_name("q").send_keys('site:linkedin.com/in AND "VietNam"')
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
    driver.find_element_by_id("hdtb-tls").click()
    driver.execute_script('''
    document.querySelectorAll(".KTBKoe").forEach(function(item){
        if(item.outerText == 'Mọi lúc')
            item.click();
    
    });

    setTimeout(function(){
    document.querySelectorAll(".tnhqA > a").forEach(function(link){
        if(link.outerText == '24 giờ qua')
            link.click();
    });
    },1000)

    ''')
    # return ""

    element = WebDriverWait(driver,200).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/a/h3"))
    )

    driver.execute_script('''
    document.querySelectorAll('a').forEach(function(node){
        if(node.href.includes('linkedin.com/in/') && !node.href.includes('translate.google.com') && !node.href.includes('google.com/search?'))
            node.name = 'profile_linkedin';
        if(node.href.includes('/search?q')){
            if(node.getAttribute("aria-label") != null)
                node.name = "page_"+ node.getAttribute("aria-label").replace("Page ","")
        }
        });
    ''')
    count = 1
    all_link = driver.find_elements_by_name('profile_linkedin')
    for link in all_link:
        print(str(count)+". "+link.get_attribute("href"))
        count += 1
        if link not in link_list:

            link_list.append(link.get_attribute("href"))
            print("Auto Crawler added: "+str(link.get_attribute("href")))

    # for page in range(2,5):
    #     driver.implicitly_wait(3)
    #     driver.find_element_by_name("page_"+str(page)).click()
    #     element = WebDriverWait(driver,200).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/a/h3"))
    #     )
    #     driver.execute_script('''
    #     document.querySelectorAll('a').forEach(function(node){
    #         if(node.href.includes('linkedin.com/in/') && !node.href.includes('translate.google.com') && !node.href.includes('google.com/search?'))
    #             node.name = 'profile_linkedin';
    #         if(node.href.includes('/search?q')){
    #             if(node.getAttribute("aria-label") != null)
    #                 node.name = "page_"+ node.getAttribute("aria-label").replace("Page ","")
    #         }
    #         });
    #     ''')
    #     all_link = driver.find_elements_by_name('profile_linkedin')
    #     for link in all_link:
            
    #         print(str(count)+". "+link.get_attribute("href"))
    #         count += 1
    #         link_list.append(link.get_attribute("href"))
    file = open(job_tit+'.txt', 'w+')
    for line in link_list:
        file.write("%s\n" % line)

