# coding: utf-8

steam_api_key = '51E1C5B51900BB2AB0D1849A839EBB45'  # Your Steam API Key obtainable here : https://steamcommunity.com/dev/apikey
server_ip_address = '208.103.169.233:27015'  # The IP address of the server you want to connect to.
steam_request_url = f'https://api.steampowered.com/IGameServersService/GetServerList/v1/?filter=\\appid\\4000\\addr\\{server_ip_address}&key={steam_api_key}'  # Don't touch without reason
