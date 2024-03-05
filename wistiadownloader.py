import re
import requests
import wget

# Get the name and link for the video
videoName = input("Please input the name of the video: ")
copiedLink = str(input("Right-click on the video and select 'Copy link and thumbnail.' Paste the result here: "))

# Find wvideo number
wvideoList = re.findall('wvideo=\w+"', copiedLink)
wvideoString = str(wvideoList[0])
wvideoLeftRemove = wvideoString.replace('wvideo=', '')
wvideoNumber = wvideoLeftRemove.replace('"', '')
print(wvideoNumber)

# Paste after URL
iframeURL = f"http://fast.wistia.net/embed/iframe/{wvideoNumber}"
print(iframeURL)

# Get the HTML
getHTML = requests.get(iframeURL)
print(getHTML.text)

# Find the .bin 
findBin = re.findall('"(https:\/\/embed-ssl\.wistia\.com\/deliveries\/\w+\.bin)"', str(getHTML.text))
print(findBin[0])
binLink = findBin[0]

# Change .bin to .mp4
mp4Link = binLink.replace(".bin", ".mp4")
print(mp4Link)

# Save video
def download_video():
    wget.download(mp4Link, f"C:\\Users\\steph\\Videos\\{videoName}.mp4")

download_video()
