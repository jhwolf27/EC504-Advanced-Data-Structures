from tkinter import ttk
from tkinter import*

LARGE_FONT= ("Verdana", 12)

popularityrank = []
popularityranksorted = []
other = []

#hashtable to hold dictionary for song name and author in correlation to number
def init_songlist():
    i = 0
    f = open('song_list.txt')
    global songlist
    songlist = {}
    songs = f.readlines()
    for i in range(0, len(songs)):
        x = songs[i].replace('\t', " ")
        songlist[i] = [x,0]


init_songlist()


def ranksongs():
    i = 0
    j = 0
    for i in range(0, len(popularityranksorted)):
        x = popularityranksorted[i][0].split(" ")
        y = popularityranksorted[i][1]
        for j in range(0, len(x)-1):
            songlist[int(x[j])][1] += y
    for i in range(0, len(songlist)):
        other.append(songlist[i])
    global rankedsongs
    rankedsongs = sorted(other, key=lambda pop:pop[1], reverse = True)



def load_playlists(file):
    global popularityrank
    i = 0
    f = open(file)
    playlist = f.readlines()
    long = len(playlist)
    totallong = long + len(popularityrank)
    deletenumber = 0
    if long > 1024 & len(popularityrank) < 1:
        for i in range(0, 1024):
            x = playlist[i].split('\t', 1)
            popularityrank.append([x[0], int((x[1].replace('\n', "")))])
            i += 1
    elif totallong > 1024:
        deletenumber = totallong - 1024
        del popularityranksorted[-(deletenumber)]
        for i in range(0, long):
            x = playlist[i].split('\t', 1)
            popularityrank.append([x[0], int((x[1].replace('\n', "")))])
            i += 1
    else:
        for i in range(0, long):
            x = playlist[i].split('\t', 1)
            popularityrank.append([x[0], int((x[1].replace('\n', "")))])
            i += 1
    popularitysort()
    ranksongs()


def autocomplete(event):
    i = 0
    text5 = ""
    global autolist
    autolist = []
    x = (entry.get())
    for i in range(0, len(popularityranksorted)):
        if len(autolist) <= 4:
            if x in str(songlist[i]):
                autolist.append(songlist[i])

    j = 0
    for j in range(0, len(autolist)-1):
        text5 = text5 + str(autolist[j]) + "\n"

    label3.config(text = text5)



def suggestion(str):
    numb = int(entry4.get())
    text4 = ""
    i=0
    j=0
    for i in range (0, len(popularityranksorted)):
        x = popularityranksorted[i][0].split(" ")
        for j in range (0, len(x)-1):
            if (numb == int(x[j])):
                text4 = popularityranksorted[i]
                label4.config(text = text4)
                return 0




def popularitysort():
    global popularityranksorted
    popularityranksorted = sorted(popularityrank, key=lambda pop: pop[1], reverse = True)
    popularityrank[0:] = popularityranksorted[0:]
    top8Update()

def addPlaylist(str):
    x = str.split("//",1)
    if len(popularityrank) >= 1024:
        del popularityrank[-1]
    popularityrank.append([x[0], int((x[1]))])
    popularitysort()



top = Tk()
top.geometry('800x500')
topLabel = Label(top, text="PlayList App")
topLabel.pack()


master = ttk.Notebook(top)

f1 = ttk.Frame(master)
f2 = ttk.Frame(master)
master.add(f1, text = "Main Page")
master.add(f2, text = "Add PlayList")
master.pack()

entry = Entry(top)
entry.pack(side = 'bottom', fill = BOTH, pady = 10, padx = 10)



entry2 = Entry(f2)
entry2.pack(side = 'bottom', fill = BOTH, pady=10)

labelinstruct = Label(f2, text = "To import from a text file, type in the [filename].txt and click Import ")
labelinstruct2 = Label(f2, text = "To manually add one, type in this format <Playlist // Popularity(integer)> with songs by numbers and hit Add")
labelinstruct.pack(side = 'top')
labelinstruct2.pack(side = 'top')

button = Button(f2, text="Import", command=lambda: load_playlists(entry2.get()))
button.pack()
button1 = Button(f2, text="Add", command=lambda: addPlaylist(entry2.get()))
button1.pack()

text2 = "Top 8"

labelinstruct3 = Label(f1, text = "Type in song name and click suggestion")
button2 = Button(f1, text = "Suggestion", command=lambda: suggestion(entry4.get()))
button2.pack(side = 'right')

label4 = Label(f1, text = "Suggestion")
label4.pack(side = 'right')

entry4 = Entry(f1)
entry4.pack(side = 'right')

label = Label(f1, text = "Top 8 \n")
label.pack(side = "left")

label3 = Label(top, text = "")
label3.pack(side = "bottom")


def top8Update():
    text2 = "Top 8 \n"
    if len(popularityranksorted) > 8:
        i = 0
        for i in range(0, 8):
            text2 = text2 + str(popularityranksorted[i]) + "\n"
            label.config(text = text2)
    elif len(popularityranksorted) > 0:
        j = 0
        for j in range(0, len(popularityranksorted)-1):
            text2 = text2 + str(popularityranksorted[j]) + "\n"
            label.config(text = text2)



top.bind('<KeyPress>', autocomplete)
top.mainloop()
