import time, shutil, os

with open("Handy.m3u", "r") as f: 
    data = f.readlines()

#used to display progress
totallen = len(data)
count = 0

existcount = 0
newcount = 0

for line in data:
    count += 1

    #set source filename and destination folder
    src = "/home/tom"+line.strip("..\n")
    try:
        if src.startswith("/home/tom/Music/"):
            dest = "/run/media/tom/16A8-F2A8/Music" + os.path.dirname(src).replace("/home/tom/Music","")
        else:
            raise directoryNameError("Source directory isn't named as we expected")
    except Exception as ex:
        print(ex)
    
    #clear screen
    os.system('cls' if os.name=='nt' else 'clear')
    
    if not os.path.exists(dest):
        os.makedirs(dest)

    existing = os.path.exists(dest+"/"+os.path.basename(src))

    #show progress
    if not existing:
        print(f"{count / totallen * 100:.2f}" + "%")
        print("Source File: " + src)
        print("Destination: " + dest)
    else:
        print(f"{count / totallen * 100:.2f}" + "% -!- Skipping... File already exists")
        print("Source File: " + src)

    try:
        if not existing:
            shutil.copy(src, dest)
            newcount += 1
        else:
            print(f"{src} exists already")
            existcount += 1
    except Exception as ex:
        print(ex)
print("\nFinished")
print(f"Added {newcount} new songs. {existcount} Songs already existed")


