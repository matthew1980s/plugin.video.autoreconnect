import xbmc
import xbmcgui
import time

STREAMS = [
    {
        "url": "https://el4live1.boldmss.com/ELCUATRO/ELCUATRO_EL4.isml/manifest",
        "headers": "User-Agent=Mozilla/5.0&Referer=https://elcuatrogo.com&Origin=https://elcuatrogo.com",
        "type": "ism"
    },
    {
        "url": "http://anbalancer.express.com.ar/live/c1eds/Canal_4_Salta/SA_PR_cipix/Manifest",
        "headers": "User-Agent=Mozilla/5.0&Referer=https://nowtv.express.com.ar/&Origin=https://nowtv.express.com.ar",
        "type": "ism"
    }
]

player = xbmc.Player()

def play_stream(stream):
    url = stream["url"] + "|" + stream["headers"]

    li = xbmcgui.ListItem(path=url)
    li.setProperty("inputstream", "inputstream.adaptive")
    li.setProperty("inputstream.adaptive.manifest_type", stream["type"])

    player.play(item=li)

while True:
    for stream in STREAMS:
        player.stop()
        time.sleep(1)

        play_stream(stream)

        started = False
        for i in range(6):
            if player.isPlaying():
                started = True
                break
            time.sleep(1)

        if not started:
            continue

        while player.isPlaying():
            time.sleep(1)

        player.stop()
        time.sleep(1)
