import requests
from time import sleep
from lxml import etree
import re
response = requests.get('http://quote.eastmoney.com/usstocklist.html' )
# print(response.text)
response.encoding = 'gb2312'
html = etree.HTML(response.text)
html_data = html.xpath('/html/body/div[9]/div[2]/div/ul')
pattern_name =re.compile(r'^[\u4E00-\u9FA5A-Za-z0-9_]+')
pattern_code =re.compile(r'\([A-Za-z]+')
codelist=[]
namelist=[]
for i in range (len(html_data[0])):
    symbol = pattern_code.findall(html_data[0][i][0].text)
    name = pattern_name.findall(html_data[0][i][0].text)
    try:
        if (symbol[0] not in codelist):
            codelist.append(symbol[0])
    except:
        pass
print(len(codelist))

