textual-znc-backlog
===========
textual-znc-backlog is a plugin for the macOS IRC client Textual when used together with a ZNC server.
It is designed to create an alias for requesting backlog messages from the ZNC server without having to send a private message to the `*backlog` plugin.

Dependencies
------------
Have [ZNC backlog](https://wiki.znc.in/Backlog) plugin installed on the server.

Installing
------------
* Download the `bl.py` file. The location to save this file will depend on how you installed Textual:
  * If you installed Textual from the Mac App Store, save the file to: `~/Library/Application\ Scripts/com.codeux.apps.textual-mas/bl.py`
  * If you installed Textual by other means, save the file to: `~/Library/Application\ Scripts/com.codeux.apps.textual/bl.py`

* Give execution permissions to the script. Again, the path will depend on your installation method:
  * Mac App Store: `chmod +x ~/Library/Application\ Scripts/com.codeux.apps.textual-mas/bl.py`
  * Other: chmod +x `~/Library/Application\ Scripts/com.codeux.apps.textual/bl.py`

* The plugin will be executed when you run the command. It's not required to restart the client.

Usage
-----
`/bl [channel] [messages]`

The functionality will be the same as if you were requesting it by manually sending a private message to the `*backlog` plugin. The backlog messages will be displayed in the corresponding window for the requested channel or window.

Examples
-----
If you execute `/bl` without arguments, it will send `/msg *backlog <current_channel>`, where `<current_channel>` is the channel (or window) you are currently in, and it will print the default amount of messages from the plugin's backlog.

If you execute `/bl 10`, it will send `/msg *backlog <current_channel> 10`, where `<current_channel>` is the channel (or window) you are currently in, and `10` is the number of backlog messages you want to be printed.

If you execute `/bl #channel`, it will send `/msg *backlog #channel` and print the default amount of messages from the plugin's backlog.

If you execute `/bl #channel 10`, it will send `/msg *backlog #channel 10`, where `#channel` is the channel from which you want to request the backlog, and `10` is the number of backlog messages you want to be printed.
