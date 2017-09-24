#all the current code, but compilling error

#https://www.dataquest.io/blog/web-scraping-tutorial-python/

import time
from bs4 import BeautifulSoup
import urllib
import requests
import csv
from datetime import datetime


job_listings = []

#gets the total number of job listings
r = urllib.urlopen('https://www.indeed.com/jobs?q=software+engineer&l=New+York%2C+NY').read()
soup = BeautifulSoup(r, "html.parser")
soup.prettify()
totalnum = soup.find('div', attrs = {'id': 'searchCount'})
totalnum = totalnum.text
totalnum = totalnum.split()
totalnum = totalnum[-1]
print totalnum



for i in range(0,50, 10):
    print "i: " + str(i)
    url = "https://www.indeed.com/jobs?q=software+engineer&l=New+York%2C+NY&start={}&pp=ABQAAAFdZjLp2AAAAAEVRKQ6AQEBBwIuOP22AZ8KzGLC4dfhydJvtupUByQDWnaIpvs2WmuQbQkywLPMwtXZovwajnXQbkVx".format(i)
    r = urllib.urlopen(url)
    soup = BeautifulSoup(r, "html.parser")
    soup.prettify()
    items = soup.find_all('a', class_='turnstileLink')
#printing all the hrefs
    for link in items:
        href = link.get('href')
        if href is None:
            continue
        else:
            job_listings.append(href)
            
sub_links = []          
for subs in job_listings:
    sub = "https://www.indeed.com" + subs
    sub_links.append(sub)

#code works up until this point
#15 links per page, but it says 1-10 on the html code...why is this the cas
thirdpartycount = 0
indeedlinks = []
#need to check if after indeed.com there is /cmp/ --> means its an indeed
#website


#capitalization matters
innovation_list = ['innovative', 'innovation', 'dynamic']
entrepreneur_list = ['entrepreneur', 'Entrepreneur','entrepreneurial', 'Entrepreneurial']
count = 0
for link in sub_links:
    print "testinglink"
    print "Total Count: " + str(count)
    innovationscore = 0;
    entrepreneurscore = 0;
    time.sleep(5)
    print link
    r2 = urllib.urlopen(link)
    soup2 = BeautifulSoup(r2, "html.parser")
    soup2.prettify()
    items = soup2.find('div', attrs={'id':'accessibilityBanner'})
    if(items == None):
        thirdpartycount=thirdpartycount+1
        count = count + 1
        print "Third Party Count: " + str(thirdpartycount)
    else:
        count = count + 1
        indeedlinks.append(link)
        r3 = urllib.urlopen(link)
        soup3 = BeautifulSoup(r3, "html.parser")
        soup3.prettify()
        jobtitle = soup3.find('b', attrs={'class':'jobtitle'})
        jobtitle = "Job Title: "+ jobtitle.text
        print jobtitle
        company = soup3.find('span', attrs={'class': 'company'})
        company = "Company: " + company.text
        print company
    #salary = soup3.find('span', attrs={'style':'white-space: nowrap'})
    #salary = "Salary: " + salary.text
    #print salary
    
        location = soup3.find('span', attrs={'class': 'location'})
        location = "Location: " + location.text
        print location
    
        jobdescription = soup3.find('span', {'id': 'job_summary'})
        for word in innovation_list:
            if word not in jobdescription.text:
                continue
            else:
                innovationscore = innovationscore + 1;
        for word in entrepreneur_list:
            if word not in jobdescription.text:
                continue
            else:
                entrepreneurscore = entrepreneurscore + 1;
            
            
        innovationscore = "Innovation Score: " + str(innovationscore)
        entrepreneurscore = "Entrepreneurial Score: " + str(entrepreneurscore);

        print innovationscore
        print entrepreneurscore

f = csv.writer(open('innovation-score-doc.csv', 'w'))
f.writerow(['Job_Title', 'Company', 'Job_Description', 'Innovation_Score', 'Entrepreneur_Score'])




    