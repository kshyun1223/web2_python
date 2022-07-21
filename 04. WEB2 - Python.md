# 생활코딩 WEB2 - Python 수업 필기노트

### CGI
- Common Gateway Interface의 약자로 웹 서버에서 동적인 페이지를 보여 주기 위해 임의의 프로그램을 실행할 수 있도록 하는 기술

### 개발 환경 구축

- Bitnami WAMP 설치
  - WAMP: Windows Apache MySQL PHP의 약자
  - 정상 설치 확인: 웹브라우저에서 127.0.0.1 (혹은 자신의 localhost) 주소로 접속하면 Bitnami WAMP의 소개 페이지가 나온다

- Python 설치

- CGI 설정
  - 에디터에 Bitnami\wampstack 폴더 불러오기
  - `apache2\conf\original\httpd.conf` 파일을 연다
  - SRVROOT 설정
    - WAMP를 OS드라이브가 아닌 다른 저장소에 설치한 경우 SRVROOT 변수의 값을 아파치 웹서버의 설치 경로로 직접 설정해야 한다
    - 여기서 잘못된 경우 에러조차도 뜨지 않으며, 브라우저에 소스코드만 출력된다
    - 만약 이후의 단계를 먼저 진행했다면 여기서부터 새로 진행해야 한다
  - CGI 모듈 활성화: `LoadModule CGI_module modules/mod_CGI.so` 코드의 주석처리(#)를 해제하면 활성화 된다
  - 디렉토리 설정: DocumentRoot 설정에서 `<Directory>` 태그의 하위에 아래 태그를 추가한다
  
  ```python
  <Files "-.py">
  options ExecCGI
  AddHandler CGI-script .py
  </Files>
  ```
    
- 웹서버 재부팅: Bitnami WAMP의 Manager Tool 프로그램을 실행해서 아파치 웹서버 재부팅

- 에디터에 `Bitnami\wampstack\apache2\htdocs` 폴더 불러오기
  - htdocs: hypertext documents의 약자로 웹페이지가 저장된 장소를 의미한다

- htdoc 폴더에 간단한 페이지(파이썬 파일)를 작성해서 정상 출력 확인
  - 브라우저에서 127.0.0.1/파일명 주소로 접속
  - shebang: 스크립트를 해석할 인터프리터를 지정
  - 인터프리터와 헤더 정보를 지정하지 않으면 브라우저에 Internal Server Error가 출력된다
  - 에러 로그: 아파치 웹서버는 `apache2\logs\error.log` 파일에 에러 로그를 기록한다

### 데이터 타입

```python
#Number - Integer(정수)
print(1) #1

#String
print('Hello world') #Hello world

#string escape
print("Hell'o' \"w\"orld") #Hell'o' "w"orld

#줄바꿈
print('H\ne\nl\nl\no') 

#docstring
print('''
H
E
L
L
O
''')
```

- `print()`: 문자열을 출력하는 함수
  - string escape: 특정 기능이 있는 기호를 문자 그 자체로만 인식되게 하려면 역슬래시( \ ) 뒤에 입력
  - 줄바꿈: \n
  - dogstring: 코드 자체에서 줄바꿈을 하려면 문자열 앞뒤에 따옴표 세 개(''' ''')를 입력
  
### 변수

```python
#variable(변수)
a = 'Hello Pyhton' #값
print(a) #출력

#length
print(len(a)) #12

#index
print(a[0]) #H
print(a[1]) #e
print(a[2:5]) #llo 

#repeat
print((a+'\n')-2) #두번 반복
```

### 포맷팅

- positional formatting: 위치를 지정하고 순서대로 값을 넣는 방법

    ```python
    print('to {}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {} Duis aute irure dolor in {} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {} officia deserunt mollit anim id est laborum.'.format('egoing', 12, 'egoing', 'egoing'))
    ```

- named placeholder: 변수명을 지정하고 값을 넣는 방법

    ```python
    print('to {name}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim apple veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. {age:d} Duis aute irure dolor in {name} reprehenderit apple computer in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui {name} officia deserunt mollit anim id est laborum.'.format(name='egoing', age=12))
    ```

  - `{age:d}`에서 d는 digit의 약자로 숫자를 의미. 이에 따라 값으로는 반드시 숫자가 들어가야 한다. 

### 파이썬으로 html과 같은 페이지 구현

- `index.py` 파일 생성

    ```python
    #!Python #shebang(인터프리터 지정)
    print("Content-Type: text/html") #헤더 정보
    print() #헤더 다음은 한 줄 공백
    print('''html 코드 생략''') #dogstring
    ```
  - print 함수의 값으로 아무것도 넣지 않으면 한 줄 공백이 된다

### URL query string을 가져오는 방법
- URL query string: query parameters(물음표 뒤에 연결된 부분)을 url에 덧붙여서 추가적인 정보를 서버 측에 전달하는 것이다
  - 클라이언트가 어떤 특정 리소스에 접근하고 싶어하는지에 대한 정보를 담는다
- 아래 코드를 추가하고 목차를 클릭하면 주소가 `/index.py?id=값`과 같은 식으로 바뀌며, 제목 또한 id 값으로 바뀐다

``` python
#!python
print("Content-Type: text/html")
print()
import CGI #CGI 모듈을 호출
form = CGI.FieldStorage() #form 변수에 FieldStorage를 할당
pageId = form.getvalue("id") #pageId 값을 받으면 id 값을 넘겨준다 
print('''
<!doctype html>
  <html>
  <head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol> #목차에 id를 부여
      <li><a href="index.py?id=HTML">HTML</a></li> 
      <li><a href="index.py?id=CSS">CSS</a></li>
      <li><a href="index.py?id=JavaScript">JavaScript</a></li> 
    </ol>
    <h2>{title}</h2> #제목에 title 변수를 추가
    <p>본문 생략</p>
  </body>
  </html>
'''.format(title=pageId))  #title 변수를 pageId로 포맷팅
```


### Boolean

``` python
#Boolean
print(True) #참
print(False) #거짓

#Expression(표현식)
print(1+1) #2
print('Hello '+'world') #Hello world

#Comparison operator(비교연산자)
print(1==1) #True
print(1<2) #True
print(2<1) #False

#Membership operator: 문자열 내에서 특정 문자의 포함 여부 
print('world' in 'Hello world') #True
 
import os.path #os.path 모듈을 호출
print(os.path.exists('boolean2.py')) #파일의 존재 여부
```

### 조건문

```python
#input 함수: 사용자가 입력한 값을 변수에 저장
user_id = input('Please enter your ID') 
user_pwd = input('Please enter your Password')

#조건문
if user_pwd == '111111':
    print('Hello master')
else:
    print('Who are you?')

#중첩 조건문
if user_id == 'egoing':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
```

- input 함수에서 괄호 안의 내용은 사용자에게 출력할 메시지이다

### 실습 작품에 조건문 적용

- 기존 index.py 페이지에서 목차 링크는 id 값을 부여했으므로 정상 작동하지만, 제목 링크는 id 값을 부여하지 않았기 때문에 오류가 발생한다
- 아래 코드를 추가하면 목차를 클릭했을 때는 기존과 같이 동작하며, 메인을 클릭하면 주소는 `/index.py`가 되고, 제목은 Welcome이 된다

    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi
    form = cgi.FieldStorage()
    if 'id' in form: #form 변수 안에 id 값이 있는 경우
        pageId = form.getvalue("id") #pageId를 받으면 id 값을 넘겨준다 
    else: #form 변수 안에 id 값이 있지 않은 경우
        pageId = 'Welcome' #pageId를 받으면 'Welcome'을 넘겨준다
    print('''html 생략'''.format(title=pageId))
    ```

### 파일 제어 기능으로 본문 구현

- 기존 index.py 페이지에서는 목차를 클릭하면 제목은 변경되지만 내용은 그대로이다
- data 폴더를 만들고 그 안에 각 목차의 내용에 해당하는 파일을 생성한다
- 이후 아래 코드를 추가하면 목차를 클릭했을 때 제목과 함께 내용도 변경된다

    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi
    form = cgi.FieldStorage()
    if 'id' in form: #form 변수 안에 id 값이 있는 경우
        pageId = form.getvalue("id")
        description = open('data/'+pageId, 'r').read() #description을 받으면 data 폴더에서 pagaId에 해당하는 파일을 읽기모드로 넘겨준다
    else: #form 변수 안에 id 값이 있지 않은 경우
        pageId = 'Welcome'
        description = 'Hello, web' #description을 받으면 'Hello, web'을 넘겨준다 
    print('''<!doctype html>
    <html>
    <head>생략</head>
    <body> 
        <h1>생략</h1>
        <ol>생략</ol>
        <h2>{title}</h2>
        <p>{desc}</p> #본문에 desc 변수를 추가
    </body>
    </html>
    '''.format(title=pageId, desc=description)) #desc 변수를 description으로 포맷팅
    ```

### 리스트
```python
squars = [1, 'four', 9, 16, 25] #리스트를 생성하여 squars 변수의 값으로 입력
print(squars) #[1, 'four', 9, 16, 25]
print(squars[1]) #four
print(len(squars)) #5

s[1] = 4 #four → 4
print(squars) #[1, 4, 9, 16, 25]

del squars[2] #9 삭제
print(squars) #[1, 4, 16, 25]

squars.append('egoing') #'egoing' 추가
print(squars) #[1, 4, 16, 25, 'egoing']
```

### 반복문 for

```python
#list 
for value in ['a','b','c'] #value 변수에 a, b, c를 차례대로 대입한다
    print(value) #a b c

#range
for value in range(10) #value 변수에 0~10을 차례대로 대입한다
    print(value) #0 1 2 3 4 5 6 7 8 9 10
```

### 반복문을 이용해서 글목록 구현
- 기존 index.py 페이지에서는 내용 파일이 추가 혹은 삭제되어도 목차가 변경되지 않는다
- 아래 코드를 추가하면 내용 파일이 추가 혹은 삭제되면 자동으로 목차가 변경된다

    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi, os #os 모듈을 호출
    files = os.listdir('data') #리스트를 files 변수에 입력, 경로는 data 폴더
    listStr = '' #listStr 변수를 출력
    for item in files: #item 변수에 files 리스트를 차례대로 대입한다
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item) #listStr 변수는 기존 값에 item 변수를 더하면서 반복된다
    form = cgi.FieldStorage()
    생략
    print('''<!doctype html>
    <html>
    <head>생략</head>
    <body>
    <h1>생략</h1>
    <ol>
        {listStr} #목차에 listStr 변수를 추가
    </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
    </body>
    </html>
    '''.format(title=pageId, desc=description, listStr=listStr)) #listStr 변수를 listStr로 포맷팅
    ```

  - listStr 변수는 반복문에 의해 빈 목록에서 CSS 항목이 더해지고, 다시 거기에 HTML, JavaScript, Python 항목이 더해진다

### 글쓰기 기능: 입력

- `index.py` 파일 편집
    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi, os
    생략
    print('''<!doctype html>
    <html>
    <head>생략</head>
    <body>
    <h1>생략</h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a> #글쓰기 페이지 링크
    <h2>{title}</h2>
    <p>{desc}</p>
    </body>
    </html>
    '''.format(생략))
    ```

- `create.py` 파일 생성
    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi, os
    생략
    print('''<!doctype html>
    <html>
    <head>생략</head>
    <body>
    <h1>생략</h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p> #제목 입력 박스
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p> #내용 입력 박스
        <p><input type="submit"></p> #등록 버튼
    </form>
    </body>
    </html>
    '''.format(생략))
    ```
  - `<form>`: 사용자가 입력필드에 입력한 데이터 값을 서버로 전송해주는 태그
    - URL query string을 생성한다고 볼 수 있다
  - `name`: `<form>`에서 입력받은 값을 식별하기 위한 이름
  - `action`: `<form>`에서 입력받은 값을 전송할 경로
  - `method`: 사용자의 정보를 서버로 전송할 때는 get 방식이 아닌 post 방식을 사용해야 한다. method 속성의 값을 별도로 지정하지 않으면 기본값은 get이다. 


### 글쓰기 기능: 처리
- `process_create.py` 파일 생성
  ```python
  #!python
  import cgi
  form = cgi.FieldStorage()
  title = form['title'].value #title 변수의 값은 form 데이터 중에서 title이다
  description = form['description'].value #description 변수의 값은 form 데이터 중에서 description이다
  opened_file = open('data/'+title, 'w') #data 폴더에 파일을 쓰기모드로 생성하고 opened_file 변수에 입력

  opened_file.write(description) #description 데이터를 생성된 파일에 입력
  opened_file.close()

  print("Location: index.py?id="+title) #생성된 페이지로 이동(Redirection)
  print()
  ```

### 글쓰기 기능: 수정
- `index.py` 파일 편집
  ```python
  #!python
  print("Content-Type: text/html")
  print()
  import cgi, os
  files = os.listdir('data')
  생략
  form = cgi.FieldStorage()
  if 'id' in form: #form 변수 안에 id 값이 있는 경우
      pageId = form["id"].value
      description = open('data/'+pageId, 'r').read() #data 폴더에서 이름이 pageId 값인 파일을 읽기모드로 실행
      update_link = '<a href="update.py?id={}">update</a>'.format(pageId) #주소의 id값을 pageId로 포맷팅하고 링크를 출력한다
  else: #form 변수 안에 id 값이 있지 않은 경우
      pageId = 'Welcome'
      description = 'Hello, web'
      update_link = '' #링크를 출력하지 않는다
  print('''<!doctype html>
  <html>
  <head>생략</head>
  <body>
    <h1>생략</h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a>
    {update_link} #글 수정 페이지 링크
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
  </html>
  '''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link)) #update_link 변수를 update_link로 포맷팅
  ```

- `update.py` 파일 생성
  ```python
  #!python
  print("Content-Type: text/html")
  print()
  import cgi, os
  생략
  print('''<!doctype html>
  <html>
  <head>생략</head>
  <body>
    <h1>생략</h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
        <input type="hidden" name="pageId" value="{form_default_title}"> #pageId의 값으로 {form_default_title} 변수를 전송
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p> #제목 입력 박스에 기존 데이터를 포함해서 출력
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p> #내용 입력 박스에 기존 데이터를 포함해서 출력
        <p><input type="submit"></p>
    </form>
  </body>
  </html>
  '''.format(title=pageId, desc=description, listStr=listStr, form_default_title=pageId, form_default_description=description)) #form_default_title 변수를 pageId로 포맷팅, form_default_description 변수를 description로 포맷팅
  ```
  - 제목은 앞으로 변경될 수도 있기 때문에 여기서 변경하려고 하는 데이터의 식별자로 쓰이면 안 된다
    - 따라서 별도의 pageId 값을 전송한다
    - 이는 사용자가 수정해서는 안 되는 값이며, 또한 내부적인 정보일 뿐 사용자 경험과는 상관이 없기 때문에 숨김 처리한다

- `process_update.py` 생성
  ```python
  #!python
  import cgi, os
  form = cgi.FieldStorage()
  pageId = form["pageId"].value #pageId 변수의 값은 form 데이터 중에서 pageId이다
  title = form["title"].value
  description = form['description'].value
  
  opened_file = open('data/'+pageId, 'w')
  opened_file.write(description) description
  opened_file.close()
  
  os.rename('data/'+pageId, 'data/'+title) #기존에 pageId값이었던 파일명을 title 값으로 바꾼다
  
  print("Location: index.py?id="+title)
  print()
  ```

### 글쓰기 기능: 삭제
- index.py 파일 편집
  ```python
  #!python
  print("Content-Type: text/html")
  print()
  import cgi, os
  files = os.listdir('data')
  생략
  form = cgi.FieldStorage()
  if 'id' in form:
      pageId = form["id"].value
      description = open('data/'+pageId, 'r').read()
      update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
      delete_action = '''
          <form action="process_delete.py" method="post"> #`process_delete.py` 파일로 post 방식으로 이동
              <input type="hidden" name="pageId" value="{}"> #pageId의 값으로 변수를 전송
              <input type="submit" value="delete"> #submit 아이콘의 레이블을 delete로 지정
          </form>
      '''.format(pageId) #비어있는 중괄호를 pageId로 포맷팅
  else:
      pageId = 'Welcome'
      description = 'Hello, web'
      update_link = ''
      delete_action = '' # 아이콘을 출력하지 않는다
  print('''<!doctype html>
  <html>
  <head>생략</head>
  <body>
    <h1>생략</h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a>
    {update_link}
    {delete_action} #글 삭제 아이콘
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
  </html>
  '''.format(title=pageId, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action)) #delete_action 변수를 delete_action으로 포맷팅
  ```  

`process_delete.py` 파일 생성
  ```python
  #!python
  
  import cgi, os
  form = cgi.FieldStorage()
  pageId = form["pageId"].value
  
  os.remove('data/'+pageId) #data 폴더에서 이름이 pageId 값인 파일을 삭제

  print("Location: index.py") #메인으로 이동
  print()
  ```

### 함수
```python
def average(a,b,c): #average 함수를 생성
    s=a+b+c
    r=s/3
    print(r)
    return r

print(average(10,20,30)) #20
``` 
- def: 함수를 생성하는 명령어
- a, b, c: 변수
- s, r: 매개변수(parameter)
- 10, 20, 30: 인자(argument)
- 하나의 함수에는 가급적 하나의 기능만을 담는 것이 바람직하다
  - average 함수에는 평균값을 구하는 기능만 담고 return 처리하여, 출력이 필요하면 별도의 print 함수를 사용한다

### 글 목록 기능을 함수로 구현
- `index.py`, `create.py`, `update.py` 편집
  - getList 함수를 생성하고 기존 코드를 이동
    ```python
    def getList():
          files = os.listdir('data')
          listStr = ''
          for item in files:
              listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
          return listStr
    ```
  - `listStr` 변수를 `getList()`로 포맷팅

### 모듈
```python
#math 모듈 생성: math.py 파일을 생성하고 함수 작성
def average(a,b,c):
    s=a+b+c
    r=s/3
    return r
 
def plus(a,b):
    return a+b
 
pi = 3.14

#호출 방법 1
import math
print(math.average(1,2,3))
print(math.plus(1,2))
print(math.pi)

#호출 방법 2
from math import average, plus, pi
 
print(average(1,2,3))
print(plus(1,2))
print(pi)
```

### 리팩토링: 모듈로 함수 정리 정돈
- view 모듈 생성 
  ```python
  import os
  def getList():
      files = os.listdir('data')
      listStr = ''
      for item in files:
          listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
      return listStr
  ```

- `index.py`, `create.py`, `update.py` 편집
  - `getList` 함수를 삭제하고 `view` 모듈을 호출
  - `listStr` 변수를 `view.getList()`로 포맷팅

### XSS(Cross Site Scripting) 공격 방어
- `index.py` 파일 편집
    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi, os, view
    form = cgi.FieldStorage()
    if 'id' in form:
        pageId = 생략
        description = 생략
        description = description.replace('<', '&lt;') #본문에서 <를 &lt;로 변경한다
        description = description.replace('>', '&gt;') #본문에서 >를 &gt;로 변경한다
        update_link = 생략
        delete_action = 생략
    else: 생략
    print('''생략
    '''.format(생략))
    ```

  - 공격자가 게시물에 JavaScript 코드를 삽입하여 웹사이트에 비정상적인 동작을 일으키는 공격이다
  - 이를 방어하기 위해 HTML에서 태그를 입력하는 기호인 `<`와 `>`를 다른 문자로 변경하거나, `<script>` 태그를 삭제하는 등의 방법을 쓸 수 있다



### Pypi와 패키지 매니저(pip)
- Pypi(Python Package Index): 파이썬용 패키지들이 업로드되는 공식 저장소
- pip(Package Installer for Python): 파이썬의 패키지를 설치하고 관리하는 기능
- HTML Sanitizer: 웹사이트에 유해할 수 있는 HTML 코드의 목록이 등록되어 있으며, 이를 필터링하는 기능을 가진 패키지
  - pip는 기본적으로 파이썬에 포함하여 설치되어 있다
  - 콘솔창을 열고 `pip intall html_sanitizer` 명령어를 입력하면 패키지가 설치된다
  - `index.py` 파일 편집
    ```python
    #!python
    print("Content-Type: text/html")
    print()
    import cgi, os, view, html_sanitizer #HTML Sanitizer 모듈을 호출
    sanitizer = html_sanitizer.Sanitizer() #sanitizer 변수에 Sanitizer를 할당

    form = cgi.FieldStorage()
    if 'id' in form:
        title = 생략
        description = 생략
        title = sanitizer.sanitize(title) #제목을 sanitize 한다
        description = sanitizer.sanitize(description) #본문을 sanitize 한다
        update_link = 생략
        delete_action = 생략
    else: 생략
    print('''<!doctype html>
    <html>생략</html>
    '''.format(생략))
    ```

  - `view.py` 파일 편집
    ```python
    import os, html_sanitizer
    def getList():
        sanitizer = html_sanitizer.Sanitizer()
        files = os.listdir('data')
        listStr = ''
        for item in files:
            item = sanitizer.sanitize(item) #item 변수를 sanitize 한다
            listStr = 생략
        return listStr
    ```
