import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 환경 변수에서 로그인 정보 가져오기
LOGIN_USER = os.getenv('LOGIN_USER')
LOGIN_PASS = os.getenv('LOGIN_PASS')

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# WebDriver 초기화
driver = webdriver.Chrome(options=chrome_options)

try:
    # 파워플래너 사이트 접속
        driver.get('https://pp.kepco.co.kr/')    
        # 로그인 처리    wait = WebDriverWait(driver, 10)
     
    # 아이디 입력
        username_field = wait.until(EC.presence_of_element_located((By.ID, 'RSA_USER_ID')))    
        username_field.send_keys(LOGIN_USER)    # 비밀번호 입력
        password_field = driver.find_element(By.ID, 'RSA_USER_PWD')    # 로그인 버튼 클릭
            password_field.send_keys(LOGIN_PASS)
        # 로그인 버튼 클릭    

        login_button = driver.find_element(By.ID, 'intro_btn_indi')
        login_button.click()
    # 데이터 추출 (실시간 사용량, 예상 사용량, 실시간 요금, 예상 요금)
    realtime_usage = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.realtime-usage'))).text
    estimated_usage = driver.find_element(By.CSS_SELECTOR, '.estimated-usage').text
    realtime_charge = driver.find_element(By.CSS_SELECTOR, '.realtime-charge').text
    estimated_charge = driver.find_element(By.CSS_SELECTOR, '.estimated-charge').text
    
    # JSON 형식으로 결과 출력
    result = {
        'realtime_usage': realtime_usage,
        'estimated_usage': estimated_usage,
        'realtime_charge': realtime_charge,
        'estimated_charge': estimated_charge
    }
    
    print(json.dumps(result))
    
finally:
    driver.quit()
