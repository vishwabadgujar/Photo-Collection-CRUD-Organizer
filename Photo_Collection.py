import json
import os
from datetime import datetime

file_name = "my_photos_data.json"

photo_data = []
id_num = 1


def load_data():
    global photo_data, id_num

    if not os.path.exists(file_name):
        print("starting with empty data (file missing)")
        return

    try:
        with open(file_name, "r") as f:
            try:
                temp = json.load(f)
            except:
                temp = {}

            photo_data = temp.get("photos", [])

        if len(photo_data) > 0:
            try:
                highest = 0
                for x in photo_data:
                    xid = x.get("id", 0)
                    if type(xid) == int and xid > highest:
                        highest = xid
                id_num = highest + 1
            except:
                id_num = 1
        else:
            id_num = 1

        print("loaded:", len(photo_data))
    except:
        print("something went wrong loading file")
        photo_data = []
        id_num = 1


def save_data():
    try:
        with open(file_name, "w") as f:
            json.dump({"photos": photo_data}, f, indent=4)
        print("data saved ok")
    except Exception as e:
        print("save failed:", e)


def add_new():
    global id_num

    print("\n--- new photo ---")

    t = input("title: ")
    if t.strip() == "":
        t = "untitled"

    locat = input("location: ")
    tg = input("tags (comma sep): ")
    fp = input("file path: ")

    today = datetime.now().strftime("%Y-%m-%d")
    d = input("date (YYYY-MM-DD or blank): ")

    if d.strip() != "":
        try:
            datetime.strptime(d, "%Y-%m-%d")
            dt = d
        except:
            print("bad date, using today")
            dt = today
    else:
        dt = today

    # tags processing
    taglist = []
    if tg.strip() != "":
        for kk in tg.split(","):
            k2 = kk.strip().lower()
            if k2:
                taglist.append(k2)

    obj = {
        "id": id_num,
        "title": t,
        "location": locat,
        "date_taken": dt,
        "tags": taglist,
        "filepath": fp
    }

    photo_data.append(obj)

    print("added id", id_num)
    id_num += 1


def view_all():
    if len(photo_data) == 0:
        print("no items to show")
        return

    search = input("search (enter = all): ").strip().lower()

    results = []

    if search == "":
        for xx in photo_data:
            results.append(xx)
    else:
        for item in photo_data:
            title = str(item.get("title", "")).lower()
            found = False

            if search in title:
                found = True
            else:
                tg = item.get("tags", [])
                for one in tg:
                    if search in one:
                        found = True
                        break

            if found:
                results.append(item)

    print("results:", len(results))

    if len(results) == 0:
        print("nothing found")
        return

    for r in results:
        ts = ", ".join(r.get("tags", []))
        print("")
        print("ID:", r.get("id"))
        print("Title:", r.get("title"))
        print("Location:", r.get("location"))
        print("Date:", r.get("date_taken"))
        print("Tags:", ts)


def edit_item():
    print("\n--- edit ---")
    x = input("id number: ")

    try:
        nid = int(x)
    except:
        print("not a number")
        return

    found = None
    for i in photo_data:
        if i.get("id") == nid:
            found = i
            break

    if found is None:
        print("no such id")
        return

    print("editing:", found.get("title"))

    newtitle = input("new title (blank keep): ")
    if newtitle.strip():
        found["title"] = newtitle

    newloc = input("new location (blank keep): ")
    if newloc.strip():
        found["location"] = newloc

    newtg = input("new tags (blank keep): ")
    if newtg.strip():
        tgs = []
        for w in newtg.split(","):
            w2 = w.strip().lower()
            if w2:
                tgs.append(w2)
        found["tags"] = tgs

    newfp = input("new file path (blank keep): ")
    if newfp.strip():
        found["filepath"] = newfp

    print("done editing")


def delete_item():
    print("\n--- delete ---")
    q = input("id: ")

    try:
        qid = int(q)
    except:
        print("bad id")
        return

    pos = -1
    for a, p in enumerate(photo_data):
        if p.get("id") == qid:
            pos = a
            break

    if pos == -1:
        print("id not found")
        return

    c = input("really delete? (y/n): ").lower()
    if c == "y":
        try:
            del photo_data[pos]
            print("deleted")
        except:
            print("delete error")
    else:
        print("cancelled")


def run():
    load_data()

    while True:
        print("""
1 add new
2 view/search
3 edit
4 delete
5 quit
""")

        ch = input("choice: ")

        if ch == "1":
            add_new()
        elif ch == "2":
            view_all()
        elif ch == "3":
            edit_item()
        elif ch == "4":
            delete_item()
        elif ch == "5":
            save_data()
            print("bye")
            break
        else:
            print("huh? invalid")


if __name__ == "__main__":
    run()