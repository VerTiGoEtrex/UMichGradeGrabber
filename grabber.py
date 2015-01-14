import time
import selenium.webdriver.support.ui as ui
from selenium import webdriver
import re

class GradeGrabber:
	def __init__(self):
		#self.uniqname = uniqname
		#self.password = password
		self.url = 'https://csprod.dsc.umich.edu/services/student'
		return

	def grab(self, uniqname, password, filename):
		self.browser = webdriver.Firefox()
		#self.browser = webdriver.Chrome()
		self.browser.get(self.url)
		wait = ui.WebDriverWait(self.browser, 120) # time out after 10 seconds
		self.browser.find_element_by_id('login').send_keys(uniqname)
		self.browser.find_element_by_id('password').send_keys(password)
		self.browser.find_element_by_id('loginSubmit').click()
		#wait.until(lambda driver: self.browser.find_elements_by_id('ptifrmtgtframe'))
		self.browser.switch_to_frame('TargetContent')
		self.browser.find_element_by_xpath("//a[@title='View an unofficial copy of your academic transcript.']").click()
		wait.until(lambda driver: self.browser.find_elements_by_id('ptifrmtgtframe'))
		self.browser.switch_to_frame('TargetContent')
		self.browser.find_element_by_id('GO').click()

		#wait.until(lambda driver: self.browser.find_element_by_id('ptifrmtgtframe').find_element_by_id('M_SR_TSCRPT_HDR_MESSAGE_PARM1'))

		time.sleep(10) # wait for the results to come out

		self.browser.switch_to_default_content()
		self.browser.switch_to_frame('TargetContent')
		#print self.browser.page_source.encode('utf-8')

		results = self.browser.find_elements_by_xpath("//*[contains(@id, 'win0divDERIVED_TSCRPT_TSCRPT_COMP_DATA')]")

		self.writeFile(results, filename)
		self.closeBrowser()
		return results

	def writeFile(self, results, filename):
		transcript = ''

		for r in results:
                    if re.match(r'Elections as of:', r.text) == None:
                        transcript += r.text + '\n'

		f = open(filename, 'w')
		f.write(transcript)
		f.close()

	def closeBrowser(self):
		self.browser.quit()
		return


