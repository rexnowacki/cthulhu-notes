# cthulhu notes v0.01 :: mon feb 27 2023
import os
from datetime import datetime, timedelta
import sys

# Get the home directory
home_dir = os.path.expanduser("~")

# Get the arguments from the command line
args = sys.argv[1:]
file_name = None
arguments = ['--today', '--yesterday']

# display today's notes
if "--today" in args:
    today = datetime.today().strftime('%Y-%m-%d')
    notes_folder = os.path.join(home_dir, "notes", today)
    if os.path.exists(notes_folder):
        for file_name in os.listdir(notes_folder):
            if file_name.endswith('.md'):
                with open(os.path.join(notes_folder, file_name)) as file:
                    print(file.read())
                    exit()
    else:
        print("No notes found for today.")
        exit()

# yesterday's notes
if "--yesterday" in args:
    yesterday = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
    notes_folder = os.path.join(home_dir, "notes", yesterday)
    if os.path.exists(notes_folder):
        for file_name in os.listdir(notes_folder):
            if file_name.endswith('.md'):
                with open(os.path.join(notes_folder, file_name)) as file:
                    print(file.read())
                    exit()
    else:
        print("No notes found for yesterday.")
        exit()


if "-n" in args:
    # Get the index of the -n argument
    index = args.index("-n")
    file_name = args[index + 1]
    del args[index:index+2]

if not file_name:
    file_name = datetime.now().strftime("%Y-%m-%d") + ".md"

note = " ".join(args)

# Check for the "notes" directory
notes_dir = os.path.join(home_dir, "notes")
if not os.path.exists(notes_dir):
    os.mkdir(notes_dir)

# Enter the "notes" directory
os.chdir(notes_dir)

# Get the current date
date = datetime.now().strftime("%Y-%m-%d")

# Check for a directory with the current date
if not os.path.exists(date):
    os.mkdir(date)

# Enter the directory with the current date
os.chdir(date)

# Create/Open a file with the current date
for a in arguments:
    if a not in note:
        with open(file_name, "a") as f:
            f.write(note + "\n")
