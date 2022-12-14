import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ssn.trainings.dlabanalytics.com/")
driver.maximize_window()

# ----------------- EPAM Sign in -------------
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'EPAM SSO').click()

time.sleep(10)

waitLogin = WebDriverWait(driver, 120)
waitLogin.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".mat-tooltip-trigger.ng-star-inserted")))

# ----------------- DATA LAB -------------
time.sleep(5)
env_name_trigger = driver.find_element(By.CSS_SELECTOR, ".mat-tooltip-trigger.ng-star-inserted")
env_name_trigger.click()

time.sleep(5)
jupyter_trigger = driver.find_element(By.CSS_SELECTOR, ".ellipsis.none-select.resources-url.mat-tooltip-trigger")
jupyter_trigger.click()

# ----------------- Jupyter -------------
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
waitJupyter = WebDriverWait(driver, 60)
waitJupyter.until(ec.visibility_of_element_located(
    (By.XPATH, '//a[@href="/apaulouskaya1/notebooks/final_task_Source_Check_Paulouskaya.ipynb"]')))

driver.implicitly_wait(5)
driver.find_element(By.XPATH, '//a[@href="/apaulouskaya1/notebooks/final_task_Source_Check_Paulouskaya.ipynb"]').click()

# ----------------- Notebook -------------
time.sleep(10)
driver.switch_to.window(driver.window_handles[2])
waitNotebook = WebDriverWait(driver, 60)
waitNotebook.until(ec.visibility_of_element_located(
    (By.XPATH, "//button[@data-jupyter-action='jupyter-notebook:confirm-restart-kernel-and-run-all-cells']")))

driver.implicitly_wait(10)
run_button = driver.find_element(By.XPATH,
                                 "//button[@data-jupyter-action='jupyter-notebook:confirm-restart-kernel-and-run-all-cells']")
run_button.click()

# ----------------- Tests -------------
time.sleep(10)
submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-sm.btn-danger")
submit_button.click()

time.sleep(20)
driver.switch_to.window(driver.window_handles[0])
driver.close()
