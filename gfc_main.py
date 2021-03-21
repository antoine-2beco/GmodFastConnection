import pyautogui
import time
import requests
import gfc_config

request = requests.get(gfc_config.steam_request_url).json()
print("----------------------------------------------------")
print("--------------- Gmod Fast Connection ---------------")
print("----------------------------------------------------")
while True:
    validation = input("Before starting the process, make sure that your Garry's Mod game has the default icon and that your game is positioned in your taskbar.\nIn addition, in your game, make sure that the connection page of the server in question is visible as soon as it is opened.\nDo not forget to configure the gfc_config.py file. Do not open anything in full screen while the process is starting. Please don't use when server isn't full.\nEnter OK and run on this console to continue.")
    if validation in ['OK', 'ok', 'oK', 'Ok']:
        break

print(f" \nLancé sur {request['response']['servers'][0].get('name')}\n ")

waiting_timer = time.time()

while True:
    connection_timer = time.time()
    request = requests.get(gfc_config.steam_request_url).json()
    server_playerscount = request['response']['servers'][0].get('players')
    server_maximumplayers = request['response']['servers'][0].get('max_players')

    if server_maximumplayers - server_playerscount > 0:
        print(f"Il y a {server_maximumplayers - server_playerscount} place !")
        pyautogui.click('images/gmod-logo.png')
        pyautogui.moveTo('images/full-connection-button.png')
        pyautogui.click()
        end_timer = time.time()
        print(f"Temps d'attente : {round(end_timer - waiting_timer, 2)} secondes")
        print(f"Connecté en {round(end_timer - connection_timer, 2)} secondes")
        break

    else:
        print("-\n--\n-")
