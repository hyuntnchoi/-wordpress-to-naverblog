from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import subprocess
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# xml 가져오기
xmlfile = ET.parse('data.xml')
xmlroot = xmlfile.getroot()
ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}

# 크롬 실행
subprocess.Popen(['python', 'chrome_starter.py'])
time.sleep(2)

BLOG_URL = 'https://blog.naver.com/uto01111'

ser = Service('C:\\mywork\\wordpress-to-naverblog-lib\\chromedriver_win32\\chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(service=ser, options=chrome_options)
action = ActionChains(browser)

# 블로그 접속
browser.get(BLOG_URL)
browser.switch_to.frame('mainFrame')
time.sleep(2)

# 글 작성
for x in xmlroot.findall('channel/item'):

    # 글쓰기 버튼 클릭
    browser.find_element_by_xpath('//*[@id="post-admin"]/a[1]').click()
    time.sleep(2)

    # 제목과 본문 가져오기
    title = x.find('title').text
    content_html_format = x.find('content:encoded', ns).text
    soup = BeautifulSoup(content_html_format)
    content = soup.get_text('\n')

    # 본문 입력
    action = ActionChains(browser)
    time.sleep(1)
    action.send_keys(content).perform()
    time.sleep(2)

    # 제목 클릭
    browser.find_element_by_xpath('//span[contains(text(),"제목")]').click()
    time.sleep(1)

    # 제목 입력
    action.send_keys(title).perform()
    time.sleep(2)

    # 발행 버튼
    browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[3]/div[3]/button').click()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[3]/div[3]/div/div/div/div[8]/div/button').click()

    print('%s 발행 완료' % title)
    time.sleep(7)