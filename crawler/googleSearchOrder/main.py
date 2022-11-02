import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    query = "皇冠體育"
    addres = "https://www.bjhenghaokeji"
    response = requests.get("https://www.google.com/search?q="+query+"&client=safari&rls=en&sxsrf=ALiCzsbFSAuM1_o0zQkOuvc8id36He6VcQ%3A1667315953276&ei=8ThhY8CyEKK12roPyY-IqAk&ved=0ahUKEwiA7_34o437AhWimlYBHckHApUQ4dUDCA8&uact=5&oq=%E7%9A%87%E5%86%A0%E9%AB%94%E8%82%B2&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwA0oECEEYAEoECEYYAFAAWABg-AJoAXABeACAAQCIAQCSAQCYAQDIAQrAAQE&sclient=gws-wiz-serp")
    soup = BeautifulSoup(response.text, "html.parser")
    beforeComsList = []
    for div in soup.find_all('div'):
        a = div.find_all_next('a')
        link = a[0]['href']
        urlArr = link.split("/url?q=")
        if len(urlArr) > 1:
            beforeComs = str(urlArr[1]).split(".com")[0]
            beforeComsList.append(beforeComs)

    urlList = []
    for beforeCom in beforeComsList:
        if beforeCom in urlList:
            continue
        else:
            urlList.append(beforeCom)

    print(urlList)
    j = 0
    for i in urlList:
        j += 1
        if i == addres:
            print("第幾個呢？ ", j)
