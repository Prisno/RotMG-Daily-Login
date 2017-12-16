# Used to make the script run once every day
import schedule
import time

# Used to open the muledump file in a browser and close it
import webbrowser, os
import subprocess 


def login():

    browser_path = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe" # Path to browser of choice
    muledump_path = r"" # Your path to muledump
    
    # Open the muledump
    p = subprocess.Popen([browser_path, muledump_path])
    time.sleep(5)
    p.kill()
    

scheduled_time = "15:00" # What time to run the script
schedule.every().day.at(scheduled_time).do(login)

while True:
    schedule.run_pending()
    time.sleep(60)
    


