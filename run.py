import os, sys
with open("stat.txt") as file:
    array = [row.strip() for row in file]
os.popen('nvlc '+array[0]+' -d')