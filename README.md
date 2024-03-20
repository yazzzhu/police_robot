## LINEBOT研究歷程

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










