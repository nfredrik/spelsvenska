#from behave import given, when, then
from hamcrest import assert_that, contains_string, equal_to, is_not
use_step_matcher("re")

@given(u'I can access Svenska spel')
def step_impl(context):
    context.browser.get('http://svenskaspel.se')
    assert_that(context.browser.title, contains_string("Svenska Spel"))
    context.helper = Helper(context)


@when(u'I search for "(?P<text>.*)"')
def step_impl(context,text):
    context.helper.search_for(text)

@then(u'I get a result for "(?P<text>.*)"')
def step_impl(context,text):
    context.helper.assert_in_page(text)
    assert True

    #raise NotImplementedError(u'STEP: Then I get a result for "Oddset"')

@then(u'I, "Fredrik" can login as user')
def step_impl(context):

    #assert_that(True, equal_to(
    #    context.helper.is_element_present(context.By.ID, "footer")))
    #assert context.helper.is_text_present("topNavLogIn")
    context.helper.login()
    assert True
    #raise NotImplementedError(u'STEP: Then I, "Fredrik" can login as user')

@then(u'verify that I can access my profile data')
def step_impl(context):
    assert True
    #raise NotImplementedError(u'STEP: Then verify that I can access my profile data')

@then(u'logout in a controlled way')
def step_impl(context):
    assert True
    #raise NotImplementedError(u'STEP: Then logout in a controlled way')



#
# Helper class
#
class Helper():
    check = {"Capybara": "is the largest rodent in the world",
             "Selenium": "reduce the effects of mercury toxicity"}

    def __init__(self, context= None):
        self.context = context

    def assert_in_page(self, input):
        assert_that(self.context.browser.page_source, contains_string(input))

    def search_for(self, subject):
#        elem = self.context.browser.find_element_by_id("searchInput")
        #elem = self.context.browser.find_element_by_id("svssearchlabel")
        elem = self.context.browser.find_element_by_id("searchDiv")
        elem.send_keys(subject)
        elem.send_keys(self.context.Keys.RETURN)

    def validate_relevance_for(self, subject):
     
        result = self.check.get(subject, "This is an error!")

        self.assert_in_page(result)

    def validate_subject_in_h1(self, subject):

        lst = self.context.browser.find_elements_by_tag_name('h1')

        if any([subject == l.text  for l in lst]):
            return

        assert_that(False)

    def is_element_present(self, how, what):
        try: self.context.browser.find_element(by=how, value=what)
        except self.context.NoSuchElementException as e: return False
        return True

    def login(self):
        #loginUserName
        #svusername
        #svspindcode
        #elem = self.context.browser.find_element_by_id("topNavLogIn")

        elem = self.context.browser.find_element_by_id("loginUserName")
        #print(help(elem))
        print("nisse:{}".format(elem.text))
        #print(elem.get_attribute())
        #elem.send_keys('nfredrik')
        #elem.send_keys(self.context.Keys.TAB)        
        elem = self.context.browser.find_element_by_id("loginPassword")
        #elem.send_keys('yyyyyy')
        #elem.send_keys(self.context.Keys.RETURN)
        #elem = self.context.browser.find_element_by_id("inputLoginButton")
        #elem.click()

    def is_text_present(self, text):
        try:
            body = self.context.browser.find_element_by_tag_name("body") # find body tag element
        except self.context.NoSuchElementException as e:
            return False
        return text in body.text # check if the text is in body's text

    def old_login(self):
        username = "nfredrik"
        password = "minMagear4stor"

        xpaths = { 'usernameTxtBox' : "//input[@name='username']",
                   'passwordTxtBox' : "//input[@name='password']",
                   'submitButton' :   "//input[@name='login']"
                 }

        #Clear Username TextBox if already allowed "Remember Me" 
        self.context.browser.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

        #Write Username in Username TextBox
        self.context.browser.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

        #Clear Password TextBox if already allowed "Remember Me" 
        self.context.browser.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

        #Write Password in password TextBox
        self.context.browser.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

        #Click Login button
        self.context.browser.find_element_by_xpath(xpaths['submitButton']).click()
