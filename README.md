# No-More-League-of-Legends
Video games can be addictive. Sometimes, a little too addictive. This is exactly what two of my friends faced with the hit MOBA: [League of Legends](https://na.leagueoflegends.com/en-us/). I took it upon myself to write a Python script to thwart their attempts at procrastination.

## How it Works
The application is quite simple. Using Python's builtin OS, Threading, and Time modules, as well as [psutil](https://github.com/giampaolo/psutil), upon running __main__.py a new monitoring thread is started which periodically checks if two specific programs are running: LeagueClient.exe, and RiotClientServices.exe.

If the script finds these applications, it force closes them using the OS module, otherwise it waits 3 minutes before checking again.

The intent is that the script starts on boot and is always running in the background to sneakily prevent the user from launching League of Legends, and ensuring that if they do, then it won't be open for very long.

I had planned additional features which would be responsible for:
* Launching the script on boot.
* Moving the location of the script on every launch so it cannot easily be found.

But for some reason the intended demographic (a.k.a. my friends) decided that they didn't want the application, so development was halted.
