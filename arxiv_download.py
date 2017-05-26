from selenium import webdriver
import time
import datetime
import shutil

# to create a folder with the date of today
tds=str(datetime.date.today())

# setting chrome driver option with default download directories, and preferences
# note that the plugins has to be turned off in order to download the pdf file

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : '/Users/baileyhsu/Downloads/'+ tds,"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}]}
chrome_options.add_experimental_option('prefs', prefs)

# here I set my defauly url to be the computational physics section in arxiv.org

chromedriver = webdriver.Chrome(executable_path = '/Users/baileyhsu/Downloads/chromedriver',chrome_options = chrome_options)
url = 'https://arxiv.org/list/physics.comp-ph/recent'
chromedriver.get(url)

# here I use find elements by css selector to locate title names
# note that the space in the class name => using . to connect them
# the titlelist is also created for later convienence

title = chromedriver.find_elements_by_css_selector('div.list-title.mathjax')
titlelist=[]
for jt in title:
	titlelist.append(jt.text)


# here is the fun part. I search for all the links that comes with the text arXiv
# and obtained all the https links where i only need to replace the abs term to pdf
# in order to link to the pdf download page.
# urllist is created since we need to change the file name after downloading. Therefore
# I need to keep track of the name downloaded.

urllist=[]
links = chromedriver.find_elements_by_partial_link_text('arXiv:')
for link in links:
    url_new=str(link.get_attribute("href")).replace('abs','pdf')
#    chromedriver.get(url_new)
    urllist.append(url_new)

# the time.sleep setting here is set 2 mins because usually I would assume
# it would not take more than 2 mins to download all the papers in the front page

time.sleep(120)

# this part deals with changing the name to the title provided in the arxiv
# and move the whole directory to my documents folder

count = 0    
for url in urllist:
    file_name = url.strip('https://arxiv.org/pdf')
    file_name = file_name+'.pdf'    
    shutil.copy('/Users/baileyhsu/Downloads/'+ tds+ '/'+file_name, '/Users/baileyhsu/Downloads/'+ tds+ '/' + titlelist[count].replace("/","") +'.pdf')
    count = count + 1

shutil.move('/Users/baileyhsu/Downloads/'+ tds, '/Users/baileyhsu/Documents/Physics_Paper/')

chromedriver.quit()

