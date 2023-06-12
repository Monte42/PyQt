# PYQT6 Journey
#### Hello, I am a Jr Developer who recently completed a coding Bootcamp for Web Development. This is my journey of learning PyQt6, self-taught of course. So please excuse the bad practices, :laughing:!  A lot of the ideas and concepts I developed on my own, and did not read anywhere.
 ---
 This is to help serve as a general guide to the layout of projects and folders, and a basic explanation of my learning process. _I recommend using a virtual environment, of course._
 ### Packages Used
 - PyQt6
 - PyQt5
 - PyQt5-tools
 - MySQL Client
```
pip install PyQt6 PyQt5 pyqt5-tools mysqlclient
```
## Repository Layout :file_folder:
I kept the direction of progression pretty simple.  You can follow my path by starting at folder 101, then increase to next folder in sequential order. In some folders there will be sub directories, where I a may have broke that project into parts A and B.
### 101 - Start Of A Journey :sunrise_over_mountains:
- Getting familiar with PyQt and how GUI's are made
- Created, styled, formatted, edited multiple widgets
- Utilized PyQt tools to build .ui and used uic to load UI
### 102 - Build A More Complex App :chart_with_upwards_trend:
#### A - Strengthening The Basics
- Modularize widgets and imported to build one app
- Created a functional menu bar, set apps font and font-size - add widgets to screen
- Achieved functionality from forms, displays from data in a display widget.
#### B - First Attempts With A DB
- Explored working with a DB
- Established connection with DB
- Successfully created :pencil: new elements in the DB
- Collected Data from DB and displayed it on a separate widget
### 201 - Achieve Better Understanding Of MySqlClient :bulb:
- Created login widget
- Completed filter query based on extracted form data
- Compared :eyes: elements of query results with form data to give or deny access :guardsman:
- Display invalid login message if login attempt fails
### 202 - Refining Use Of The DB
#### A - Looking for better practices :thinking:
- Created DB connection once in Main App - Try not to connect ever widget or function
- Successfully shared DB connection with sperate widgets - Preventing multiple connection
- Connected login widget with functional app
- Create and Read capabilities
- Established connection with List Widget Item on click (for a future idea :stuck_out_tongue_winking_eye:)
#### B - CRUD :construction_worker::construction::construction_worker:
- Coming Soon!