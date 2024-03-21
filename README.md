## LINEBOT研究歷程

 - [建置LINE Developers/GitHub/Django專案](#建置LINE_Developers/GitHub/Django專案)
 - [資料庫遷移初始化及建立管理者帳號](#資料庫遷移初始化及建立管理者帳號)
 - [開發LINE Bot應用程式](#開發LINE_Bot應用程式，以views.py為預設主要判斷程式)
 - [Deploy a Django App on Render](#Deploy_a_Django_App_on_Render)
 - [Git 教學和 GitHub 設定指引](#Git教學和GitHub設定指引)

## 建置LINE Developers/GitHub/Django專案

#### **先到[LINE Developers](https://developers.line.biz/zh-hant/)**
1.	建立Provider
2.	建立Messaging API channel

Messaging API > LINE Official Account features > Auto-reply messages > `Edit`

回應功能 Webhooks：這個選項要記得打開(`Enabled`)

<img width="416" alt="Webhooks_Enabled" src="https://github.com/yazzzhu/police_robot/assets/80439162/ba8c394b-ceec-4e75-a71c-63ac262c874f">

<br>
<br>

#### **在 GitHub 建立專案**

`New repository` > 輸入專案名稱

<br>

#### **架設Django網站框架(於cmd)**

cd 到要建立專案的資料夾下

    #建立虛擬環境(進行套件安裝更改就不會影響本機原來的開發環境)
    pip install virtualenv
    virtualenv venv (虛擬環境名稱)
    .\venv\Scripts\activate
    #啟動虛擬環境(在Windows系統下)，正確啟動後前面會有(venv)
    #退出虛擬環境deactivate

安裝會用到的Python套件

    $pip install django line-bot-sdk requests gunicorn
    $pip install dj-database-url dj-static gunicorn psycopg2 django-simple-captcha
    (python下載3.10.~版本，python 12移除了distuilts)

另外要執行(建立套件清單)#我是建在專案外

    cd ..
    pip freeze > requirements.txt

#在要建立專案的資料夾下

    django-admin startproject BotProject(專案名稱)

啟動本地端伺服器

    cd BotProject(專案名稱)
    python manage.py runserver

出現`Starting development server at http://127.0.0.1:8000/` 複製 http://127.0.0.1:8000/ 這段於瀏覽器開啟

(ctrl+c退出運行模式)

※如若出現紅字

<img width="408" alt="red_error" src="https://github.com/yazzzhu/police_robot/assets/80439162/78abe654-e603-4c06-a4c4-4665f180c20d">

`python manage.py migrate` 後再執行就行

<br>

#### **建立Django APP**

    cd 到建立專案的資料夾下
    python manage.py startapp BotApp(APP名稱)

新增兩個資料夾
(static主要用於靜態資料如圖片、圖示、其他媒體檔案等等)
(templates則是用於放模版，也就是寫好的html的網頁)

    md templates
    md static

更改settings.py
(把LINE的Channel Access Token跟Channel Secret新增到Secret_Key之前)

    # SECURITY WARNING: keep the secret key used in production secret!
    LINE_CHANNEL_ACCESS_TOKEN = '你的LINE Channel Access Token(於Basic settings)'
    LINE_CHANNEL_SECRET = '你的LINE Channel Secret(於Messaging API)'
    SECRET_KEY = 'Django專案的Secret Key'#此處不需更改

若此處設定為False，則網頁出現Bug的時候，會呈現HTTP 404的Status Code

    DEBUG = True
    
    ALLOWED_HOSTS = ['*']

在INSTALLED_APPS內新增剛剛建立的APP名稱

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'APP名稱', #新增APP名稱('botapp.apps.BotappConfig',)
    ]

在TEMPLATES中新增，templates的資料夾路徑

    'DIRS': [os.path.join(BASE_DIR,'templates')], #新增templates資料夾路徑

語系、時區的設定

    LANGUAGE_CODE = 'zh-hant'
    
    TIME_ZONE = 'Asia/Taipei'

新增static路徑

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATICILES_DIRS = [
        os.path.join(BASE_DIR,'static') #加入static路徑
    ]

在RobotApp應用程式資料夾下，新增urls.py

    from django.urls import path
    from . import views  #引用這個資料夾中的views檔案
    urlpatterns = [
        path('', views.index, name = "Index")
    ]

更改botproject下的urls.py

    from django.contrib import admin
    from django.urls import path, include  # 引用include函式
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('posts/', include('botapp.urls')) #新增應用程式的網址
    ]

新增Procfile(無副檔名)

    web: gunicorn --pythonpath BotProject BotProject.wsgi

開啟views.py來撰寫對應的檢視函式(View Function)

    from django.shortcuts import render
    from django.http.response import HttpResponse
    # Create your views here.
    def index(request):
        return HttpResponse("My First Django App.") 

<br>

    python manage.py runserver

開啟http://127.0.0.1:8000/posts/

<img width="313" alt="My_First_Django_App" src="https://github.com/yazzzhu/police_robot/assets/80439162/2addcc1e-152a-46fc-a0f1-aa918eda9790">

#測試Django App開發

<br>

## 資料庫遷移初始化及建立管理者帳號

**Django Migration(資料遷移) 資料庫遷移的初始化**

    python manage.py makemigrations
    python manage.py migrate

**建立一個管理者帳號**

    python manage.py createsuperuser

<br>

## 開發LINE_Bot應用程式，以views.py為預設主要判斷程式

編輯app應用程式資料夾下的views.py檔案

    from django.shortcuts import render
    
    # Create your views here.
    from django.conf import settings
    from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
    from django.views.decorators.csrf import csrf_exempt
    
    from linebot import LineBotApi, WebhookParser
    from linebot.exceptions import InvalidSignatureError, LineBotApiError
    from linebot.models import MessageEvent, TextSendMessage
    
    line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
    parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
    
    @csrf_exempt
    def callback(request):
        if request.method == 'POST':
            signature = request.META['HTTP_X_LINE_SIGNATURE']
            body = request.body.decode('utf-8')
    
            try:
                events = parser.parse(body, signature)
            except InvalidSignatureError:
                return HttpResponseForbidden()
            except LineBotApiError:
                return HttpResponseBadRequest()
    
            for event in events:
                if isinstance(event, MessageEvent):
                    mtext=event.message.text
                    message=[]
                    message.append(TextSendMessage(text=mtext))
                    line_bot_api.reply_message(event.reply_token,message)
    
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

※要注意專案名稱不要命名為linebot，不然這段程式會出bug

<br>

更改botproject下的urls.py

    from django.contrib import admin
    from django.urls import path, include  # 引用include函式
    from BotApp import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('posts/', include('BotApp.urls')), #新增應用程式的網址
        path('callback', views.callback),
    ]

**將檔案上傳至github上面**

[(下載git詳見「Git 教學和 GitHub 設定指引」)](#Git教學和GitHub設定指引)

<br>

## Deploy_a_Django_App_on_Render

註冊Render帳號

(我是用github帳號登入)

`Web Service` → `New Web Service`（或是在右上角 `New` + 然後選 `Web Service`）

登入你的 GitHub 做連結，就會出現下面的畫面，再來選你在 GitHub 的 Line Bot 專案名稱

<img width="416" alt="Render" src="https://github.com/yazzzhu/police_robot/assets/80439162/bb6ef3d8-420c-4963-9b0b-ed583c9c22f8">

`Connect` 按下去後開始填資料

<br>

Build command填: `./build.sh` (相對位址才會找到檔案)

要在存儲庫的主目錄中新增檔案(記得上傳github)

build.sh

    #!/usr/bin/env bash
    # exit on error # 出錯時退出
    set -o errexit
    
    pip install --upgrade pip
    pip install -r requirements.txt

Start Command要輸入命令來啟動 Django 應用程式: `gunicorn --pythonpath BotProject BotProject.wsgi` (BotProject專案名)

<br>

`Advanced` / `Environment`

Key : PYTHON_VERSION

Value : 3.10.11

<br>

`Create Web Service` 按下去後，就會自動跑到這個畫面了，它就開始佈署你的 Line Bot

`Your service is live 🎉` 就是部屬成功

<br>

複製左上角連結

再到`LINE Developers` / `Messaging API`

Edit Webhook URL : `https:~(複製的連結)/callback`

按下 `Verify` 顯示Success就連接成功

(Use webhook要開啟)

<br>

**Line成功畫面(重覆用戶文字訊息的回聲機器人)**

<img width="277" alt="line" src="https://github.com/yazzzhu/police_robot/assets/80439162/8a05e20d-021d-4980-951f-566de8704452">

※render免費限制

每月 750 小時

有連續 15 分鐘未使用會進入休眠，休眠後的甦醒時間約是 30 秒。

## **Git教學和GitHub設定指引**

安裝Git for Windows ([https://gitforwindows.org/](https://gitforwindows.org/))

修改預設編輯器為vscode

其餘步驟都預設下一步就行

<br>

到Git Bish或vscode的Git Bish

    git --version #確認版本

設定使用者(若已有 GitHub 帳號，建議和 GitHub 使用相同的)

    git config --global user.name "<Your Name>"
    git config --global user.email "<your@gmail.com>"

    git config --list   #檢視 git 設定

<br>

**(上傳github流程)**

    cd 到建立專案的資料夾下
    git init #初始化Git Repository(建立.git之隱藏檔案)
    git status #觀察Repository檔案追蹤狀況
    git add '檔名' #將檔案加入追蹤清單，如: git add .(add全)
    
再一次 `git status` 就會列出新增清單

    git commit -m "此處填版本訊息" #建一組版本更新訊息
    
再一次 `git status` 可以發現訊息已經被清空，後續可以在github上看到

    git push origin master

<br>

**連接到遠端**

    git remote add origin(遠端空間名稱) https:~(遠端地址)

* 有error: remote origin already exists. #已存在之錯誤:
    * 先刪除 git remote rm origin
    * 後增加 git remote add origin git@github.com:~.git

<br>

    git remote -v #查詢遠端的repository
    git branch -M main

`(有error: failed to push some refs to '~.git'錯誤: git pull --rebase origin master)`

    git push (-u) origin(遠端空間名稱) master(遠端空間的分支名稱)
    [Hint] "-u"會把預設的remote設成origin, 未來push若不指定remote,則都會推到origin

登入授權就連接成功

    git push(先前設定origin為預設，連接之後可以直接push)



