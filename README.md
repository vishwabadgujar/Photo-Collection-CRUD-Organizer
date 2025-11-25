# Photo-Collection-CRUD-Organizer
A simple, command-line tool written in Python to manage and organize photo metadata, including titles, locations, tags, and file paths.

# Features
- Data Persistence: Automatically loads and saves photo records to a local file (my_photos_data.json) using JSON format.

- Unique Indexing: Assigns a unique, incremental ID number to each photo record.

- Add Records: Easily input title, location, tags, file path, and date taken for a new photo.

- View & Search: Display all stored records, or search records by title or tags.

- Edit Records: Update the title, location, tags, or file path of an existing record using its ID.

- Delete Records: Remove a record permanently by its ID, with a confirmation prompt.

- Console Interface: Uses a simple, menu-driven command-line interface for ease of use.

# Installation and Setup
This project requires Python 3.x and uses only standard library modules, so no external installation is necessary.

Prerequisites:-
- Python 3.x

Running the Application
1. Save the Code: Save the provided code into a file named photo_manager.py.

2. Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute:
python photo_manager.py

3. Data File: The application will automatically create a file named my_photos_data.json in the same directory to store your data.

# Usage
The application will present a main menu on startup:
1 add
2 view
3 edit
4 delete
5 quit

pick:

1. Add (Add a New Item)
Selecting 1 prompts you to enter metadata for a new photo. If you leave the 'date' field blank or enter an invalid format, it defaults to the current date.

2. View (View and Search Items)
Selecting 2 prompts you for a search term.

- Enter a blank value to display all saved photo records.

- Enter a search term to filter records by Title or Tags.

3. Edit (Edit an Item)
Selecting 3 asks for the ID of the item you want to edit. It then prompts for new values for the title, location, tags, and file path. You can leave any field blank if you don't want to change that specific attribute.

4. Delete (Delete an Item)
Selecting 4 asks for the ID of the item to delete, followed by a confirmation prompt (y/n) to prevent accidental deletion.

5. Quit
Selecting 5 saves all current changes to my_photos_data.json and exits the application.

# Dependencies
The project relies only on the Python Standard Library:

- json: For reading and writing data to the JSON file.

- os: For checking if the data file exists.

- datetime: For handling date input and setting the current date.

  # Author:
  Vishwa Namdeo Badgujar
