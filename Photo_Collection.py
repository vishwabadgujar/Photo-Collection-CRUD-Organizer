import json
import os
from datetime import datetime

data_file = "my_photos_data.json"

stuffList = []
picNum = 1


def loadStuff():
    global stuffList, picNum

    if not os.path.exists(data_file):
        print("no file, starting fresh")
        return

    try:
        with open(data_file, "r") as f:
            try:
                bx = json.load(f)
            except:
                bx = {}

            stuffList = bx.get("items", [])

        if stuffList:
            m = 0
            for t in stuffList:
                v = t.get("num", 0)
                if type(v) == int and v > m:
                    m = v
            picNum = m + 1
        else:
            picNum = 1

        print("loaded", len(stuffList))
    except:
        print("load error")
        stuffList = []
        picNum = 1


def saveStuff():
    try:
        with open(data_file, "w") as f:
            json.dump({"items": stuffList}, f, indent=4)
        print("saved")
    except Exception as e:
        print("save err", e)


def addOne():
    global picNum

    print("\n-- add item --")

    nm = input("title: ")
    if nm.strip() == "":
        nm = "untitled"

    place = input("location: ")
    tg = input("tags (comma): ")
    fileSpot = input("file: ")

    today = datetime.now().strftime("%Y-%m-%d")
    dd = input("date: ").strip()

    if dd:
        try:
            datetime.strptime(dd, "%Y-%m-%d")
            finalDate = dd
        except:
            print("bad date, using today")
            finalDate = today
    else:
        finalDate = today

    tgBox = []
    if tg.strip():
        for p in tg.split(","):
            pp = p.strip().lower()
            if pp:
                tgBox.append(pp)

    tempBox = {
        "num": picNum,
        "name": nm,
        "place": place,
        "taken": finalDate,
        "tgs": tgBox,
        "file": fileSpot
    }

    stuffList.append(tempBox)
    print("added", picNum)
    picNum += 1


def showAll():
    if not stuffList:
        print("nothing saved")
        return

    searchTxt = input("search (blank=all): ").strip().lower()
    foundList = []

    if searchTxt == "":
        for h in stuffList:
            foundList.append(h)
    else:
        for h in stuffList:
            nm = str(h.get("name", "")).lower()
            ok = False

            if searchTxt in nm:
                ok = True
            else:
                gg = h.get("tgs", [])
                for z in gg:
                    if searchTxt in z:
                        ok = True
                        break

            if ok:
                foundList.append(h)

    print("found:", len(foundList))
    if not foundList:
        print("none match")
        return

    for it in foundList:
        ts = ", ".join(it.get("tgs", []))
        print("")
        print("ID:", it.get("num"))
        print("Title:", it.get("name"))
        print("Location:", it.get("place"))
        print("Date:", it.get("taken"))
        print("Tags:", ts)


def fixOne():
    print("\n-- edit item --")
    x = input("id: ")

    try:
        y = int(x)
    except:
        print("not a number")
        return

    target = None
    for s in stuffList:
        if s.get("num") == y:
            target = s
            break

    if target is None:
        print("no id")
        return

    print("editing:", target.get("name"))

    nt = input("new title: ").strip()
    if nt:
        target["name"] = nt

    nl = input("new location: ").strip()
    if nl:
        target["place"] = nl

    nx = input("new tags: ").strip()
    if nx:
        t2 = []
        for k in nx.split(","):
            k2 = k.strip().lower()
            if k2:
                t2.append(k2)
        target["tgs"] = t2

    nf = input("new file path: ").strip()
    if nf:
        target["file"] = nf

    print("updated")


def removeOne():
    print("\n-- delete --")
    x = input("id: ")

    try:
        y = int(x)
    except:
        print("bad id")
        return

    idx = -1
    for i, s in enumerate(stuffList):
        if s.get("num") == y:
            idx = i
            break

    if idx < 0:
        print("not found")
        return

    c = input("sure? (y/n): ").lower()
    if c == "y":
        try:
            del stuffList[idx]
            print("removed")
        except:
            print("err deleting")
    else:
        print("no action")


def runNow():
    loadStuff()

    while True:
        print("""
1 add
2 view
3 edit
4 delete
5 quit
""")

        w = input("pick: ").strip()

        if w == "1":
            addOne()
        elif w == "2":
            showAll()
        elif w == "3":
            fixOne()
        elif w == "4":
            removeOne()
        elif w == "5":
            saveStuff()
            print("bye")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    runNow()