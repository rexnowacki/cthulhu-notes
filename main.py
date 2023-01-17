# cthulhu notes v0.01 :: mon jan 16 2023

import os
from datetime import datetime
import sys

# Get the home directory
home_dir = os.path.expanduser("~")

# Get the arguments from the command line
args = sys.argv[1:]
file_name = None

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
#if not os.path.exists(notes_dir):
#    os.mkdir(notes_dir)

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
with open(file_name, "a") as f:
    f.write(note + "\n")
