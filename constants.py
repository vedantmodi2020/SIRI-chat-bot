class Constants:
    App_name = {
        "safari": "/Applications/Safari.app",
        "itunes": "/Applications/iTunes.app",
        "calendar": "/Applications/Calendar.app",
        "contacts": "/Applications/Contacts.app",
        "messages": "/Applications/Messages.app",
        "mail": "/Applications/Mail.app",
        "facetime": "/Applications/FaceTime.app",
        "photos": "/Applications/Photos.app",
        "notes": "/Applications/Notes.app",
        "reminders": "/Applications/Reminders.app",
        "terminal": "/Applications/Utilities/Terminal.app",
        "preview": "/Applications/Preview.app",
        "appstore": "/Applications/App Store.app",
        "systempreferences": "/Applications/System Preferences.app",
        "music": "/Applications/Music.app",
        "maps": "/Applications/Maps.app",
        "calculator": "/Applications/Calculator.app",
        "messages": "/Applications/Messages.app",
        "stickies": "/Applications/Stickies.app",
        "news": "/Applications/News.app",
        "tv": "/Applications/TV.app",
        "podcasts": "/Applications/Podcasts.app",
        "diskutility": "/Applications/Utilities/Disk Utility.app",
        "activitymonitor": "/Applications/Utilities/Activity Monitor.app",
        "console": "/Applications/Utilities/Console.app",
        "keychainaccess": "/Applications/Utilities/Keychain Access.app",
        "textedit": "/Applications/TextEdit.app",
        "systeminformation": "/Applications/Utilities/System Information.app",
        "diskutil": "/sbin/diskutil",
        "activitymonitor": "/Applications/Utilities/Activity Monitor.app",
        "systemuiserver": "/System/Library/CoreServices/SystemUIServer.app",
        "networkutility": "/Applications/Utilities/Network Utility.app",
        "nettop": "/Applications/Utilities/NetTop.app",
        "archey": "/Applications/Utilities/Archey.app",
        "audiomidi": "/Applications/Utilities/Audio MIDI Setup.app",
        "airportutility": "/Applications/Utilities/Airport Utility.app",
        "diskwarrior": "/Applications/Utilities/DiskWarrior.app",
        "adobebridge2020": "/Applications/Adobe Bridge CC 2020.app",
        "launchpad": "/System/Library/CoreServices/Launchpad.app",
        "androidfile": "/Applications/Android File Transfer.app",
        "androidstudio": "/Applications/Android Studio.app",
        "blender": "/Applications/Blender.app",
        "bravebrowser": "/Applications/Brave Browser.app",
        "chromeremote": "/Applications/Google Chrome Remote Desktop Host Uninstaller.app",
        "copyclip": "/Applications/CopyClip.app",
        "dosbox": "/Applications/DOSBox.app",
        "figma": "/Applications/Figma.app",
        "firefox": "/Applications/Firefox.app",
        "googlechrome": "/Applications/Google\ Chrome.app",
        "haptickey": "/Applications/HapticKey.app",
        "jetbrainstoolbox": "/Applications/JetBrains\ Toolbox.app",
        "macsfan": "/Applications/Macs Fan Control.app",
        "memorycleaner": "/Applications/Memory Cleaner 5.app",
        "memorydiag": "/Applications/Memory Diag.app",
        "microsoftexcel": "/Applications/Microsoft Excel.app",
        "microsoftpowerpoint": "/Applications/Microsoft PowerPoint.app",
        "microsoftword": "/Applications/Microsoft Word.app",
        "notionweb": "/Applications/Notion Web Clipper.app",
        "ppteditor": "/Applications/PPT-Editor.app",
        "pock": "/Applications/Pock.app",
        "postman": "/Applications/Postman.app",
        "pritunl": "/Applications/Pritunl.app",
        "protonvpn": "/Applications/ProtonVPN.app",
        "pycharm": "/Applications/PyCharm.app",
        "python38": "/Applications/Python 3.8.app",
        "reactnative": "/Applications/React Native Debugger.app",
        "rectangle": "/Applications/Rectangle.app",
        "safari": "/Applications/Safari.app",
        "slack": "/Applications/Slack.app",
        "spotify": "/Applications/Spotify.app",
        "telegram": "/Applications/Telegram.app",
        "utilities": "/Applications/Utilities",
        "vlc": "/Applications/VLC.app",
        "visualstudio": "/Applications/Visual Studio Code.app",
        "wine": "/Applications/Wine.app",
        "winebottler": "/Applications/WineBottler.app",
        "wireshark": "/Applications/Wireshark.app",
        "xcode": "/Applications/Xcode.app",
        "xnviewmp": "/Applications/XnViewMP.app",
        "iterm": "/Applications/iTerm.app",
        "pgadmin4": "/Applications/pgAdmin 4.app",
        "zoom": "zoom.us",
    }

    ApiKey = "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"
    Serapi_key = "04b8ed8f39bfaa4c8875e64db0a941c31efff1e08ba3fd7d71737074a68e5eac"

    token = "secret_l3GhXOvblm68kBJi5p9K6w3VxbJz81Nsgq1qUJHB1z5"
    database_id = "a74c19166580480cab86596f9095d872"

    google_email_client_id = "103587891426-hen3icvurunt25u46hps9v45a2vgmt1v.apps.googleusercontent.com"
    google_email_client_secret = "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"

    gogle_smtp_port = 587
    google_smtp_server = "smtp.gmail.com"
    google_email_from = "vedantmodi201834@gmail.com"
    google_email_pwd = "bgzcwgrwsgpmrdhq"

    whatsapp_url = "https://graph.facebook.com/v17.0/131794806682160/messages"
    whatsapp_at = "EAAOHM4AQXZBEBO4yWq7yjnsI4HjeQsWZAhHB51BxLaJeCIqMtzx781ZCD8jTtl2kqqbmzA6BhC1emjsKMuUqNDRxjbGoOnPuaJ6jtmhvnl7WjR2hVrcgw5zW1zHtJ7cnAQRnW0ebR5o4Xi21XVbNWcjFKDpib5ow7MuxqZCqe5VnEZAPZB1XabFyRw2p6ZCVPjxDbJjA07wZCaZBFDtl9uCIZD"
    

    conversational_chain_template = """
  Answer the following questions as best you can. You have access to the following tools:

  spotify_pause: Useful for when the user want to pause the current song,direct call the function no input is required
  spotify_play: Useful for when the user want to play a song ,the user will tell either a song or any genre and based on that the input will be a song name based on the user data, input will only be a single song name
  search: useful when you need to answer questions about recent events. You should ask targeted questions. Not good in case of giving a detailed answer for a particular topic  
  artist_songs: Useful for when the user wants to know the songs for a particular artist
  write_notes: Useful when the user wants to write anything in the notion and save it, input will be the content mentioned by the user

  Use the following format:

  Question: the input question you must answer
  Thought: you should always think about what to do
  Action: the action to take, should be one of [spotify_pause, spotify_play, search, artist_songs, write_notes]
  Action Input: the input to the action
  Observation: the result of the action
  ... (this Thought/Action/Action Input/Observation can repeat N times,Important Thing to notice if the none of the above tools is required to answer the user then just answer the question according to what user asked
  )
  Thought: I now know the final answer
  Final Answer: the final answer to the original input question


  Begin!

  Question: {input}

  """
