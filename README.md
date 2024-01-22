# jellyfin-keep-awake
A Python script to prevent a Jellyfin server falling asleep while streaming is active

# Summary
Scenario: you have a PC that you use as a Jellyfin server, and you want it to be able to fall asleep when not in use.
Jellyfin doesn't have a built-in method of preventing system sleep while streaming is happening.
This script runs in the background and monitors the Jellyfin activity. While streaming is active, the system will stay awake - but when no streaming is happening, the system will sleep.

**Note** - this was written to be OS-agnostic, so should work on Windows or Linux systems. 
It is **untested** on Windows however, so use at your own risk.
I personally use it on my Linux (Ubuntu) system and it works well.

# Usage
- Clone the repo
- Use a platform-specific method to run the script in the background, preferably on system boot
- Enjoy!

 # Running on start-up

 **Linux**
 The script needs to run as soon after start-up as Jellyfin itself is running. I created a Start-up Script in Ubuntu with this argument:
 `python3 /path/to/file.py`

 **Windows**
 You can use Task Scheduler to start the script on boot, but I don't have specific instructions for that.
