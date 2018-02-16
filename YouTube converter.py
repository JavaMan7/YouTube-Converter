import pafy 
from threading import Thread
from appJar import gui

app = gui("YouTube converter by Jordan Bowley", "400x200")
app.addLabel("youtube", "Welcome to appJar")

app.addLabelEntry("url")
app.addLabelEntry("url playlist")


app.addLabelEntry("output")

app.setEntry("output","D:\\\\m\\t\\", callFunction=False)
app.addLabelOptionBox("Formats", ["mp3","wav",  "mp4","ogg","m4a","flv","webm","3gp"
                        ])

app.addMeter("progress")




def press(button):
    #if button == "Cancel":
       # t1.stop()
    #else:
        url = app.getEntry("url")
        if url == "":
         
        
         output = app.getEntry("output")
         url = app.getEntry("url playlist")
         videoPafy = pafy.get_playlist(url)
         print(len(videoPafy['items']))
         for x in range(0,len(videoPafy['items'])):
          t1 = Thread(target=write, args=[url,output,videoPafy['items'][int(x)]['pafy']])
         
          t1.start()
        else:
         
         output = app.getEntry("output")
         videoPafy = pafy.new(url)
         t1 = Thread(target=write, args=[url,output,videoPafy])
         t1.start()
app.addButtons(["Submit", "Cancel"], press)
def writePlaylist(url,output,x,videoPafy):
    
    
    f=app.getOptionBox("Formats")
    if(f== "wav"):
    
     print(x)
     best =  videoPafy['items'][int(x)]['pafy'].getbestaudio()#(preftype=f)
      
     best.download(filepath=output+videoPafy['items'][int(x)]['pafy'].title+"."+f, quiet=False, callback=None, meta=False, remux_audio=False)
    else:
     
      print(x)
      best =  videoPafy['items'][int(x)]['pafy'].getbest(preftype=f)
      
      
      best.download(filepath=output+videoPafy['items'][int(x)]['pafy'].title+"."+f, quiet=False, callback=None, meta=False, remux_audio=False)
def write(url,output,videoPafy):
    
    
    f=app.getOptionBox("Formats")
    if(f== "wav" or f=="mp3"):
     
     print("hi")
     best =  videoPafy.getbestaudio()#(preftype=f)
      
     best.download(filepath=output+videoPafy.title+"."+f, quiet=False, callback=None, meta=False, remux_audio=False)
    else:
    
    
     best =  videoPafy.getbest(preftype=f)
      
      
     best.download(filepath=output+videoPafy.title+"."+f, quiet=False, callback=None, meta=False, remux_audio=False)
app.go()
#best.download(filepath="D:\\vd", quiet=False, callback=None, meta=False, remux_audio=False)

