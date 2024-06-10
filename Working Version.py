from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv('credential.env')
chromeDriver = os.getenv("chromeDriver")

def scrape_imdb_top_movies(num_pages):
    options = webdriver.ChromeOptions()
    chromedriver_path = chromeDriver  # Use raw string to specify the path
    options.add_argument(f'--webdriver-executable={chromedriver_path}')  # Specify Chromedriver executable path
    driver = webdriver.Chrome(options=options)

    movie_list = []

    for page in range(num_pages):
        url = f"https://www.imdb.com/chart/top/"
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'h3'))) #(1) 
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cli-title-metadata'))) #(2)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="ratingGroup--imdb-rating"]'))) #(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ipc-html-content-inner-div'))) #(4)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.sc-74bf520e-6.bbdzqJ'))) #(5)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.sc-74bf520e-6.bbdzqJ')))
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.sc-74bf520e-5.ePoirh a.dli-cast-item')))

        movie_elements = driver.find_elements(By.TAG_NAME, 'h3') #(1)
        #year_elements = driver.find_elements(By.CSS_SELECTOR, '.cli-title-metadata span.sc-b189961a-8.kLaxqf.cli-title-metadata-item') #(2)
        #rating_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="ratingGroup--imdb-rating"]') #(3)
        #synopsis_elements = driver.find_elements(By.CSS_SELECTOR, '.ipc-html-content-inner-div') #(4)
        #director_elements = driver.find_elements(By.CSS_SELECTOR, 'span.sc-74bf520e-6.bbdzqJ + span.sc-74bf520e-5.ePoirh a.dli-director-item') #(5)
        #coDirector_elements = driver.find_elements(By.CSS_SELECTOR, 'span.sc-74bf520e-6.bbdzqJ + span.sc-74bf520e-5.ePoirh a.dli-director-item')
        #ipc-link ipc-link--base dli-director-item
        #cast_elements = driver.find_elements(By.CSS_SELECTOR, 'span.sc-74bf520e-5.ePoirh a.dli-cast-item')

        for element in movie_elements:
            try:
                title = element.text
                #year = element.text.strip('\n')
                #rating = element.text
                #synopsis = element.text
                #director = element.text
                #coDirector = coDirector.text
                #cast = element.text

                movie_list.append({
                    'title': title,
                    #'year': year,
                    #'rating (Start out of 10)': rating,
                    #'synopsis': synopsis,
                    #'director' : director,
                    #'coDirector' : coDirector,
                    #'cast' : cast
                })
            except Exception as e:
                print(f"Error: {e}")

    driver.quit()
    return pd.DataFrame(movie_list)

# Scrape the top movies and save to a DataFrame
df = scrape_imdb_top_movies(1)
print(df)   

df.head(17)

#df.to_csv('title.csv', index=False)

# pair 1 works with 1 to scrape title
# pair 2 works with 2 to scrape year, duration, restricted rating
# pair 3 works with 3 to scrape user rating
# pair 4 works with 4 to scrape synopsis
# pair 5 works with 5 to scrape director