from sulley import *

s_initialize("M3U")

# header
s_static("#EXTM3U\r\n")
s_static("#EXTINF:123, Sample artist - Sample title\r\n")

# Sample URL Resource
s_static("http://")
s_string("www")
s_delim(".")
s_string("example")
s_delim(".")
s_string("com")
s_delim("/")
s_string("test")
s_delim(".")
s_static("m3u")

# Generate Fuzz Samples
i = 0

while s_mutate():
    fuzz_file = open("M3U_HTTP/http-sample-"+str(i)+".m3u", "w")
    fuzz_file.write(s_render())
    fuzz_file.closed
    i = i+1

print("Sulley M3U fuzzer generated files")




