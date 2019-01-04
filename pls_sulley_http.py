from sulley import *
import sys

s_initialize("PLS")

# Header containing playlist info
s_static("playlist")
s_static("\n")

# File URL
s_static("File1=")
s_static("http://")
s_string("www.google.com")
s_static("\n")

# Title
s_static("Title=1")
s_string("test")
s_static("\n")

# Lenght of Filename
s_static("Length1=")
s_short(1)
s_static("\n")

# Number of Entries
s_static("NumberOfEntries=")
s_short(1)
s_static("\n")

# Version
s_static("Version=")
s_short(2)
s_static("\n")

i=0
while s_mutate():
    fuzz_file = open('PLS_HTTP/http_pls_test'+str(i)+'.pls', 'w')
    fuzz_file.write(s_render())
    fuzz_file.closed
    i=i+1

print("Sulley PLS fuzzer has generated files\n")


