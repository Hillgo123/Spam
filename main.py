import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


spam_sites = [
    'https://www.scientificamerican.com/page/newsletter-sign-up/?origincode=2019_sciam_StayInformed_NewsletterSignUp',
    'https://www.scientology.org/daily-connect/?subscribe=1',
]
    

def get_email():
    return str(input("What's your email?"))

def spammer():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    _email = 'example@gmail.com'

    for url in spam_sites:
        driver.get(url)

        if url == 'https://www.scientificamerican.com/page/newsletter-sign-up/?origincode=2019_sciam_StayInformed_NewsletterSignUp':
            try:
                driver.find_element("xpath", "//input[@name='email']").send_keys(_email)
                driver.find_element("xpath", "//input[@name='emailConfirmation']").send_keys(_email)
                driver.execute_script("window.scrollTo(0, 1100)")
                driver.find_element("xpath", "//input[@name='List_OptIn_Internal']").click()
                driver.find_element("xpath", "//input[@name='List_OptIn_External']").click()
                driver.find_element("xpath", "//input[@name='List_EnglishAcceptedTC']").click()
                driver.find_element("xpath", "//button[@id='submitCreateAccount']").click()

            
            except Exception as e: 
                print(e)
                print('Scientific american failed')
        
        if url == 'https://www.scientology.org/daily-connect/?subscribe=1':
            try:
                driver.find_element("xpath", "//input[@name='firstName']").send_keys('Miro')
                driver.find_element("xpath", "//input[@name='email']").send_keys(_email)
                driver.find_element("xpath", "//button[@type='submit']").click()
                
            except Exception as e:
                print(e)
                print('Scientology failed')

    time.sleep(5)
    driver.quit()

def main():
    spammer()
    print('You got spam!')


if __name__ == '__main__':
    main()