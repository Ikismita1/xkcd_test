from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://xkcd.com/about/")

## Find number of links present on the webpage##
Links_count = driver.find_elements_by_tag_name("a")
print(len("Total links:", Links_count))


## Check link slashnet ##
driver.find_element_by_link_text('slashnet').click()
TITILE_SLASHNET = 'SlashNET'
try:
    title1 = driver.title
    assert 'SlashNET' in title1
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link xkcd ##
driver.find_element_by_link_text('xkcd').click()
try:
    title2 = driver.title
    assert 'xkcd - Wikipedia' in title2
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link Spanish ##
driver.find_element_by_link_text('Spanish').click()
try:
    title3 = driver.title
    assert 'xkcd-es - Ent-Mujeres' in title3
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link Russian ##
driver.find_element_by_link_text('Russian').click()
try:
    title4 = driver.title
    assert 'Эффект БДЛПСУДКС - xkcd по-русски' in title4
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link German ##
driver.find_element_by_link_text('German').click()
try:
    title5 = driver.title
    assert 'German' in title5
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link get out and meet each other ##
driver.find_element_by_link_text('get out and meet each other').click()
try:
    title6 = driver.title
    assert 'Geohashing' in title6
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link geohashing ##
driver.find_element_by_link_text('geohashing').click()
try:
    title7 = driver.title
    assert 'xkcd: Geohashing' in title7
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link gallery of photos ##
driver.find_element_by_link_text('gallery of photos').click()
try:
    title8 = driver.find_element_by_xpath("//font[contains(text(),'People playing chess on roller coasters')]").text
    assert 'People playing chess on roller coasters' in title8
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link comic#249 ##
driver.find_element_by_link_text('comic #249').click()
try:
    title9 = driver.title
    assert 'xkcd: Chess Photo' in title9
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link whatif ##
#---- FAILED CASE____#
driver.find_element_by_link_text('What If').click()
try:
    title10 = driver.title
    assert '404 Not Found' in title10
    print('SERVER ERROR')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link Thing Explainer link##
driver.find_element_by_link_text('Thing Explainer').click()
try:
    title11 = driver.title
    assert 'Thing Explainer: Complicated Stuff in Simple Words' in title11
    print('Pass')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link Christina Gleason link##
#---- FAILED CASE____#
driver.find_element_by_link_text('Christina Gleason').click()
try:
    title12 = driver.title
    assert 'Privacy error' in title12
    print("It's not secured")
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link Long Titles link##
#---- FAILED CASE____#
driver.find_element_by_link_text('Long Titles').click()
try:
    title13 = driver.find_element_by_xpath("//div[contains(text(),'Oops! We can’t find that page')]").text
    assert 'Oops! We can’t find that page' in title13
    print('PAGE COULD NOT BE FOUND')
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link Mozilla Bug #45375 link##
driver.find_element_by_link_text('Mozilla Bug #45375').click()
driver.implicitly_wait(10)
try:
    title14 = driver.find_element_by_xpath("//header/div[1]/h1[1]/a[1]").text
    assert 'Bugzilla' in title14
    print("PASS")
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link this link##
#---- FAILED CASE____#
driver.find_element_by_link_text('this').click()
try:
    title15 = driver.find_element_by_xpath("//div[contains(text(),'Oops! We can’t find that page')]").text
    assert 'Oops! We can’t find that page' in title15
    print('PAGE COULD NOT BE FOUND')
except Exception as e:
    print('Fail', format(e))
driver.back()

## Check link The Pleiades link##
driver.find_element_by_link_text('The Pleiades').click()
try:
    title16 = driver.title
    assert 'Pleiades - Wikipedia' in title16
    print("PASS")
except Exception as e:
    print('Fail', format(e))
driver.back()


## Check link Back to main link##
driver.find_element_by_link_text('Back to main').click()
try:
    title17 = driver.title
    assert 'xkcd: Interruption' in title17
    print("PASS")
except Exception as e:
    print('Fail', format(e))
driver.back()





