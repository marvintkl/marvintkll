import youtube_dl
from idm import IDMan
import time
import os

list=
length = len(list)
t=2
i=0
while i<length:
    url = str(list[i]) # The youtube video you want to download 
    print (url)
    downloader = IDMan()
    destination_path = r"C:\kkk\rr" # The folder path you want your downloading video to be saved

    ydl_opts = {'format': 'bestaudio[ext=m4a]'137/best'} # Choose the video format you want or using the best format available by default
                
    def extractor(url):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return info_dict

    info = extractor(url)
    title = info['title'] 
    width = info['width']
    height = info['height']
    ext = info['ext']
    download_url = info['url']
    downloader.download(download_url,path_to_save = destination_path, output=f"{title}.{ext}", referrer= url, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
    t=2  
    while t==2:
         

        import subprocess
        getVersion =  subprocess.Popen('tasklist /fi "windowtitle eq Download comp*"', shell=True, stdout=subprocess.PIPE).stdout
        version =  getVersion.read()




        print("Hello")
        fullstring = str(version.decode())
        substring = "Console"


        if substring in fullstring:
            print("Found!")
            i=i+1
            print (i)
            t = 3
            os.system('taskkill /IM idman.exe')
                   
                   
        else:
            print("Not found!")
        
        time.sleep(4)
        
        
         for %i in (*.mp4) do ffmpeg -i "%i" -i "%~ni.m4a" -c copy "%~ni.mkv"