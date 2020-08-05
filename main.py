import json
import sys

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

keys, delay = ["email", "pwd", "driver", "endorse"], 4


def endorse(driver):
    """
    Endorse the person
    :param driver: Web driver
    """
    wait = WebDriverWait(driver, delay)
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "profile-content")))
        driver.execute_script("window.scrollTo(0, 3 * document.body.scrollHeight / 5);")
    except TimeoutException:
        print("Error on scroll to load skills.")
        return
    skills = '//ol[contains(@class, "pv-skill-categories-section__top-skills")]/li'
    buttons = './/div[1]/div[1]/div[1]/button'
    try:
        for skill in wait.until(EC.presence_of_all_elements_located((By.XPATH, skills))):
            button = WebDriverWait(skill, delay).until(EC.element_to_be_clickable((By.XPATH, buttons)))
            if button.get_attribute("aria-pressed") != "true":
                driver.execute_script("arguments[0].click();", button)
        print(f"\033[92mOK\033[0m")
    except TimeoutException:
        print("Endorsements failed")
        return


def goProfil(driver, plebeian):
    """
    Find the profile of the person to endorse
    :param driver: Web driver
    :param plebeian: List of persons to endorse
    """
    potentialDude = '//div[@class="display-flex"]/div/div/div/ul/li[1]/div/div'
    message = '/div[3]/div'
    profile = '/div[2]/a'
    wait = WebDriverWait(driver, delay)
    for dude in plebeian:
        print(dude + ": ", end="")
        driver.get(getUrl(dude))
        try:
            # Check that the person has a Linkedin account
            wait.until(EC.visibility_of_all_elements_located((By.XPATH, potentialDude)))
            # Checking we are connected to this person
            wait.until(EC.text_to_be_present_in_element((By.XPATH, potentialDude + message), "Message"))
            wait.until(EC.element_to_be_clickable((By.XPATH, potentialDude + profile))).click()
        except TimeoutException:
            print("Not found")
            continue
        endorse(driver)


def getUrl(name):
    return "https://www.linkedin.com/search/results/all/?keywords=" + name + "&origin=GLOBAL_SEARCH_HEADER"


def connect(conf):
    """
    Connect to the Linkedin account
    :param conf: json config
    """
    try:
        driver = Chrome(conf[keys[2]])
    except WebDriverException:
        sys.exit("Error while opening Chrome driver at " + conf[keys[2]])
    driver.get("https://www.linkedin.com/login")
    myButtonXpath = '//*[@id="app__container"]/main/div[2]/form/div[3]/button'
    username = "username"
    password = "password"
    wait = WebDriverWait(driver, delay)
    try:
        wait.until(EC.element_to_be_clickable((By.ID, username))).send_keys(conf[keys[0]])
        wait.until(EC.element_to_be_clickable((By.ID, password))).send_keys(conf[keys[1]])
        wait.until(EC.element_to_be_clickable((By.XPATH, myButtonXpath))).send_keys(Keys.ENTER)
        # Sanity check
        wait.until(EC.visibility_of_element_located((By.ID, "global-nav")))
    except TimeoutException:
        sys.exit("Error while signing in.")
    goProfil(driver, conf[keys[3]])


def check(conf):
    """
    Check the json config is well formed
    :param conf: json config, needs to contain these fields ["email", "pwd", "driver", "endorse"],
    the latter should be a list even if there is no one or only one person to endorse
    """
    for key in keys:
        if key not in conf or \
                (key == keys[-1] and type(conf[key]) != list) or (key != keys[-1] and type(conf[key]) != str):
            sys.exit("Error on key: " + key)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        sys.exit("Usage: python3 main.py config.json")
    with open(args[1]) as f:
        config = json.load(f)
    check(config)
    connect(config)
