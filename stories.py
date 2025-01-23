try:
    from requests import Session 
    from secrets import token_hex
    from colorama import Fore , Style
    from uuid import uuid4
    from time import sleep , time
    import os , json , requests
except Exception as JK:
    print(JK)
    input()

def set_cmd_window_size(width, height):
    os.system(f'mode con: cols={width} lines={height}')
set_cmd_window_size(140, 25)
Purple="\033[1;35m"
def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    return fr"""                                                                                     
{Fore.BLUE}

    dMMMMb  dMMMMb  dMP dMP dMP .aMMMb dMMMMMMP dMMMMMP        .dMMMb dMMMMMMP .aMMMb  dMMMMb  dMP dMMMMMP .dMMMb 
   dMP.dMP dMP.dMP amr dMP dMP dMP"dMP   dMP   dMP            dMP" VP   dMP   dMP"dMP dMP.dMP amr dMP     dMP" VP 
  dMMMMP" dMMMMK" dMP dMP dMP dMMMMMP   dMP   dMMMP           VMMMb    dMP   dMP dMP dMMMMK" dMP dMMMP    VMMMb   
 dMP     dMP"AMF dMP  YMvAP" dMP dMP   dMP   dMP            dP .dMP   dMP   dMP.aMP dMP"AMF dMP dMP     dP .dMP   
dMP     dMP dMP dMP    VP"  dMP dMP   dMP   dMMMMMP         VMMMP"   dMP    VMMMP" dMP dMP dMP dMMMMMP  VMMMP"    
                                                                                                                  
                    By Joker @vv1ck | @221298
"""
def get_user_input(prompt, error_message):
    while True:
        value = input(prompt)
        if value:
            return value
        print(error_message)
class Followers:
    def __init__(self):
        self.session = Session()
        self.ST = 0
        print(LOGO())
        self.RUN = True
        self.CM = 0
        self.TOTAL_USERS = 0
        self.USERSLIST = []
        while True:
            self.mode = input(f'{Purple}1. Add member private stories\n{Fore.GREEN}2. Get followers\n{Fore.YELLOW}Choose: {Style.RESET_ALL}')
            if self.mode in ['1', '2']:
                if self.mode == '2': 
                    while True:
                        self.TARGET_USERs = input(f'{Purple}[+] Enter Target User: {Style.RESET_ALL}')
                        self.generate_headers()
                        self.INFO_ACCONTS()
                        if self.TARGET_USER != 'None':
                            break
                        else:
                            print(f'{Fore.RED}[-] Username not found')
                while True:
                    self.token = input(f'{Purple}[+] Enter Sessionid: {Style.RESET_ALL}')
                    if len(self.token) < 10:pass
                    else:break
                self.get_admin_id()
                break
            else:
                print('[-] Invalid mode')
    def generate_headers(self):
        self.uid = uuid4().hex.upper()
        self.csr = token_hex(8) * 2
        self.miid = token_hex(13).upper()
        self.dtr = token_hex(13)
    def INFO_ACCONTS(self):
        try:
            headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en,en;q=0.9','cookie': f'ig_did={self.uid}; datr={self.dtr}; mid={self.miid}; ig_nrcb=1; csrftoken={self.csr}; ds_user_id=vv11cckk; dpr=1.25','referer': f'https://www.instagram.com/{self.TARGET_USERs}/?hl=en',#joker
            'sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"','Sec-Ch-Ua-Full-Version-List': 'Not;A=Brand";v="99.0.0.0", "Chromium";v="106.0.5249.62','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin','user-agent': 'Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)','viewport-width': '1051','x-asbd-id': '198387','x-csrftoken': str(self.csr),'x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-requested-with': 'XMLHttpRequest'}
            _INFO = self.session.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={self.TARGET_USERs}', headers=headers, timeout=10)
            try:self.TARGET_USER = _INFO.json()['data']['user']['id']
            except Exception as JOKER:self.TARGET_USER = 'None'
        except (requests.exceptions.ConnectionError , requests.exceptions.ReadTimeout , requests.exceptions.ChunkedEncodingError , requests.exceptions.InvalidURL , requests.exceptions.ProxyError , requests.exceptions.Timeout , requests.exceptions.HTTPError):
            print('Connection error, your internet may be slow or blocked, use a vpn')
        
    def get_admin_id(self):
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": str(time()),
            "X-Ig-Bandwidth-Speed-Kbps": "19888.000",
            "X-Ig-Bandwidth-Totalbytes-B": "4689295",
            "X-Ig-Bandwidth-Totaltime-Ms": "217",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "hmac.AR1WLxFW5if_vvYNcmTIb54J-_0M6c9V_w0ywVddo8VIQZ6T",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": "ProfileMediaTabFragment:self_profile:17:main_profile:1737208776.706::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "Authorization": f"Bearer IGT:2:{self.token}",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        response = self.session.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=headers)
        if ('pk_id' in response.text):
            self.USERNAME_ADMIN = response.json()['user']['username']
            self.ID_ADMIN = response.json()['user']['pk_id']
            print(f'{Fore.GREEN}[+] Admin Username: {self.USERNAME_ADMIN} - ID: {self.ID_ADMIN}')
            sleep(5)
            if self.mode == '1':
                self.GET_followers_ID()
            else:
                self.GET_followers()
        elif ("You've Been Logged Out" in response.text):
            print(f'{Fore.RED}[-] Session: {self.token} - Logged Out')
            sleep(4)
            while True:
                self.token = input(f'{Purple}[+] Enter New Sessionid: {Style.RESET_ALL}')
                if len(self.token) < 10:pass
                else:break
            self.get_admin_id()
        else:
            print(f'{Fore.RED}[-] Session: {self.token} - Logged Out')
            sleep(4)
            while True:
                self.token = input(f'{Purple}[+] Enter New Sessionid: {Style.RESET_ALL}')
                if len(self.token) < 10:pass
                else:break
            self.get_admin_id()
    
    def GET_followers_ID(self):
        while True:
            file = 'users-ID.txt'
            if os.path.exists(file):break
            else:
                print(f'[-] {file} not found')
                continue
        with open(file, 'r') as f:
            for line in f:
                try:
                    USERNAME, ID = line.strip().split(':')
                except ValueError:
                    ID = line.strip()
                    USERNAME = ID
                self.add_member_private_stories(ID, USERNAME)
    def add_member_private_stories(self, ID, USERNAME):
        headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
            "X-Pigeon-Rawclienttime": str(time()),
            "X-Ig-Bandwidth-Speed-Kbps": "19888.000",
            "X-Ig-Bandwidth-Totalbytes-B": "4689295",
            "X-Ig-Bandwidth-Totaltime-Ms": "217",
            "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
            "X-Ig-Www-Claim": "hmac.AR1WLxFW5if_vvYNcmTIb54J-_0M6c9V_w0ywVddo8VIQZ6T",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
            "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
            "X-Ig-Android-Id": "android-279938d90eae62a5",
            "X-Ig-Timezone-Offset": "28800",
            "X-Ig-Nav-Chain": f"MainFeedFragment:feed_timeline:1:cold_start:{str(time())}::,QuickCaptureFragment:stories_gallery:18:your_story_placeholder:{str(time())}::,CameraSettingsFragment:camera_settings:19:button:{str(time())}::,CameraSettingsFragment:stories_camera_settings:20:button:{str(time())}::,PrivateStoryAudiencePickerFragment:audience_selection:21:button:{str(time())}::",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "X-Ig-App-Id": "567067343352427",
            "Priority": "u=3",
            "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
            "Accept-Language": "en-US",
            "Authorization": f"Bearer IGT:2:{self.token}",
            "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
            "Ig-U-Ds-User-Id": f"{self.ID_ADMIN}",
            "Ig-U-Rur": f"RVA,{self.ID_ADMIN},{str(time())}:01f72924f5ed709fea2b4a7985a2e98338c11147f4e3f655936a7af5f640790215dbb552",
            "Ig-Intended-User-Id": f"{self.ID_ADMIN}",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "108",
            "Accept-Encoding": "gzip, deflate",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True"}
        data = f'module=audience_selection&source=story_settings&user_id={ID}&_uuid=f7a78e22-d663-48de-bee6-e56388b68cd3'
        add_member = self.session.post(f'https://i.instagram.com/api/v1/stories/private_stories/add_member/', headers=headers, data=data)
        if ('"status":"ok"' in add_member.text):
            print(f'{Fore.GREEN}[+] Add member private stories success: {USERNAME}')
        else:
            print(f'{Fore.RED}[-] Add member private stories failed: {USERNAME}')
            print(add_member.text)
        sleep(3)
        
    
    def Filter_users(self, USERS):
        while True:
            try:
                ID = USERS[0]['pk_id']
                USERNAME = USERS[0]['username']
                if ID not in self.USERSLIST:
                    self.USERSLIST.append(ID)
                    with open('users-ID.txt', 'a') as file:
                        file.write(f'{USERNAME}:{ID}\n')
                    self.TOTAL_USERS += 1
                print(f'{Fore.GREEN}[+] Username: {USERNAME} - ID: {ID} - Total Users: {self.TOTAL_USERS}')
                USERS.pop(0)
            except Exception as JOKER:
                self.ST = 1
                sleep(5)
                break

    def GET_followers(self):
        while self.RUN:
            headers = {
                "Host": "i.instagram.com",
                "X-Ig-App-Locale": "en_US",
                "X-Ig-Device-Locale": "en_US",
                "X-Ig-Mapped-Locale": "en_US",
                "X-Pigeon-Session-Id": "UFS-ba61fdae-0ac1-4f2c-9f02-93f2de719873-0",
                "X-Pigeon-Rawclienttime": str(time()),
                "X-Ig-Bandwidth-Speed-Kbps": "19888.000",
                "X-Ig-Bandwidth-Totalbytes-B": "4689295",
                "X-Ig-Bandwidth-Totaltime-Ms": "217",
                "X-Bloks-Version-Id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
                "X-Ig-Www-Claim": "hmac.AR1WLxFW5if_vvYNcmTIb54J-_0M6c9V_w0ywVddo8VIQZ6T",
                "X-Bloks-Is-Layout-Rtl": "false",
                "X-Ig-Device-Id": "f7a78e22-d663-48de-bee6-e56388b68cd3",
                "X-Ig-Family-Device-Id": "91f6c5a4-5d85-4bb8-8766-c68e303bf770",
                "X-Ig-Android-Id": "android-279938d90eae62a5",
                "X-Ig-Timezone-Offset": "28800",
                "X-Ig-Nav-Chain": f"ExploreFragment:explore_popular:7:main_search:{str(time())}::,SingleSearchTypeaheadTabFragment:search_typeahead:8:button:{str(time())}::,UserDetailFragment:profile:12:search_result:{str(time())}::,ProfileMediaTabFragment:profile:13:button:{str(time())}::,FollowListFragment:followers:14:button:{str(time())}::",
                "X-Fb-Connection-Type": "WIFI",
                "X-Ig-Connection-Type": "WIFI",
                "X-Ig-Capabilities": "3brTv10=",
                "X-Ig-App-Id": "567067343352427",
                "Priority": "u=3",
                "User-Agent": "Instagram 275.0.0.27.98 Android (28/9; 300dpi; 900x1600; google; G011A; G011A; intel; en_US; 458229257)",
                "Accept-Language": "en-US",
                "Authorization": f"Bearer IGT:2:{self.token}",
                "X-Mid": "Z4uBIQABAAHqhTG9u-Mj39nw9mWb",
                "Ig-U-Ds-User-Id": f"{self.ID_ADMIN}",
                "Ig-U-Rur": f"RVA,{self.ID_ADMIN},{str(time())}:01f7cc0b35c0ef22548fdbded58cf5e4a23b6276218bef94f1bed9108c330dd6e1592350",
                "Ig-Intended-User-Id": f"{self.ID_ADMIN}",
                "Accept-Encoding": "gzip, deflate",
                "X-Fb-Http-Engine": "Liger",
                "X-Fb-Client-Ip": "True",
                "X-Fb-Server-Cluster": "True"}
            if self.ST == 0:
                URL = f'https://i.instagram.com/api/v1/friendships/{self.TARGET_USER}/followers/?search_surface=follow_list_page&query=&enable_groups=true&rank_token=90745fe9-84ac-4212-afd0-d9830218938e'
            else:
                URL = f'https://i.instagram.com/api/v1/friendships/{self.TARGET_USER}/followers/?search_surface=follow_list_page&max_id={self.next_max_id}&query=&enable_groups=true&rank_token=90745fe9-84ac-4212-afd0-d9830218938e'
            USERS = self.session.get(URL, headers=headers)
            if ('pk_id' in USERS.text):
                try:
                    self.next_max_id = USERS.json()['next_max_id']
                except KeyError:
                    input('Finish Extract Followers , Press Enter to Exit ...')
                    break
                self.Filter_users(USERS.json()['users'])
            elif ('"Please wait a few minutes before you try again."' in USERS.text):
                print(f'{Fore.RED}[-] Please wait a few minutes before you try again.')
                sleep(4)
                while True:
                    self.token = input(f'{Purple}[+] Enter New Sessionid: {Style.RESET_ALL}')
                    if len(self.token) < 10:pass
                    else:break
                self.get_admin_id()
            else:
                print(f'{Fore.RED}[-] Please wait a few minutes before you try again.')
                sleep(4)
                while True:
                    self.token = input(f'{Purple}[+] Enter New Sessionid: {Style.RESET_ALL}')
                    if len(self.token) < 10:pass
                    else:break
                self.get_admin_id()

if __name__ == '__main__':
    Followers()