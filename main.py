import json
from pprint import pprint
from datetime import datetime

path = 'PATH' #Path of your data goes in here
with open(path, "r") as file:
    data = json.load(file)

def format_time(number):
    number = int(number/1000)
    minutes = number // 60
    seconds = number % 60
    
    if seconds == 0:
        return f"{minutes}:00"
    else:
        return f"{minutes}:{seconds:02}"

for i in data:
    ip = i['ip_addr_decrypted']
    track = i['master_metadata_track_name']
    playtime = format_time(float(i['ms_played']))
    if i['offline']:
        cnct = 'Offline'
    else:
        cnct = 'Online'
    timestamp_str = i['ts']
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
    time = timestamp.strftime("%d %B %Y %I:%M %p")
    
    if i['skipped']:
        print(f'IP: {ip}\nTrack name: {track}\nMinutes played: {playtime}\nInternet connection: {cnct}\nDate and time when played: {time}\nTrack skipped at {playtime}\n\n')
    else:
        print(f'IP: {ip}\nTrack name: {track}\nMinutes played: {playtime}\nInternet connection: {cnct}\nDate and time when played: {time}\nTrack played until the end\n\n')
#pprint(data)
