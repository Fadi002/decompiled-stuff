import time,requests,random
from instabot import Bot
from colorama import Fore
import webbrowser
red=Fore.RED
yellow=Fore.YELLOW
blue=Fore.BLUE
green=Fore.GREEN
cyan=Fore.CYAN
print('للمزيد من الادوات والثغرات اشترك ف البوت الخاص بنا على التليقرام @s8rat_bot')
webbrowser.open('https://t.me://s8rat_bot')
global x2,j
x2 = ' @s8rat_bot'
j = '''
[-] NEW USER:︎︎
'''
req=requests.session()
r=requests.session()
def insta_checker_without_list():
    count = 0
    user = ""
    length = int(4)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    while True:
        if count < 1000:
            count += 1
            for user in range(1):
                user = ""
                for item in range(length):
                    user += random.choice(chars)
            urlinsta = f'https://www.instagram.com/{user}'
            headerinsta = {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
            send = req.get(urlinsta, headers=headerinsta)
            if send.status_code == 404:
                print(green+f"[✅] Available: {user}")
                tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')                re = requests.post(tele)
                with open('Available.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user + '\n')
            else:
                print(red+f"[❌] Not Available: {user}")
            time.sleep(1)
        else:
            break
def insta_checker_with_list():
    sl = 'user.txt'
    file = open(sl, 'r')
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    while True:
        user = file.readline().split('\n')[0]
        urlinsta = f'https://www.instagram.com/{user}'
        headerinsta = {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
        send = req.get(urlinsta, headers=headerinsta)
        if send.status_code == 404:
            print(green+f"[✅] Available: {user}")
            tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')
            re = requests.post(tele)
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(red+f"[❌] Not Available: {user}")
        time.sleep(1)
def telegram_with_list():
    r = requests.session()
    sl = 'user.txt'
    ja = 1
    file = open(sl, 'r')
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    while True:
        user = file.readline().split('\n')[0]
        url = f"https://t.me/{user}"
        req = r.get(url)
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
            print(green+f"[{ja}] Available: {user}")
            tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            re = requests.post(tele)
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(red+f"[{ja}] Not Available: {user}")
            ja += 1
def telegram_without_list():
    count = 0
    user = ""
    length = int(5)
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    chars = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    try:
        while True:
            time.sleep(1.2)
            if count < 500:
                count += 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                url = f"https://t.me/{user}"
                send = req.get(url)
                if send.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                    print(green+f"[✅] Available: {user}")
                    tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')
                    re = requests.post(tele)
                    with open('Available.txt', 'a') as x:
                        tl = '[] NEW USER -->  '
                        x.write(tl + user + '\n')
                else:
                    print(red+f"[❌] Not Available: {user}")                time.sleep(0.9)
            else:
                break
    except:
        pass
def tik_checker_with_sess_with_list():
    try:
        sw = input("Enter session ID: ")
        if sw == "":
            print(f"[🆔] Please Enter your session id")
            while True:
                break
        else:
            sl = 'user.txt'
            file = open(sl, 'r')
            use_checkers = open('id_token.txt', "r").read().splitlines()
            ID = use_checkers[0]
            token = use_checkers[1]
            while True:
                user = file.readline().split('\n')[0]
                headers = {
                    'Host': 'www.tiktok.com',
                    'Cookie': f'sessionid={sw}',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'
                }
                response = requests.get(
                    f'https://www.tiktok.com/api/uniqueid/check/?unique_id={user}&aid=1233&app_name=tiktok_web&device_platform=web_mobile&region=SA&os=android&screen_width=360&screen_height=780&browser_language=ar-SA&browser_platform=Linux&browser_name=Mozilla&browser_version=5.0%20%28Linux%3B%20Android%2010%3B%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F90.0.4430.82%20Mobile%20Safari%2F537.36&browser_online=true&timezone_name=Asia%2FRiyadh&_signature=_02B4Z6wo00101kZaPigAAIDAAT3gcnLW59ZGWjqAAPFm46',
                    headers=headers)
                exp = (response.json()["status_msg"])
                vaild = (response.json()["is_valid"])
                if 'Login expired' in exp:
                    print(f"Error in session id the session id is expired")
                    exit()
                elif exp == "" or vaild == "True":
                    print(green + f"[✅] Available: {user}\t[{vaild}]")
                    tele = (
                        f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')                    re = requests.post(tele)
                    with open('Available.txt', 'a') as x:
                        tl = '[] NEW USER -->  '
                        x.write(tl + user + '\n')
                elif 'This username isn’t available. Try a suggested username, or enter a new one.' in exp or vaild == "False":
                    print(red + f"[❌] Not Available: {user}\t[{vaild}]")
                else:
                    print(f'Error {user}\t{vaild}')
                time.sleep(0.9)
    except:
        pass
def tik_checker_without_sess_with_list():
    req=requests.session()
    sl = 'user.txt'
    file = open(sl, 'r')
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    while True:
        user = file.readline().split('\n')[0]
        urltik = f'https://www.tiktok.com/@{user}?'
        headertik = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar',
                        'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
        send = req.get(urltik, headers=headertik)
        if send.status_code == 404:
            print(green+f"[✅] Available: {user}")
            tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')
            re = requests.post(tele)
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(red+f"[❌] Not Available: {user}")
        time.sleep(1)
def tik_checker_without_sess_without_list():
    count = 0
    req=requests.session()
    user = ""
    length = int(4)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    use_checkers = open('id_token.txt', "r").read().splitlines()
    ID = use_checkers[0]
    token = use_checkers[1]
    while True:
        time.sleep(0)
        if count < 1000:
            count += 1
            for user in range(1):
                user = ""
                for item in range(length):
                    user += random.choice(chars)
            urltik = f'https://www.tiktok.com/@{user}?'
            headertik = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar',
                        'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
            send = req.get(urltik, headers=headertik)
            if send.status_code == 404:
                print(green+f"[✅] Available: {user}")
                tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n 𝐮𝐬𝐞𝐫: {user}\n\n{x2}')                re = requests.post(tele)
                with open('Available.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user + '\n')
            else:
                print(red+f"[❌] Not Available: {user}")
                time.sleep(1)
        else:
            break
def tik_checker_with_sess_without_list():
    try:
        sw = input("Enter session ID: ")
        if sw == "":
            print(f"[🆔] Please Enter your session id")
            while True:
                break
        else:
            use_checkers = open('id_token.txt', "r").read().splitlines()
            ID = use_checkers[0]
            token = use_checkers[1]
            count = 0
            remaining = 1000
            user = ""
            length = int(4)
            chars = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
            while True:
                time.sleep(1.2)
                if count < 1000:
                    count += 1
                    remaining -= 1
                    for user in range(1):
                        user = ""
                        for item in range(length):
                            user += random.choice(chars)
                    headers = {
                        'Host': 'www.tiktok.com',
                        'Cookie': f'sessionid={sw}',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 10)'
                    }
                    response = requests.get(
                        f'https://www.tiktok.com/api/uniqueid/check/?unique_id={user}&aid=1233&app_name=tiktok_web&device_platform=web_mobile&region=SA&os=android&screen_width=360&screen_height=780&browser_language=ar-SA&browser_platform=Linux&browser_name=Mozilla&browser_version=5.0%20%28Linux%3B%20Android%2010%3B%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F90.0.4430.82%20Mobile%20Safari%2F537.36&browser_online=true&timezone_name=Asia%2FRiyadh&_signature=_02B4Z6wo00101kZaPigAAIDAAT3gcnLW59ZGWjqAAPFm46',
                        headers=headers)
                    exp = (response.json()["status_msg"])
                    vaild = (response.json()["is_valid"])
                    if 'Login expired' in exp:
                        print(f"Error in session id the session id is expired")
                        exit()
                    elif exp == "" or vaild == "True":
                        print(green+f"[✅] Available: {user}\t[{vaild}]")
                        tele = (
                            f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𝐮𝐬𝐞𝐫: {user}\n\n{x2}')
                        re = requests.post(tele)
                        with open('Available.txt', 'a') as x:
                            tl = '[] NEW USER -->  '
                            x.write(tl + user + '\n')
                    elif 'This username isn’t available. Try a suggested username, or enter a new one.' in exp or vaild == "False":
                        print(red+f"[❌] Not Available: {user}\t[{vaild}]")
                    else:
                        print(f'Error {user}\t{vaild}')
                    time.sleep(0.9)
                else:
                    break
    except:
        pass
def tik_comments():
    try:
        done = 0
        tx = input("Enter Your text: ")
        postid = input("Enter the post id: ")
        sessionid = input("Enter Your seesion id: ")
        url = f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2F&root_referer=https:%2F%2Fwww.tiktok.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FBahrain&priority_region=BH&verifyFp=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s&appId=1233&region=BH&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6944589237636646401&tt-web-region=BH&uid=6957894826579641349&aweme_id={postid}&text={tx}&device_id=6944589237636646401&_signature=_02B4Z6wo00101xegn7AAAIDAKCYplETPOLsXoJsAAKVx98"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'tt_webid_v2=6944589237636646401; tt_webid=6944589237636646401; s_v_web_id=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s; tt_csrf_token=dQmMg8Uekbw2Oq3qWeMzmZPV; csrf_session_id=53caf56337014635982064c815fd0b40; R6kq3TV7=APBQKTB5AQAARUF0d_OQ-94UVu51UTkJV6aMnxLDIekq-bfbknTR1okfl63_|1|0|27675acbbb7f3bf62040a83a6038ebc361ab9539; ak_bmsc=1C37B7EFB848AACA78C6A86D2E98F4472E2A548E28340000BD668F60218C611A~plMf9kvndtWdGMYA6ntojGLjZAnbo9JL/O3k0tlMDA/bnO2xhgSlQPPClh0dOgGSaun5sLRBrfmGZ2EZStGoGE8ZvuGNl7JDdOJ+vMkSPg8ONxn/pue9pK75OI1uenyR8+BSuBg0l/4nl8Gkz2mC4jTKnu2W8fm8vyijAPGEy9dHMGeHevdaKji8TeHmTmmz+qIM2AqFZBgMiLtpZqfNfN3vFoeaojuT1oOXdwCP/j6P4=; bm_sz=F2EFD804894550F3CA53C6456C64DB72~YAAQjlQqLhK1DiB5AQAA/1MpMAudG6Do3bfpbNxInp+UTsyWegkW8B64MgSviKu0pp5V6Fhluh66SzeqUvOsChOxFC+JDudD3O+1JSYqWBdunXgsvsM1RiFfvonoaen5R1R+Y0DbcTkKaCo/9sii4e9IYFF6icxq+NHilHnVzugyLNeBoXWWdMejkyg1M6bJ; _abck=D689B4F48527BC79C2A79217632F331E~0~YAAQjlQqLhO1DiB5AQAA/1MpMAVWkY7o8DGEfut8tpMTkcOrYGsuzI00y8cmKO/os7ywHsi5UeafSAqlHSEyTY8wbVoei6XMgYICIMnoZ8tCQe8nzK9j3h5K+aYRq+C7U7YFp0vToH1HZBDYtynCuZqOmKSoZ5CymLYStP97xIyliQ2+hOFddb2GUSlZ/p4lSupiCDj3XximHvlm7r746WAF3MBJC4JAqedluFI3UkebwX8A87Y3DDK4iAqVeDyKLjlKJ2scqw/5anKng648GEBMYJr2Sx1M8Ph6bct1qCSMXsm/lUlJMXn9YHxMXnM9tSCgovhpCSjHokc3o1DXebuNR+BWl4FDeZ3rdMMec+Mrf7UbHWapraXB7V1hRyI2dSIAlG86Mg6PFL79KgGmpQ8PQuD2q30t~-1~-1~-1; passport_csrf_token=45de29b0fdd44543ae03ebca1712aba9; passport_csrf_token_default=45de29b0fdd44543ae03ebca1712aba9; ttwid=1%7C76-Am_AM-jdvsHzB1lr6PLsnCSwMEQmDmftstnJM4c4%7C1620011314%7C98e8f2f8df0f69b0d8133eab649605fa3487dba3c89a7632aaeeddd6b8b0ed51; sid_guard={sessionid}%7C1620011343%7C5184000%7CFri%2C+02-Jul-2021+03%3A09%3A03+GMT; uid_tt=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; uid_tt_ss=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; store-idc=alisg; store-country-code=bh; cmpl_token=AgQQAPNZF-RMpbCxht16_B08-gG6LbPKf4PSYPhliQ; MONITOR_WEB_ID=6944589237636646401; odin_tt=a0e48820809040f306cc53f7c451b11dc8b0dcc1a0a154e9aa47bc3b460120ce2073a7979a3ba19fd724b00c8968968fd494a2299079c4607d3d3d5fdcbd1a12996f7fc7e82bc35ba3623247430e4e58; bm_sv=313B67CA31A48965C7AAD5944033B58E~Lso3XobClkO+2LgPELng8uvbHFQCpeycIWyhPae5NVMiuMlyoz2pWZbwQ6Z6gAO5arGhNfLqdCy0HQaYdIdEQanEAPwyfc0vmFH4fXTNkKg9xGR3OVK9Euo8BXuHIw3clCQpN6/kAXDBufMKkXmOhTF55BEqEYKxm+UDNHlZYAo=',
            'origin': 'https://www.tiktok.com',
            'referer': f'https://www.tiktok.com/@volleyboll_dear/video/{postid}?is_copy_url=1&is_from_webapp=v1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'tt-csrf-token': 'dQmMg8Uekbw2Oq3qWeMzmZPV',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        while True:
            time.sleep(6.6)
            req = requests.post(url, headers=headers)
            if "Comment sent successfully" in req.text:
                print("================================================================")
                print(f'DONE [{tx}]\nconut [{done}] \nsession id [{sessionid}]')
                print("================================================================")
                done += 1
                if done == 101:
                    break
            elif 'Login expired' in req.text:
                print(f'[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱\nsession id [{sessionid}]')
                break
            elif '{}' in req.text:
                print(f'[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱\nsession id [{sessionid}]')
                break
            else:
                print("================================================================")
                print(f'ERROR \nconut [{done}] \nsession id [{sessionid}]')
                print("================================================================")
    except:
        pass
def comments_insta():
    global tx,slp,go,headLG,datLG
    try:
        done=0
        b=Bot
        r = requests.session()
        user = input("User: ")
        pess = input("Password: ")
        tx = input("Your text: ")
        post = input("Post url: ")
        idd=b.get_media_id_from_link(self='',link=post)
        slp = int(7.1)
        urLG = "https://www.instagram.com/accounts/login/ajax/"
        headLG = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '272',
        'content-type': 'application/x-www-form-urlencoded',        'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '790551e77c76',
        'x-requested-with': 'XMLHttpRequest'}
        datLG = {
        "username": user,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
        "queryParams": "{}",
        "optIntoOneTap": "false"}
        go = r.post(urLG, headers=headLG, data=datLG)
        if ("userId") in go.text:
            print(green+f"""تم تسجيل دخول للحساب بنجاح [✅]""")
            sis = go.cookies['sessionid']
            urCOm = 'https://www.instagram.com/web/comments/{}/add/'.format(idd)
            hedCOM = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '44',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid=' + sis,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CMmx4KOpnx6/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
            'x-instagram-ajax': '753ce878cd6d',
            'x-requested-with': 'XMLHttpRequest'}
            daCOM = {
                'comment_text': tx,
                'replied_to_comment_id': ''}
            while True:
                time.sleep(slp)
                ct = r.post(urCOm, headers=hedCOM, data=daCOM)
                if '"status":"ok"' in ct.text:
                    print(green+f'[✅] DONE SEND COMMENT [{tx}]\nconut [{done}]')
                    done += 1
                    if done==101:
                        break
                elif 'Please' in ct.text:
                    print(red+'\n[‼️] ERROR SEND COMMENT - BAN ')
                elif ("two_factor") in go.text:
                    print(red+'\n[⛔️] Binary verification \n')
                    break
                elif ("checkpoint_url") in go.text:
                    print(yellow+'\n[⚠️] Account Secure \n')
                    break
                else:
                    print(blue+'\n[✖️] The username or password or post id is wrong! \n')
                    break
    except:
        pass
def reports_insta():
    try:
        filza445 = input("user: ")
        FLOZ20 = input("password: ")
        floz70 = input("Target: ")
        done = 0
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '296',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'x-csrftoken': 'MPicCBRW0thEKbRdX9DhiTL6UB0nGtqV',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp9zg7',
            'x-instagram-ajax': 'f65d2f981648',
            'x-requested-with': 'XMLHttpRequest'}
        data = {
            'username': f'{filza445}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{FLOZ20}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'}
        filza5448 = r.post(url, headers=headers, data=data)
        if '"authenticated":true' in filza5448.text:
            print(green+f"""تم تسجيل دخول للحساب بنجاح [✅]""")
            r.headers.update({'x-csrftoken': filza5448.cookies['csrftoken']})
            sl = int(4.5)
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(floz70)
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            ffilza2000 = user_id.split('_')[1]
            while True:
                url_spam = 'https://www.instagram.com/users/{}/report/'.format(ffilza2000)
                data_spam = {
                'source_name': '',
                'reason_id': 1,
                'frx_context': ''}
                solo = r.post(url_spam, data=data_spam)
                print(f'[✅] DONE SPAM USER [{floz70}]\nconut [{done}]')
                time.sleep(sl)
                done += 1
                if done == 101:
                    break
        elif ('checkpoint_required') in filza5448.text:
            print(yellow+f"""[⚠️] SECURE!!!""")
        elif ('"user":true,"authenticated":false') in filza5448.text:
            print(red+f"""[✖️] WRONG PASSWORD!!!""")
        elif filza5448.status_code == "429":
            print(red+f"""[⛔️] YOU HAVE BAN!""")
        elif ('"user":false') in filza5448.text:
            print(red+f"""[❗️] USERNAME WAS NOT FOUND!!!""")        else:
            print(red+"""[‼️] ERROR_CODE 404!""")
    except:
        pass
#############################
print(yellow+f"Free Tool Not for sell")
choose=int(input(f"""
{red}1) - insta Comments
2) - insta reports
3) - tiktok comments
{blue}
4) - Tiktok checkers
5) - TeleGram checker
6) - instagram checkers
7) - save the id and token for using checkers (only one Time u will do that)
\n--> """))
if choose==1:
    comments_insta()
elif choose==2:
    reports_insta()
elif choose==3:
    tik_comments()
elif choose==4:
    choose2=int(input(f"""
    {yellow}
    1) Tiktok checker with session id
    {cyan}
    2) Tiktok checker without session id
    """))
    if choose2==1:
        choose3=int(input(f"""
        {red}
        1) tiktok checker with list
        {blue}
        2) tiktok checker without list
        """))
        if choose3==1:
            tik_checker_with_sess_with_list()
        elif choose3==2:
            tik_checker_with_sess_without_list()
    elif choose2==2:
        choose4=int(input(f"""
        {red}
        1) tiktok checker with list
        {cyan}
        2) tiktok checker without list
        """))
        if choose4==1:
           tik_checker_without_sess_with_list()
        elif choose4==2:
            tik_checker_without_sess_without_list()
    else:
        exit("@s8rat_bot")
elif choose==5:
    choose6=int(input(f"""
    {yellow}
    1) telegram checker with list
    {blue}
    2) telegram checker without list
    """))
    if choose6==1:
        telegram_with_list()
    elif choose6==2:
        telegram_without_list()
    else:
        exit('@s8rat_bot')
elif choose==6:
    choose7=int(input(f"""
    {cyan}
    1) instagram checker with list
    {red}
    2) instagram checker without list
    """))
    if choose7==1:
        insta_checker_with_list()
    elif choose7==2:
        insta_checker_without_list()
    else:
        exit('@s8rat_bot')
elif choose==7:
    ID=input("ID ->: ")
    token=input("token ->: ")
    with open('id_token.txt', 'a') as x:
        x.write(ID + "\n" + token)
    print(f"ID: {ID}\nTOKEN: {token}")
elif choose==8:
    P="باعوص"
    exit(F"YOU ARE:\n{P}")
else:
    exit("@s8rat_bot")
