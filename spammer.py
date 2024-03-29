import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

spam_sites = [
    'https://www.scientificamerican.com/page/newsletter-sign-up/?origincode=2019_sciam_StayInformed_NewsletterSignUp',
    'https://www.scientology.org/daily-connect/?subscribe=1',
    'https://nordace.com/en/',
    'https://www.kohls.com/homepage/sale_alert_signup.jsp',
    'https://www.bananarepublic.co.uk/interstitial/UK/BananaRepublic/index.html',
    'https://www.target.com/',
]


email_check = True
while email_check == True:
    _email = str(input("What's your email?"))

    if '@' in _email and '.' in _email:
        email_check = False


def spammer():
    driver = webdriver.Chrome(service=ChromeService(
        executable_path=ChromeDriverManager().install()), options=options)
    for url in spam_sites:
        driver.get(url)

        if url == 'https://www.scientificamerican.com/page/newsletter-sign-up/?origincode=2019_sciam_StayInformed_NewsletterSignUp':
            try:
                driver.find_element(
                    "xpath", "//input[@name='email']").send_keys(_email)
                driver.find_element(
                    "xpath", "//input[@name='emailConfirmation']").send_keys(_email)
                driver.execute_script("window.scrollTo(0, 1100)")
                driver.find_element(
                    "xpath", "//input[@name='List_OptIn_Internal']").click()
                driver.find_element(
                    "xpath", "//input[@name='List_OptIn_External']").click()
                driver.find_element(
                    "xpath", "//input[@name='List_EnglishAcceptedTC']").click()
                driver.find_element(
                    "xpath", "//button[@id='submitCreateAccount']").click()

            except Exception as e:
                print(e)
                print('Scientific american failed')

        if url == 'https://www.scientology.org/daily-connect/?subscribe=1':
            try:
                driver.find_element(
                    "xpath", "//input[@name='firstName']").send_keys('name')
                driver.find_element(
                    "xpath", "//input[@name='email']").send_keys(_email)
                driver.find_element(
                    "xpath", "//button[@type='submit']").click()

            except Exception as e:
                print(e)
                print('Scientology failed')

        if url == 'https://nordace.com/en/':
            try:
                driver.find_element(
                    "xpath", "//input[@name='input_1']").send_keys(_email)
                driver.find_element("xpath", "//input[@type='submit']").click()

            except Exception as e:
                print(e)
                print('Nordace failed')

        if url == 'https://www.kohls.com/homepage/sale_alert_signup.jsp':
            try:
                driver.find_element(
                    "xpath", "//input[@name='enterEmail']").send_keys(_email)
                driver.find_element(
                    "xpath", "//input[@name='emailConfirm']").send_keys(_email)
                driver.find_element(
                    "xpath", "//button[@class='addtolist']").click()

            except Exception as e:
                print(e)
                print('Kohls failed')

        if url == 'https://www.bananarepublic.co.uk/interstitial/UK/BananaRepublic/index.html':
            try:
                driver.find_element(
                    "xpath", "//input[@name='email']").send_keys(_email)
                driver.find_element(
                    "xpath", "//input[@class='sds_absolute']").click()

            except Exception as e:
                print(e)
                print('Banana republic failed')

        if url == 'https://www.target.com/':
            try:
                driver.find_element(
                    "xpath", "//input[@name='email-address']").send_keys(_email)
                driver.find_element(
                    "xpath", "//button[@id='submit-button']").click()

            except Exception as e:
                print(e)
                print('Target failed')

    time.sleep(5)
    driver.quit()
    print('You got spam!')


def main():
    spammer()


if __name__ == '__main__':
    main()
