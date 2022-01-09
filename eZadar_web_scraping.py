from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import requests, csv, numpy as np, time, json

def dohvati_kategorije():
    # Send GET request
    url = 'https://ezadar.net.hr/'
    data = requests.get(url)

    # Making the soup
    soup = BeautifulSoup(data.text, 'html.parser')
    #print(soup.prettify())

    # File for category links  
    f = open("linkoviKategorije.txt","w")

    # Find and write all navigation links in file
    for a in soup.find_all("a","Navigation-link"):
        f.write(a['href'] + "\n")
    f.close()
    
def dohvati_linkove_clanaka():
    # Read category links
    with open("linkoviKategorije.txt" , "r") as f:
        lines = f.readlines()

    counter = np.arange(2000, dtype=int)
    
    for line in lines:   
        print("Changing category!")
        for pageCnt in counter[1:]:
        #for pageCnt in counter:
            # Create link for each category and page number
            url = 'https://ezadar.net.hr/arhiva/' + line.split("/")[3] + "/?stranica=" + str(pageCnt)
            print(url)
            data = requests.get(url)
            soup = BeautifulSoup(data.text, 'html.parser')
            
            # Find Article links
            for a in soup.find_all("a","News-link"):
                
                print(a['href'])
                data = requests.get(a['href'])
                soup = BeautifulSoup(data.text, 'html.parser')
                
                # Date control
                timeTag = soup.find("time")
                datum = timeTag['datetime'].split(" ")[0]
                
                datum = datum.split("-")
                d1 = datetime(int(datum[0]),int(datum[1]),int(datum[2])) 
                d2 = datetime(2020,12,31)
                d3 = datetime(2022,1,1)
                print("Article date: ")
                print(d1)
                
                if d1 <= d2:
                    # Don't write article link if date before 31.12.2020
                    # Break the inner loop...
                    break
                elif (d1 >=d3):
                    # Don't write article link if date after 01.01.2022
                    continue
                else:
                    # Write article link in file
                    d = open("linkoviClanaka.txt","a")
                    print("Writing link in file!")
                    d.write(a['href'] + "\n")
            else:
                # Continue if the inner loop wasn't broken.
                continue
            # Inner loop was broken, break the outer.
            break  
        
    d.close()    
    f.close()

def eZadar_scrap():
    with open("linkoviClanaka.txt") as f:
        lines = f.readlines()
    
    with open("eZadarPodaci.csv","a", encoding='utf-8') as csv_file:
        
        writer = csv.writer(csv_file)
        
        # DEFINE HEADERS
        header = ["ID","LINK", "NASLOV", "AUTOR", "POTPUNI TEKST", "DATUM OBJAVLJIVANJA", "KATEGORIJA", "FACEBOOK SHARES", "FACEBOOK LIKES", "TAG"]
        writer.writerow(header)
        
        articleID = 1003
        
        # Initialize Firefrox browser with default user
        # Deprecated way
        options = Options()
        profile = webdriver.FirefoxProfile('C:\\Users\\Boss\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\jq5cpfr7.default-release-1640173659683') # Windows
        #profile = webdriver.FirefoxProfile('/home/bluking/.mozilla/firefox/not30cpu.default-release') # Ubuntu
        #profile = webdriver.FirefoxProfile('/home/bluking/.mozilla/firefox/duiotsmo.joezi')
        options.headless = True
        options.profile = profile
        driver = webdriver.Firefox(options=options)
        
        # For each link in linkoviClanka.txt file 
        for line in lines:
            # Increment ID
            articleID += 1
            
            print(line.strip("\n"))
            # Send GET request 
            driver.get(line)
            
            # Accept cookies 
            try:
                driver.find_element(By.CSS_SELECTOR,'.fc-button.fc-cta-consent.fc-primary-button').click()
                print("Cookies accepted!")
            except NoSuchElementException:
                print("Accept cookies button not found!")

            # ARTICLE TITLE
            try:
                articleInner = driver.find_element(By.CLASS_NAME,'Article-inner') 
                articleNaslov = articleInner.find_element(By.TAG_NAME,'h1').text  
            except NoSuchElementException:
                print("Naslov not found!")
                
            
            # ARTICLE AUTHOR
            try:
                articleAuthor = driver.find_element(By.CLASS_NAME,'Article-author').text
                # If empty author is in another element found by xpath
                if(articleAuthor == ""):
                    articleAuthor = driver.find_element(By.XPATH,'//*[@target="_blank"]').text
            except NoSuchElementException:
                print("Autor not found!")

            # ARTICLE TEXT
            articleText = ''
            try:
                articleMeteredContent = driver.find_element(By.CLASS_NAME,'Article-meteredContent')  
                for p in articleMeteredContent.find_elements(By.TAG_NAME,'p'):
                    if(p.text == ""):
                        # If text <p> element is empty, try get <span> element
                        # Some contents in articles are written in <span> element
                        try:
                            articleText = articleText + p.find_element(By.TAG_NAME,'span').text
                        except NoSuchElementException:
                            print("Span element don't exsist")
                    else:    
                        articleText = articleText + p.text
            except NoSuchElementException:
                print("Tekst not found!")
            
            # ARTICLE PUBLISH DATE AND TIME
            try:
                articleDate = driver.find_element(By.TAG_NAME,'time').text
            except NoSuchElementException:
                print("Datum i vrijeme not found!")
            
            
                
            # ARTICLE CATEGORY (scrap from link)
            articleCategory = line.split("/")[3].capitalize()

            # ARTICLE TAG
            try:
                articleTag = driver.find_element(By.CLASS_NAME,'Article-subtitle').text
            except NoSuchElementException:
                print("Tag not found!")

            
            #FACEBOOK LIKES AND SHARES
            try:
                articleLikeNum = driver.find_element(By.XPATH,'//*[@data-type="like"]').text
            except NoSuchElementException:
                print("Likes not found!")
            
            try:
                articleShareNum = driver.find_element(By.XPATH,'//*[@data-type="share"]').text
            except NoSuchElementException:
                print("Shares not found!")    

            if (articleLikeNum == ""):
                articleLikeNum = 0
            if (articleShareNum == ""):
                articleShareNum = 0
            

            # Scroll to bottom of the page
            driver.execute_script("window.scrollTo(0,1650);") # document.body.scrollHeight

            # wait 3 seconds
            #time.sleep(3)
                
            # FACEBOOK COMMENTS
            #try:
            #    delay = 4
            #    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@title="fb:comments Facebook Social Plugin"]')))
            #    print ("Facebok frame present!")
            #except TimeoutException:
            #    print ("Facebok frame not present!")

            #try:
            #    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@title="fb:comments Facebook Social Plugin"]'))
            #    print("Switched to facebook frame!")
            #except NoSuchElementException:
            #    print("Facebook frame not found!")
                
            #try:
            #    articleCommentNum = driver.find_element(By.CLASS_NAME,'_50f7').text
            #except NoSuchElementException:
            #    articleCommentNum = 'Nemoguće dohvatiti'
            #    print("Comment number not found!")
                            
            # ARTICLE FACEBOOK COMMENTS    
            #articleFacebookComments = []
            #try:
            #    for div in driver.find_elements(By.CLASS_NAME,'_3-8y'):
            #        span = div.find_element(By.CLASS_NAME,'_5mdd')
            #        commentText = span.find_element(By.TAG_NAME,'span').text
            #        articleFacebookComments.append(commentText)
            #except NoSuchElementException:
            #    print("Cant find comments!")
            
                
            clanak = [articleID,line.strip("\n"),articleNaslov,articleAuthor,articleText,articleDate,articleCategory,articleShareNum,articleLikeNum,articleTag]
            writer.writerow(clanak)
            
    driver.close()
 
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        # Convert each csv row into python dict
        for row in csvReader: 
            # Add this python dict to json array
            jsonArray.append(row)
  
    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

if __name__ == '__main__':
    #dohvati_kategorije()
    dohvati_linkove_clanaka()
    eZadar_scrap()  
    
    csvFilePath = r'eZadarPodaci.csv'
    jsonFilePath = r'eZadarPodaci.json'
    #csv_to_json(csvFilePath, jsonFilePath)