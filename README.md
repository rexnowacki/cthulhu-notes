# cthulhu-notes
cli text/markdown notes in python

## Table of Conflicts
* [Features](#features)
* [To-Do](#to-do)

<a name="features"></a>
## Features

**You can**

Write notes
```
$ cn this is actually a pretty bad note.
```

Which will create a directory (first note of the day) with today's date 
and then create a file with today's date and collect all your notes for 
the day.

<a name="to-do"></a>

**Directory clean-up**: Move all January files to a January 2023 folder.
**Write on a specific topic**
```
$ cn -t python read up on argparse module
```
should eventually write a file python.md in ~/notes/python.
