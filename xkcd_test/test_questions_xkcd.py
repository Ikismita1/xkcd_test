from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://xkcd.com/about/")

QUESTION_1 = driver.find_element_by_xpath("//h3[contains(text(),'Who are you?')]")
QUESTION_2 = driver.find_element_by_xpath("//h3[contains(text(),'What else do you do?')]")
QUESTION_3 = driver.find_element_by_xpath("//h3[contains(text(),'Who else are you?')]")
QUESTION_4 = driver.find_element_by_xpath("//h3[contains(text(),'What does XKCD stand for?')]")
QUESTION_5 = driver.find_element_by_xpath("//h3[contains(text(),'Where did all this start?')]")
QUESTION_6 = driver.find_element_by_xpath("//h3[contains(text(),'Why can't I read the whole comic mouseover text in')]")
QUESTION_7 = driver.find_element_by_xpath("//h3[contains(text(),'Can we print xkcd in our magazine/newspaper/other ')]")
QUESTION_8 = driver.find_element_by_xpath("//h3[contains(text(),'How can I find the date a comic was posted?')]")
QUESTION_9 = driver.find_element_by_xpath("//h3[contains(text(),'Is there an interface for automated systems to acc')]")
QUESTION_10 = driver.find_element_by_xpath("//h3[contains(text(),'What is your favorite astronomical entity?')]")



## Compare question "Who are you?"##
def question_who_are_you(self):
    question_expected1 = "Who are you?"
    self.assertEqual(question_expected1, QUESTION_1)


## Compare question "What else do you do?"##
def question_what_else_do_you_do(self):
    question_expected2 = "What else do you do?"
    self.assertEqual(question_expected2, QUESTION_2)


## Compare question "Who else are you?"##
def question_who_else_are_you(self):
    question_expected3 = "Who else are you?"
    self.assertEqual(question_expected3, QUESTION_3)


## Compare question "What does XKCD stand for?"##
def question_what_does_XKCD_stands_for(self):
    question_expected4 = "What does XKCD stand for?"
    self.assertEqual(question_expected4, QUESTION_4)


## Compare question "Where did all this start?"##
def question_where_did_all_this_start(self):
    question_expected5 = "Where did all this start?"
    self.assertEqual(question_expected5, QUESTION_5)


## Compare question "Why can't I read the whole comic mouseover text in Firefox?"##
def question_why_cant_I_read_the_comic(self):
    question_expected6 = "Why can't I read the whole comic mouseover text in Firefox?"
    self.assertEqual(question_expected6, QUESTION_6)


## Compare question "Can we print xkcd in our magazine/newspaper/other publication?"##
def question_can_we_print_xkcd_in_our_magazzine(self):
    question_expected7 = "Can we print xkcd in our magazine/newspaper/other publication?"
    self.assertEqual(question_expected7, QUESTION_7)


## Compare question "How can I find the date a comic was posted?"##
def question_how_can_I_find_a_comic(self):
    question_expected8 = "How can I find the date a comic was posted?"
    self.assertEqual(question_expected8, QUESTION_8)


## Compare question "Is there an interface for automated systems?"##
def question_is_there_an_interface(self):
    question_expected9 = "Is there an interface for automated systems?"
    self.assertEqual(question_expected9, QUESTION_9)


## Compare question "What is your favorite astronomical entity?"##
def question_what_is_your_favorite_astronomical_entity(self):
    question_expected10 = "What is your favorite astronomical entity?"
    self.assertEqual(question_expected10, QUESTION_10)



