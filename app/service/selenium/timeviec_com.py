from os import scandir
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def crawl_timviec():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("incognito")
    path = os.path.join(os.getcwd(),"app\\service\\selenium\\chromedriver.exe")
    driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
    driver.maximize_window()


    driver.get("https://timviec.com.vn/employer")
    driver.find_element_by_name("email").send_keys("duchuy1096@gmail.com")
    driver.find_element_by_name("password").send_keys("Metrohuy1770")
    driver.execute_script('document.querySelector(".btn-login").click()')
    element = WebDriverWait(driver,200).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/a/img"))
    )
    driver.execute_script('''
        setTimeout(function(){
             
            document.querySelector("div .closeModal > img").click();
            document.querySelector(".btn-candidate-show-modal").click();
           
        },1000)
    ''')
    element = WebDriverWait(driver,200).until(
        EC.presence_of_element_located((By.CLASS_NAME, "new-2021-item-candidate-name"))
    )
    link = driver.execute_script('''
        let link = "";
        setTimeout(function(){
            document.querySelector("div .closeModal > img").click();
            
            console.log("XOA THANH CONG");
        },2000)
        return document.querySelector(".new-2021-item-candidate-name").getAttribute("href");
    ''')

    driver.implicitly_wait(2)


    driver.get(link)
    token = driver.execute_script('''
        return document.querySelector("#btn-download-cv").getAttribute("data-href").split("/")[5];
    ''')
    print("token"+str(token))
    num = 580990 - 5000 - 5000
    for i in range(1,10000):
        # driver.get("https://timviec.com.vn/ung-vien?page="+str(i))
        # links = driver.execute_script('''
        # scrollBy(0,1000);
       
        # let links = [];
        # document.querySelectorAll(".new-2021-item-candidate-name").forEach(function(item){
        #     links.push(item.getAttribute("data-href"))
        # })
        # return links;
    
        # ''')
        url = "https://cv.timviec.com.vn/tai-cv-when-login-ntd/"+str(num - i)+"/"+token
        driver.get(url)
       