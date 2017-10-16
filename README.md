# gdb automated debugging: 2017 flare-on's pewpewboat

Here's a script to automatically debug Fire Eye's Flare-on challenge #5: pewpewboat.
There are 10 levels to be played, but I wanted to automate the process in case there were *n* levels, where *n* is too big.

The coordinates are always the same for every level. However, NotMd5Hash() is calculated for random values, so you need to read the hash from memory every time and patch it, which is why automated debugging seemed like a good idea.

**Site:** http://flare-on.com/

## Usage

```bash
$ gdb -q -x commandsgdb pewpewboat
```

## Basic explanation

By using gdb's commands and some python code, the following tasks have been automated:
 - Setting a breakpoint after a level is loaded, but before it is launched
 - Setting a breakpoint before NotMd5Hash() and user input are compared
 - Reading coordinates for current level from a structure in memory
 - Writing coordinates to a *.txt* file that will be fed into the program as user input
 - Reading NotMd5Hash() from memory
 - Patching user input to match NotMd5Hash() right before the comparison

## Files

 - ***commandsgdb***: file with gdb commands to perform automated debugging
 - ***boat_coords.py***: some routines and classes that are imported from gdb. They read from memory and write some files, and can be reused.
 - ***coordinates.txt***: result of execution
 - ***pewpewboat***: the original executable. I do not own this. Go visit flare-on's website.

***Note***: when I ran this under Arch Linux, *python* command from gdb didn't work as expected, so I replaced it with *python-interactive* to get it to work. This corresponds to file **commandsgdb_arch**. The original *commandsgdb* was tested on Ubuntu 16.04.
