import time
import pychromecast 
castNames = []
services, browser = pychromecast.discovery.discover_chromecasts()
pychromecast.discovery.stop_discovery(browser)
for cast in services:
    print(cast[2],":",cast[3],":",cast[4])
    castNames.append(cast[3])

for thing in castNames:    
    chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[thing])
    [cc.device.friendly_name for cc in chromecasts]
    cast = chromecasts[0]
    cast.wait()
    print(cast.device)
    print(cast.status)
    mc = cast.media_controller
    #mc.play_media('http://kristofer.is/meme/spooky.mp3', 'audio/mp3')
    #mc.block_until_active()
    
    print(mc.status)
    pychromecast.discovery.stop_discovery(browser)
    print("----------------------------------------------")
