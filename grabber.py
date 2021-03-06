import time
import selenium.webdriver.support.ui as ui
from selenium import webdriver
import re
import platform

class GradeGrabber:
    def __init__(self):
        #self.uniqname = uniqname
        #self.password = password
        self.url = 'https://csprod.dsc.umich.edu/services/student'
        return

    def grab(self, uniqname, password, filename, bType):
        try:
            # Init browser
            if bType.lower() == "f":
                self.browser = webdriver.Firefox()
            elif bType.lower() == "c":
                if platform.system() == "Linux":
                    self.browser = webdriver.Chrome(executable_path='./chromeDriver_linux')
                elif platform.system() == "Darwin":
                    self.browser = webdriver.Chrome(executable_path='./chromeDriver_osx')
                elif platform.system() == "Windows":
                    self.browser = webdriver.Chrome(executable_path='./chromeDriver_win.exe')
                else:
                    raise Exception("Unsupported Platform: {}".format(platform.system()))
            else:
                raise Exception("Invalid browser type!")

            # Get Wolverine Access student business page
            self.browser.get(self.url)
            wait = ui.WebDriverWait(self.browser, 120) # time out after 10 seconds

            # Login to Wolverine Access
            self.browser.find_element_by_id('login').send_keys(uniqname)
            self.browser.find_element_by_id('password').send_keys(password)
            self.browser.find_element_by_id('loginSubmit').click()
            #wait.until(lambda driver: self.browser.find_elements_by_id('ptifrmtgtframe'))

            # Load transcript request page
            self.browser.switch_to_frame('TargetContent')
            self.browser.find_element_by_xpath("//a[@title='View an unofficial copy of your academic transcript.']").click()
            wait.until(lambda driver: self.browser.find_elements_by_id('ptifrmtgtframe'))

            # Request transcript
            self.browser.switch_to_frame('TargetContent')
            self.browser.find_element_by_id('GO').click()
            #wait.until(lambda driver: self.browser.find_element_by_id('ptifrmtgtframe').find_element_by_id('M_SR_TSCRPT_HDR_MESSAGE_PARM1'))
            time.sleep(10) # wait for the results to come out

            # Get all of the transcript entries
            self.browser.switch_to_default_content()
            self.browser.switch_to_frame('TargetContent')
            #print self.browser.page_source.encode('utf-8')

            results = self.browser.find_elements_by_xpath("//*[contains(@id, 'win0divDERIVED_TSCRPT_TSCRPT_COMP_DATA')]")

            self.writeFile(results, filename)
        except Exception, e:
            print "Error occured while grabbing transcript. Wolverine access is probably down."
            print e
            self.closeBrowser()
            return False
        self.closeBrowser()
        return True

    def writeFile(self, results, filename):
        transcript = ''

        for r in results:
            if re.match(r'Elections as of:', r.text) == None:
                transcript += r.text + '\n'

        f = open(filename, 'w')
        f.write(transcript)
        f.close()

    def closeBrowser(self):
        if self.browser != None:
            self.browser.quit()
        return


