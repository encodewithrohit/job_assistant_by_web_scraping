import requests
from bs4 import BeautifulSoup

known_skills = input("Provide familiar skillset separated by comma : ")
known_skills = known_skills.replace(" ", "").split(",")
print (f"Below are the jobs as per your known_skills {known_skills}")

def scrap_jobs() :
    
    #Reach the address of the html webpage & fetch the content
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Risk+Analyst%22&txtKeywords=%22Risk+Analyst%22&txtLocation=").text

    #Scrap the data to fetch the desired result
    soup = BeautifulSoup (html_text, 'lxml')

    total_jobs = soup.find_all ('li', class_='clearfix job-bx wht-shd-bx')

    for job in total_jobs :

        date_posted = job.find('span', class_='sim-posted').text.replace("  ", " ").strip()
        skills = job.find('span', class_='srp-skills').text.replace(" ", "").strip().split(",")
        
        if 'few' in date_posted and set(known_skills) & set(skills):
            
            company_name = job.find('h3', class_='joblist-comp-name').text.replace("  "," ").strip()
            apply_now = job.header.h2.a['href']
            print (f'''
Company name : {company_name}
Skills needed : {skills}
Apply here : {apply_now}
    ''')
            print("----------------")

if __name__ == "__main__" :
    scrap_jobs()