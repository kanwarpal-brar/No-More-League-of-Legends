import ProcessBlocker as ProcessBlocker
import threading
import sys


def main():  # Main function, begins the execution of main thread
    # Launch the waiting thread, to see if League is running
    threading.Thread(
        target=ProcessBlocker.ProcessBlocker(['LeagueClient.exe', 'RiotClientServices.exe'],
                                             1,
                                             int(sys.argv[1]) if len(sys.argv) >= 2 else -1).waitForProcess).start()


if __name__ == '__main__':  # Runs the main, by the __main__.py function
    main()
