import json
import os
from datetime import datetime

datFile = 'my_photos_data.json'
photoList = [] 
photoID = 1

def loadData():
    global photoList, photoID
    
    if not os.path.exists(datFile):
        print("No file found. Starting empty.")
        return

    try:
        with open(datFile, 'r') as f:
            data = json.load(f)
            photoList = data.get('photos', [])
            
            if photoList:
                max_id_val = 0
                for p in photoList: 
                    if p.get('id', 0) > max_id_val: 
                        max_id_val = p.get('id', 0)
                photoID = max_id_val + 1
            else:
                photoID = 1
                
        print(f"Data loaded. Found {len(photoList)} items.")

    except (json.JSONDecodeError, FileNotFoundError, OSError):
        print("Load error.")
        photoList = []
        photoID = 1

def saveData():
    try:
        with open(datFile, 'w') as f:
            json.dump({'photos': photoList}, f, indent=4)
        print("\nSaved.")
    except Exception as e:
        print(f"\nSave failed: {e}")

def createItem():
    global photoID
    
    print("\n--- NEW ENTRY ---")

    title = input("Title: ").strip()
    Loc = input("Location: ").strip()
    tags_in = input("Tags (csv): ").strip()
    fpath = input("File Path: ").strip()
    
    date_taken = datetime.now().strftime('%Y-%m-%d')
    date_str = input("Date (YYYY-MM-DD, default today): ").strip()
    
    if date_str != "":
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            date_taken = date_str
        except ValueError:
            print("Bad date. Using today.")
            
    newItem = {
        'id': photoID,
        'title': title or 'Unknown Item',
        'date_taken': date_taken,
        'location': Loc,
        'tags': [t.strip().lower() for t in tags_in.split(',') if t.strip() != ""],
        'filepath': fpath
    }
    
    photoList.append(newItem)
    photoID = photoID + 1
    print(f"\nAdded ID: {newItem['id']}.")

def readItem():
    if not photoList:
        print("\nEmpty.")
        return

    s_val = input("Search term (blank for all): ").strip().lower()
    
    results = []
    
    if s_val == "":
        results = photoList
        print(f"\n--- Showing All {len(results)} ---")
    else:
        for p in photoList:
            is_match = False
            
            if s_val in p.get('title', '').lower():
                is_match = True
            
            if not is_match:
                for t in p.get('tags', []):
                    if s_val in t:
                        is_match = True
                        break 
            
            if is_match:
                results.append(p)
        
        print(f"\n--- Found {len(results)} for '{s_val}' ---")

    if not results:
        print("No matches.")
        return

    for p in results:
        t_s = ", ".join(p.get('tags', []))
        print(f"\nID: {p.get('id')} | Title: {p.get('title')}")
        print(f" Loc: {p.get('location')} | Date: {p.get('date_taken')}")
        print(f" Tags: [{t_s}]")

def updateItem():
    print("\n--- EDIT ENTRY ---")
    
    ID_in = input("ID to modify: ")
    photo = None

    try:
        ID_num = int(ID_in)
        for i in photoList:
            if i.get('id') == ID_num:
                photo = i
                break
    except ValueError:
        pass
    
    if photo is None:
        print(f"ID {ID_in} not found.")
        return

    print(f"\nEditing ID {photo['id']} - '{photo['title']}'")
    
    key_t = 'title'
    cur_t = photo.get(key_t, 'N/A')
    new_t = input(f"New Title (Current: '{cur_t}'): ").strip()
    if new_t != "": 
        photo[key_t] = new_t

    key_l = 'location'
    cur_l = photo.get(key_l, 'N/A')
    new_l = input(f"New Location (Current: '{cur_l}'): ").strip()
    if new_l != "": 
        photo[key_l] = new_l
     
    cur_tag_str = ', '.join(photo.get('tags', []))
    new_tag_in = input(f"New Tags (csv, Current: '{cur_tag_str}'): ").strip()
    if new_tag_in != "":
        photo['tags'] = [t.strip().lower() for t in new_tag_in.split(',') if t.strip() != ""]

    key_f = 'filepath'
    cur_f = photo.get(key_f, 'N/A')
    new_f = input(f"New File Path (Current: '{cur_f}'): ").strip()
    if new_f != "": 
        photo[key_f] = new_f
    
    print(f"\nID {photo['id']} updated.")

def deleteItem():
    global photoList
    print("\n--- DELETE ENTRY ---")
    
    ID_in = input("ID to delete: ")
    photo = None
    idx = -1
    
    try:
        ID_num = int(ID_in)
        for i, p in enumerate(photoList):
            if p.get('id') == ID_num:
                photo = p
                idx = i
                break
    except ValueError:
        pass 
    
    if photo is None:
        print(f"ID {ID_in} not found.")
        return

    c = input(f"Delete '{photo['title']}' (ID: {photo['id']})? (y/N): ").lower()
    
    if c == 'y':
        try:
            del photoList[idx]
            print(f"\nID {ID_in} deleted.")
        except IndexError:
            print("Error deleting item.") 
    else:
        print("\nCancelled.")

def startApp():
    loadData()

    while True:
        print("  My Simple Photo Index")
        print("1. New Item")
        print("2. View/Search")
        print("3. Edit Item")
        print("4. Remove Item")
        print("5. Quit")
        
        choice = input("Option: ")
        
        if choice == '1':
            createItem()
        elif choice == '2':
            readItem()
        elif choice == '3':
            updateItem()
        elif choice == '4':
            deleteItem()
        elif choice == '5': 
            saveData()
            print("\nExiting.")
            break
        else:
            print("\nBad input.")

if __name__ == "__main__":
    startApp()