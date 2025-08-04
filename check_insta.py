import requests
from user_agent import generate_user_agent
from pystyle import Colors ,Write
from colorama import Fore, Style
#..................................................
useragent = generate_user_agent()
#..................................................
print("""  _                              ___   ___ 
 | |__   _ __   __ _   ___  ___ |_  ) | __|
 | '_ \ | '_ \ / _` | (_-< (_-<  / /  |__ 
 |_.__/ | .__/ \__,_| /__/ /__/ /___| |___/
        |_|      

        Telegram chanal : @bpass25
        Telegram user : @bpass25_25
        
        """)
#..................................................

def check_instagram():
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    data = { 
        "email_or_username": Email,
        "jazoest": 21779
            }
    headers = {
        "user-agent" : useragent,

        "x-csrftoken" : "LSdjRJ1tB-73_eU_POHXGn"
    }
    req_ = requests.post(url=url, data=data,headers=headers)
    if "toast_message"  in req_.json():
        print("Email is Fonud in the instagram" )
    else :
        print("Email is not Fonud in the instagram")
#..................................................
Email = Write.Input("Enter your email : ",Colors.blue_to_red)
check_instagram()
