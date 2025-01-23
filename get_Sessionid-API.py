try:
    import string , random , re,base64 , os
    from uuid import uuid4
    from requests import Session
    from colorama import Fore , Style
    from time import time
except Exception as e:
    print(e)
    input()
    os._exit(0)
def set_cmd_window_size(width, height):
    os.system(f'mode con: cols={width} lines={height}')
set_cmd_window_size(140, 25)
Purple="\033[1;35m"
def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    return fr"""                                                                                     
{Fore.BLUE}
  .--.--.                                                                                      
 /  /    '.                                    ,--,                         ,--,         ,---, 
|  :  /`. /                                  ,--.'|    ,---.        ,---, ,--.'|       ,---.'| 
;  |  |--`              .--.--.    .--.--.   |  |,    '   ,'\   ,-+-. /  ||  |,        |   | : 
|  :  ;_       ,---.   /  /    '  /  /    '  `--'_   /   /   | ,--.'|'   |`--'_        |   | | 
 \  \    `.   /     \ |  :  /`./ |  :  /`./  ,' ,'| .   ; ,. :|   |  ,"' |,' ,'|     ,--.__| | 
  `----.   \ /    /  ||  :  ;_   |  :  ;_    '  | | '   | |: :|   | /  | |'  | |    /   ,'   | 
  __ \  \  |.    ' / | \  \    `. \  \    `. |  | : '   | .; :|   | |  | ||  | :   .   '  /  | 
 /  /`--'  /'   ;   /|  `----.   \ `----.   \'  : |_|   :    ||   | |  |/ '  : |__ '   ; |:  | 
'--'.     / '   |  / | /  /`--'  //  /`--'  /|  | '.'\   \  / |   | |--'  |  | '.'||   | '/  ' 
  `--'---'  |   :    |'--'.     /'--'.     / ;  :    ;`----'  |   |/      ;  :    ;|   :    :| 
             \   \  /   `--'---'   `--'---'  |  ,   /         '---'       |  ,   /  \   \  /   
              `----'                          ---`-'                       ---`-'    `----'    
                    By Joker @vv1ck | @221298
"""
class IG_LOGIN:
    def __init__(self):
        self.QTR = Session()
        self.tim = time()
        print(LOGO())
        self.info_Device()
        self.login()
    
    def info_Device(self):
        self.UID = str(uuid4())
        self.waterfall_id = self.UID[:8] + "should_trigger_override_login_success_action" + self.UID[8:]
        self.android = f"android-{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}"
        self.user_agent = f"Instagram 303.0.0.0.59 Android (28/9; 320dpi; 900x1600; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
        self.Pigeon_SessionId = f"UFS-{self.UID}-0"

    def Check_code(self):
        while True:
            headers = {
                "Host": "i.instagram.com",
                "X-Ig-App-Locale": "en_US",
                "X-Ig-Device-Locale": "en_US",
                "X-Ig-Mapped-Locale": "en_US",
                "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
                "X-Pigeon-Rawclienttime": str(time()),
                "X-Ig-Bandwidth-Speed-Kbps": "5162.000",
                "X-Ig-Bandwidth-Totalbytes-B": "0",
                "X-Ig-Bandwidth-Totaltime-Ms": "0",
                "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
                "X-Ig-Www-Claim": "0",
                "X-Bloks-Is-Layout-Rtl": "false",
                "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
                "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
                "X-Ig-Android-Id": "android-279938d90eae62a5",  
                "X-Ig-Timezone-Offset": "28800",
                "X-Ig-Nav-Chain": f"bloks_unknown_class:select_verification_method:1:button:{str(time())}::,bloks_unknown_class:select_verification_method:2:button:{str(time())}::,bloks_unknown_class:verify_email_code:3:button:{str(time())}::,bloks_unknown_class:select_verification_method:4:button:{str(time())}::,bloks_unknown_class:verify_email_code:5:button:{str(time())}::,bloks_unknown_class:select_verification_method:6:button:{str(time())}::,bloks_unknown_class:verify_email_code:7:button:{str(time())}::,bloks_unknown_class:select_verification_method:8:button:{str(time())}::,bloks_unknown_class:select_verification_method:9:button:{str(time())}::,bloks_unknown_class:verify_email_code:10:button:{str(time())}::",
                "X-Fb-Connection-Type": "WIFI",
                "X-Ig-Connection-Type": "WIFI",
                "X-Ig-Capabilities": "3brTv10=",
                "X-Ig-App-Id": "567067343352427",
                "Priority": "u=3",
                "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
                "Accept-Language": "en-US",
                "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
                "Ig-Intended-User-Id": "0",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Content-Length": "942",
                "Accept-Encoding": "gzip, deflate",
                "X-Fb-Http-Engine": "Liger",
                "X-Fb-Client-Ip": "True",
                "X-Fb-Server-Cluster": "True"}
            code = input('[+] Enter Code : ')
            data=f'security_code={code}&perf_logging_id=2294257&has_follow_up_screens=0&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&challenge_context={self._context}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
            chk = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=headers,data=data)
            if ('Instagram User' in chk.text):
                input('[-] Ban Account !')
                os._exit(0)
            if ("Bearer" in chk.text):
                sessionids = re.search(r'Bearer IGT:2:(.*?),',chk.text).group(1).strip()
                try:
                    session = sessionids[:-8]
                    graps=base64.b64decode(session).decode('utf-8')
                    if "sessionid"  in graps:sessionid = re.search(r'"sessionid":"(.*?)"}',graps).group(1).strip()
                except Exception as JOK:
                    sessionid = sessionid
                try:
                    sessionid2 = re.sub(r'\\+', '', sessionids).split('"')[0]
                except Exception as JOK:
                    sessionid2 = sessionids
                print(f'[+] Sessionid API 1 : {sessionid}')
                print(f'[+] Sessionid API 2 : {sessionid2}')
                with open('sessionids.txt', 'w') as f:
                    f.write(f'Sessionid API 1 : {sessionid}\nSessionid API 2 : {sessionid2}\n')
                input('[+] Sessionid saved in sessionids.txt , Press Enter to continue')
                os._exit(0)
            elif ('Please check the code we sent you and try again.' in chk.text):
                print('[-] Wrong Code ! Try again')
            else:
                print(chk.text)
    
    def replay_challenge(self):
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": str(time()),
            "X-Ig-Bandwidth-Speed-Kbps": "5162.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": f"bloks_unknown_class:select_verification_method:1:button:{str(time())}::,bloks_unknown_class:select_verification_method:2:button:{str(time())}::,bloks_unknown_class:verify_email_code:3:button:{str(time())}::,bloks_unknown_class:select_verification_method:4:button:{str(time())}::,bloks_unknown_class:verify_email_code:5:button:{str(time())}::,bloks_unknown_class:select_verification_method:6:button:{str(time())}::,bloks_unknown_class:verify_email_code:7:button:{str(time())}::,bloks_unknown_class:select_verification_method:8:button:{str(time())}::,bloks_unknown_class:select_verification_method:9:button:{str(time())}::,bloks_unknown_class:verify_email_code:10:button:{str(time())}::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "879",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        data = f'choice={self.choice}&bk_client_context=%7B%22bloks_version%22%3A%228ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb%22%2C%22styles_id%22%3A%22instagram%22%7D&challenge_context={self._context}&bloks_versioning_id=8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb'
        ryplay = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.replay_challenge/',headers=headers, data=data)
        print(ryplay.text)
    
    def take_challenge(self):
        while True:
            self.choice = input('[+] choice : ')
            if self.choice in ['1', '2']:break
            else:print('Error !')
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": "1737201349.381",
            "X-Ig-Bandwidth-Speed-Kbps": "5162.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": f"bloks_unknown_class:select_verification_method:1:button:{str(time())}::,bloks_unknown_class:select_verification_method:2:button:{str(time())}::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "899",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        data=f'user_id={self.user_id}&cni={self.cni}&nonce_code={self.nonce_code}&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&fb_family_device_id=9017b6ad-d8d5-4711-b0fb-422b0e6c3784&challenge_context={self.challenge_context}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a&get_challenge=true'
        take = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=headers, data=data)
        if ('challenge_context' in take.text):
            splt = take.text.split('has_follow_up_screens')[1]
            _contexts=splt.replace('\\', '')
            try:
                self._context = _contexts.split('"False", "')[1].split('"')[0]
            except IndexError:
                self._context = _contexts.split('), "')[1].split('"')[0]
            data=f'choice={self.choice}&has_follow_up_screens=0&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&challenge_context={self._context}&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
            sent_code = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/',headers=headers,data=data)
            if ('Get a new code' in sent_code.text):
                print('Done sent code')
                splt2 = sent_code.text.split('has_follow_up_screens')[1]
                _contexts2=splt2.replace('\\', '')
                try:
                    self._context = _contexts2.split('"False", "')[1].split('"')[0]
                except IndexError:
                    self._context = _contexts2.split('), "')[1].split('"')[0]
                self.Check_code()
            else:
                if ('This field is required' in sent_code.text):
                    code = input('[+] A code was previously sent. Do you want to send a new code or use the old one? (1: new code, 2: old code) ')
                    if code == '1':
                        self.replay_challenge()
                    elif code == '2':
                        self.Check_code()
                    else:pass
                else:
                    print('=============== 2 ===============')
                    print(sent_code.text)
                    print('=============== 2 ===============')
        else:
            print('=============== 1 ===============')
            print(take.text)
            print(take.status_code)
    
    def challenge_required(self):
        self.headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": str(time()),
            "X-Ig-Bandwidth-Speed-Kbps": "5162.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": f"bloks_unknown_class:select_verification_method:1:button:{str(time())}::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-Intended-User-Id": "0",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        joker=self.QTR.get(f'https://i.instagram.com/api/v1/challenge{self.APIS}?guid=f7a78e22-d663-48de-bee6-e56388b68cd3&device_id=android-279938d90eae62a5&challenge_context={self._context}',headers=self.headers)
        if ('step_data' in joker.text):
            step_data = joker.json()["step_data"]
            self.user_id = joker.json()['user_id']
            self.challenge_context = joker.json()['challenge_context']
            self.nonce_code = joker.json()['nonce_code']
            self.cni = joker.json()['cni']
            print('--------------------')
            if "phone_number" in step_data:
                try:
                    phone = step_data["phone_number"]
                    email = step_data["email"]
                    print(f' [0] phone_number : {phone}')
                    print(f' [1] email : {email}')
                    self.take_challenge()
                except Exception as e:
                    try:
                        phone = step_data["phone_number"]
                        print(f' [0] phone_number : {phone}')
                        self.take_challenge()
                    except Exception as e:print(e)
            elif "email" in step_data:
                try:
                    phone = step_data["phone_number"]
                    email = step_data["email"]
                    print(f' [0] phone_number : {phone}')
                    print(f' [1] email : {email}')
                    self.take_challenge()
                except Exception as e:
                    try:
                        email = step_data["email"]
                        print(f' [1] email : {email}')
                        self.take_challenge()
                    except Exception as e:print(e)
            elif 'contact_point' in joker.text:
                try:
                    choice = step_data["choice"]
                    email = step_data["contact_point"]
                    print(f' [{str(choice)}] contact_point : {email}')
                    self.take_challenge()
                except Exception as e:
                    print(e)
            else:
                print(joker.text)
        else:
            print(joker.text)
    

    def two_step_verification(self):
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-3cd49367-63a9-48c4-b050-4a090a765b67-0",
            "X-Pigeon-Rawclienttime": str(self.tim),
            "X-Ig-Bandwidth-Speed-Kbps": "-1.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "2510",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        data ='params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22'+self.android+'%22%2C%22is_whatsapp_installed%22%3A0%2C%22machine_id%22%3A%22Z2lDXwABAAEgXxQ8xlfS3n2GPdc5%22%7D%2C%22server_params%22%3A%7B%22family_device_id%22%3A%22'+self.UID+'%22%2C%22device_id%22%3A%22'+self.android+'%22%2C%22two_step_verification_context%22%3A%22'+self.two_step_verification_context+'%22%2C%22flow_source%22%3A%22two_factor_login%22%2C%22INTERNAL_INFRA_screen_id%22%3A%22j8i4vo%3A3%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a'
        check = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.two_step_verification.entrypoint/',headers=headers,data=data)
        if ('Waiting for approval, Approve from the other device to continue' in check.text):
            input('Waiting for approval, Approve from the other device to continue')
            while True:
                login = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.two_step_verification.has_been_allowed.async/',headers=headers,data='params=%7B%22client_input_params%22%3A%7B%22auth_secure_device_id%22%3A%22%22%2C%22machine_id%22%3A%22Z2lDXwABAAEgXxQ8xlfS3n2GPdc5%22%2C%22family_device_id%22%3A%22'+self.UID+'%22%2C%22device_id%22%3A%22'+self.android+'%22%7D%2C%22server_params%22%3A%7B%22machine_id%22%3Anull%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22INTERNAL__latency_qpl_instance_id%22%3A1.17961624300087E14%2C%22device_id%22%3A%22'+self.android+'%22%2C%22two_step_verification_context%22%3A%22'+self.two_step_verification_context+'%22%2C%22flow_source%22%3A%22two_factor_login%22%7D%7D&bk_client_context=%7B%22bloks_version%22%3A%229fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a')
                if "Bearer" in login.text:
                    sessionids = re.search(r'Bearer IGT:2:(.*?),',login.text).group(1).strip()
                    try:
                        session = sessionids[:-8]
                        graps=base64.b64decode(session).decode('utf-8')
                        if "sessionid"  in graps:sessionid = re.search(r'"sessionid":"(.*?)"}',graps).group(1).strip()
                    except Exception as JOK:
                        sessionid = sessionid
                    try:
                        sessionid2 = re.sub(r'\\+', '', sessionids).split('"')[0]
                    except Exception as JOK:
                        sessionid2 = sessionids
                    print(f'[+] Sessionid API 1 : {sessionid}')
                    print(f'[+] Sessionid API 2 : {sessionid2}')
                    with open('sessionids.txt', 'w') as f:
                        f.write(f'Sessionid API 1 : {sessionid}\nSessionid API 2 : {sessionid2}\n')
                    input('[+] Sessionid saved in sessionids.txt , Press Enter to continue')
                    break
                else:
                    input('[-] You have not been approved. Please approve your device by logging into your account and clicking on Accept Login, then click here Enter.')
        else:
            print(check.text)
            print(check.status_code)

    def login(self):
        self.username = input('[+] Enter Username : ')
        self.password = input('[+] Enter Password : ')
        data = {"params": "{\"client_input_params\":{\"contact_point\":\"" + self.username + "\",\"password\":\"#PWD_INSTAGRAM:0:0:" +  self.password + "\",\"fb_ig_device_id\":[],\"event_flow\":\"login_manual\",\"openid_tokens\":{},\"machine_id\":\"Z2lDXwABAAEgXxQ8xlfS3n2GPdc5\",\"family_device_id\":\"\",\"accounts_list\":[],\"try_num\":1,\"login_attempt_count\":1,\"device_id\":\"" + self.android + "\",\"auth_secure_device_id\":\"\",\"device_emails\":[],\"secure_family_device_id\":\"\",\"event_step\":\"home_page\"},\"server_params\":{\"is_platform_login\":0,\"qe_device_id\":\"\",\"family_device_id\":\"\",\"credential_type\":\"password\",\"waterfall_id\":\"" + self.waterfall_id + "\",\"username_text_input_id\":\"9cze54:46\",\"password_text_input_id\":\"9cze54:47\",\"offline_experiment_group\":\"caa_launch_ig4a_combined_60_percent\",\"INTERNAL__latency_qpl_instance_id\":56600226400306,\"INTERNAL_INFRA_THEME\":\"default\",\"device_id\":\"" + self.android + "\",\"server_login_source\":\"login\",\"login_source\":\"Login\",\"should_trigger_override_login_success_action\":0,\"ar_event_source\":\"login_home_page\",\"INTERNAL__latency_qpl_marker_id\":36707139}}"}
        data["params"] = data["params"].replace("\"family_device_id\":\"\"", "\"family_device_id\":\"" +self.UID + "\"")
        data["params"] = data["params"].replace("\"qe_device_id\":\"\"", "\"qe_device_id\":\"" + self.UID + "\"")
        print('[+] Attempting to log in ..')
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": "1737200882.960",
            "X-Ig-Bandwidth-Speed-Kbps": "5162.000",
            "X-Ig-Bandwidth-Totalbytes-B": "0",
            "X-Ig-Bandwidth-Totaltime-Ms": "0",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": "bloks_unknown_class:select_verification_method:1:button:1737199364.978::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "3348",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        LOG = self.QTR.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',headers=headers ,data=data)
        if ("Bearer" in LOG.text):
            sessionids = re.search(r'Bearer IGT:2:(.*?),',LOG.text).group(1).strip()
            try:
                session = sessionids[:-8]
                graps=base64.b64decode(session).decode('utf-8')
                if "sessionid"  in graps:sessionid = re.search(r'"sessionid":"(.*?)"}',graps).group(1).strip()
            except Exception as JOK:
                sessionid = sessionid
            try:
                sessionid2 = re.sub(r'\\+', '', sessionids).split('"')[0]
            except Exception as JOK:
                sessionid2 = sessionids
            print(f'[+] Sessionid API 1 : {sessionid}')
            print(f'[+] Sessionid API 2 : {sessionid2}')
            with open('sessionids.txt', 'w') as f:
                f.write(f'Sessionid API 1 : {sessionid}\nSessionid API 2 : {sessionid2}\n')
            input('[+] Sessionid saved in sessionids.txt , Press Enter to continue')
            os._exit(0)
        elif ("two_step_verification" in LOG.text):
            print('[+] Type : two_step_verification_context')
            url=LOG.text.replace('\\\\\\', '')
            try:
                u = url.split('two_step_verification_context')[1]
                two_step_verification_context = u.split('bk.action.array.Make,')[1].split('"')[1].split('"')[0]
                self.two_step_verification_context = two_step_verification_context.rstrip('\\')
            except Exception as Jok:
                u = url.split('com.bloks.www.ap.two_step_verification.entrypoint_async')[1]
                self.two_step_verification_context=u.split('device_id')[1].split('bk.action.array.Make,')[1].split('"')[1].rstrip('\\')
            self.two_step_verification()
        elif ("challenge_required" in LOG.text):
            print('[+] Type : challenge_required')
            url = re.search(r'url(.*?),',LOG.text).group(1).strip()
            url=url.replace('\\\\\\', '')
            self.APIS=url.split('challenge')[1].split('\\\",')[0].split('"')[0]
            _context = re.search(r'challenge_context(.*?),',LOG.text).group(1).strip()
            _context=_context.replace('\\\\\\', '')
            self._context=_context.split('":"')[1].split('\\\",')[0].split('"}')[0]
            self.challenge_required()
        elif "The password you entered is incorrect" in LOG.text or "Please check your username and try again." in LOG.text or "inactive user" in LOG.text or "should_dismiss_loading\", \"has_identification_error\"" in LOG.text:
            print(f"{Fore.RED}[-] Bad Passowrd {Fore.BLUE}Try again")
            self.login()
        else:
            print(f"{Fore.RED}[!] Something wrong {Fore.BLUE}Try again")
            os._exit(0)

IG_LOGIN()
