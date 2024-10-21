import requests
import time
import platform
import subprocess
import ctypes
from datetime import datetime, timedelta
import os
import subprocess

def keep_system_awake():
    # Keep system awake using platform-specific method
    env = os.environ.copy()
    env["DISPLAY"] = ":0"
    system_platform = platform.system()
    if system_platform == "Windows":
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    elif system_platform in ["Linux", "Darwin"]:
        subprocess.run(["xset", "s", "reset"], env=env)

def get_api_data():
    api_url = "http://127.0.0.1:8096/Sessions"
    headers = {"X-Emby-Token": "7245c64c15294f8686ba8f321258434b"}

    try:
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def process_api_data(api_data):
    if api_data:
        sessions = api_data

        for session in sessions:
            now_playing_item = session.get("NowPlayingItem", "");
            now_playing_queue = session.get("NowPlayingQueueFullItems", [])

            if now_playing_queue or now_playing_item:
                last_active = session.get("LastActivityDate")
                last_active = last_active[:-2]
                last_active = last_active + "Z"

                time_difference = datetime.utcnow() - datetime.strptime(last_active, "%Y-%m-%dT%H:%M:%S.%fZ")
                if time_difference < timedelta(minutes=5):
                    print(session.get("Client") + ", keeping awake")
                    keep_system_awake()
                else:
                    print(session.get("Client") + ", nothing playing")
            else:
                print(session.get("Client") + ", nothing playing")

if __name__ == "__main__":
    while True:
        api_data = get_api_data()

        if api_data:
            process_api_data(api_data)

        # Sleep for one minute before checking again
        time.sleep(60)
