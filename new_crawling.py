import urllib.request as req # 원격 서버 url 자료 요청 
from bs4 import BeautifulSoup # source -> html 파싱 
import re

'''
url 쿼리를 이용한 새로운 titles 생성 코드입니다.
'''

#1.url 생성
base_url = "https://www.epeople.go.kr/nep/pttn/gnrlPttn/pttnSmlrCaseList.npaid"

#2. url read & decode to utf-8
res = req.urlopen(base_url+"?_csrf=1a8db2e5-e9c2-4d50-b7bc-d56fc8c19fb0&recordCountPerPage=20000&pageIndex=1&epUnionSn=&dutySctnNm=&lcgovBlngInstCd=&searchWordType=1&searchWord=&rqstStDt=2020-07-31&rqstEndDt=2021-07-31&dateType=0&pttnTypeNm=&searchInstType=locgovDiv&searchInstCd=6410000&focusPerPageYn=&frm_frmMenuMngNo=&frm_instCd=&frm_frmUrlSn=&frm_frmAllUrl=")
src = res.read()
data = src.decode('utf-8')

# #3. parsing & variable save
# html = BeautifulSoup(data, 'html.parser')

# a_tag = html.select('필요 코드 주소')

# 3. 정규식 표현으로 각 게시글의 고유 주소 넘버 추출(17000개 한번에!)
p = re.compile(r'\d\w\w-\d\d\d\d-\d\d\d\d\d\d\d-\d\w\w-\d\d\d\d-\d\d\d\d\d\d\d-\d\d\d\d\d\d\d-\d\d') 
#. = 하나의 문자 / ^ : 문자열의 시작
# $ (se$) : 문자열의 끝 -> case, base (o), face (x)
address = p.findall(data)

for i in address:
    try:
        res = req.urlopen(base_url+"?_csrf=c196acf4-7186-412f-8c94-2a2e95d0fd6a&recordCountPerPage=1&pageIndex=1&epUnionSn=%s&dutySctnNm=taol&lcgovBlngInstCd=&searchWordType=1&searchWord=&rqstStDt=2020-07-31&rqstEndDt=2021-07-31&dateType=0&pttnTypeNm=&searchInstType=locgovDiv&searchInstCd=6410000&focusPerPageYn=&frm_frmMenuMngNo=&frm_instCd=&frm_frmUrlSn=&frm_frmAllUrl="% i)
        src = res.read()
        data = src.decode('utf-8')
        html = BeautifulSoup(data, 'html.parser')
        tit_tag = html.select('') # 제목 추출
        con_tag = html.select('') # 내용 추출
        ans_tag = html.select('') # 답변 추출
    except:
        pass

titles = []
contents = []
answers = []

for i in tit_tag :
    tit = str(i.string)
    titles.append(tit.strip())
for i in con_tag :
    con = str(i.string)
    contents.append(con.strip())
for i in ans_tag :
    ans = str(i.string)
    contents.append(ans.strip())

    
#####################################################################################################################################

# 지은 - 미완성의 상태

import urllib.request as req  # 원격 서버 url 자료 요청 
from bs4 import BeautifulSoup # source -> html 파싱 
import re #regular expression
# url 쿼리를 이용한 새로운 titles 생성 코드입니다.

#1.url 생성
base_url = "https://www.epeople.go.kr/nep/pttn/gnrlPttn/pttnSmlrCaseList.npaid"

#2. url read & decode to utf-8
res = req.urlopen(base_url+"?_csrf=bb812c43-ff00-4476-82a3-ec86d61a85a0&recordCountPerPage=1&pageIndex=1&epUnionSn=&dutySctnNm=&lcgovBlngInstCd=&searchWordType=1&searchWord=&rqstStDt=2020-08-02&rqstEndDt=2021-08-02&dateType=0&pttnTypeNm=&searchInstType=locgovDiv&searchInstCd=6410000&focusPerPageYn=&frm_frmMenuMngNo=&frm_instCd=&frm_frmUrlSn=&frm_frmAllUrl=")
src = res.read()  
data = src.decode('utf-8')
html = BeautifulSoup(data, 'html.parser')


# 3. 정규식 표현으로 각 게시글의 고유 주소 넘버 추출(17000개 한번에!)[정규표현식] - 문자 포함식으로!
p = re.compile(r'\d\w\w-\d\d\d\d-\d\d\d\d\d\d\d-\d\w\w-\d\d\d\d-\d\d\d\d\d\d\d-\d\d\d\d\d\d\d-\d\d') 
#. = 하나의 문자 / ^ : 문자열의 시작
# $ (se$) : 문자열의 끝 -> case, base (o), face (x)
address = p.findall(data) 

add=address[2000:2120]

# for문 코드(css이용 - selenium주소에서 썼던 주소 활용중)
for i in add:
    titles = []
    title = html.select('#txt > div.same_mwWrap > div.samBox.mw > div > div.samC_top').text # tit_tag 제목이 출력이 되긴했습니다.긍데... 뭔가 틀렸어요..
    titles.append(title)
    
    print(title[i].get_text())


# 찬영님 올려주신 기본코드 (여기서 이래저래 조금씩 수정해보며 하고있어요)
for i in add:
    titles = []
        tit_tag = html.select('#txt > div.same_mwWrap > div.samBox.mw > div > div.samC_top') # 제목 추출

    for i in tit_tag :
        tit = str(i.string)
        titles.append(tit.strip())
    
titles        
        
        
'''
title 성공한다면 같은 방법으로 확장때 이용할 코드

    try:   
        #con_tag = html.select('div.samBox mw > div.sam_cont > div.samC_c')    # 내용 추출
        #ans_tag = html.select('div.samBox ans > div.sam_cont > div.samC_top') # 답변 추출
    except:
        pass

contents = []
answers = []

for i in tit_tag :
    tit = str(i.string)
    titles.append(tit.strip())
for i in con_tag :
    con = str(i.string)
    contents.append(con.strip())
for i in ans_tag :
    ans = str(i.string)
    contents.append(ans.strip())
'''




