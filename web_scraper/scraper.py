import requests
from bs4 import BeautifulSoup
from requests.models import Response

URL= "https://en.wikipedia.org/wiki/History_of_Mexico"



def  get_citations_needed_count(URL):

    response=requests.get(URL)
    soup = BeautifulSoup(response.text,'html.parser')
    result=soup.find_all('sup',class_='noprint Inline-Template Template-Fact')
    return len(result)


print(get_citations_needed_count(URL))

def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find(class_="mw-parser-output")
    all_results = results.findAll('p')
    arr=[]
    for i in all_results:
        citation_needed=i.findAll('a',title='Wikipedia:Citation needed')
        for j in citation_needed:
            arr.append(i.text) 
    return "\n""\n".join(arr)



print(get_citations_needed_report(URL))
    