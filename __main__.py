import psutil
import threading
import time
import os
import logging
# Application to Curb Imaan and Ajay's addictions to League of Legends

if "RiotClientServices.exe" in (p.name() for p in psutil.process_iter()):
    print("Yes")


def main():  # Main function, begins the execution of all threads (manages all threads from here)
    # Launch the waiting thread, to see if League is running
    launchWaitThread = threading.Thread(target=waitForLeagueLaunch)
    launchWaitThread.start()

def waitForLeagueLaunch():  # This function is run on a timer, and checks to see if league has been launched
    # League is killed if a launch is detected
    # If no launch, sleep the thread for 3 minutes, check again after
    if leagueIsRunning():
        print("kill")
        try:
            os.system("taskkill /f /im LeagueClient.exe")
            os.system("taskkill /f /im RiotClientServices.exe")
        except:
            pass
    else:
        time.sleep(180)  # After checking if league is running, thread sleeps for 3 minutes


def leagueIsRunning():  # Checks if a league of legends-related application is running, returns true
    if "RiotClientServices.exe" in (p.name() for p in psutil.process_iter()):
        return True
    elif "LeagueClient.exe" in (p.name() for p in psutil.process_iter()):
        return True
    else:
        return False

def hideSelf():  # This method is reponsible for hiding the application to a new folder on each launch
    return

def enableStartup():  # This method allows the application to run on startup
    return


if __name__ == '__main__':  # Runs the main, by the __main__.py function
    main()
